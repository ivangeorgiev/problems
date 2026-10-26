
Unity Service allows multiple teams to share same Unity Catalog Metastore by providing access control to Securable Objects

The company has multiple applications. Application is implemented by teams.

Applications are registered by sugmitting application registration. Reviewer approves application registrations. The person submitted the application becomes Application Administrator. Application Administor can manage applicaton teams. Application team is managed by team administrators.

Team securable objects are managed by managing identities from the same team.

## Conceptual Data Model

```mermaid
erDiagram
	IDENTITY ||--o{ APPLICATION_ADMIN : administers
	APPLICATION ||--|{ APPLICATION_ADMIN : has
	APPLICATION ||--|{ TEAM : contains
	IDENTITY ||--o{ TEAM_MEMBERSHIP : has
	TEAM ||--|{ TEAM_MEMBERSHIP : includes
	TEAM ||--o{ SECURABLE_OBJECT : owns
	IDENTITY ||--o{ APPLICATION_REGISTRATION : submits
	APPLICATION_REGISTRATION ||--o{ REGISTRATION_REVIEW : has
	IDENTITY ||--o{ REGISTRATION_REVIEW : reviews
	APPLICATION_REGISTRATION ||--o| APPLICATION : approved_as

	IDENTITY {
		string identity_id PK
		string identity_provider
	}
	APPLICATION_REGISTRATION {
		string registration_id PK
		string name
		string description
		datetime submitted_at
		string submitter_identity_id FK
	}
	REGISTRATION_REVIEW {
		string review_id PK
		string registration_id FK
		string reviewer_identity_id FK
		string result
		string comment
		datetime reviewed_at
	}
	APPLICATION {
		string application_id PK
		string registration_id FK
		string name
		string description
		string latest_review_result
		datetime latest_reviewed_at
	}
	APPLICATION_ADMIN {
		string application_id PK, FK
		string identity_id PK, FK
	}
	TEAM {
		string team_id PK
		string application_id FK
		string name
	}
	TEAM_MEMBERSHIP {
		string team_id PK, FK
		string identity_id PK, FK
		string role
	}
	SECURABLE_OBJECT {
		string object_id PK
		string team_id FK
		string unity_catalog_name
		string object_type
		string parent_object_id
	}
```

An Application Registration holds the submitted application details. Each review is a separate, immutable decision record, preserving who reviewed it, the result, and when. An approved registration creates an Application and assigns its submitter as an Application Administrator. The Application may materialize the latest review result for convenient reads; Registration Review records remain the authoritative history. An Identity is identified by a stable ID from the company's identity provider; credentials are not managed by this service. Application Administrators manage application teams and assign Team Administrators. Each Team Membership has a role, and Unity Service uses that role together with the securable object's owning team to authorize requests. There are no per-object privilege grants: the role-to-action policy determines which operations a team member may perform on objects owned by that team.

## REST API Design

All endpoints use JSON under `/api/v1`. The caller's identity comes from the authenticated request, never from a caller-supplied identity field. List endpoints are paginated. Return `401` for unauthenticated requests, `403` for unauthorized requests, `404` for missing resources, `409` for conflicting state, and `422` for invalid input.

```mermaid
flowchart TD
	subgraph Registration[Application registration: reviewer workflow]
		submitter[Authenticated submitter] -->|POST /application-registrations| registration[(Application Registration)]
		reviewer[Reviewer] -->|GET /application-registrations/:registrationId| registration
		reviewer -->|POST /application-registrations/:registrationId/reviews| review[(Registration Review)]
		registration -->|GET /application-registrations/:registrationId/reviews| review
		review --> decision{Result?}
		decision -->|APPROVED: create application and assign submitter as Application Administrator| app[(Application)]
		decision -->|REJECTED: preserve review result| registration
		app -. may materialize latest result .-> review
	end

	subgraph Teams[Application and team administration]
		appAdmin[Application Administrator] -->|GET /applications/:applicationId/teams| app
		appAdmin -->|POST /applications/:applicationId/teams| team[(Team)]
		appAdmin -->|POST /teams/:teamId/members with role ADMINISTRATOR| membership[(Team Membership)]
		teamAdmin[Team Administrator] -->|POST /teams/:teamId/members| membership
		teamAdmin -->|PATCH or DELETE /teams/:teamId/members/:identityId| membership
	end

	subgraph Access[Team-owned Unity Catalog access]
	member[Authenticated team member] -->|Request operation on securable object| gateway[Unity Service authorization gateway]
	teamAdmin[Team Administrator] -->|Manage team membership and roles| membership
	membership -->|role| gateway
	object[(Securable Object)] -->|owning team| gateway
	gateway -->|Role permits operation| unityCatalog[(Unity Catalog Metastore)]
	gateway -->|Role does not permit operation| denied[403 Forbidden]
	end
```

The service must verify that each team belongs to the referenced application and each securable object is associated with its owning team. The role-to-action policy is applied by Unity Service before forwarding an authorized request to Unity Catalog. Application-level administration does not implicitly grant securable-object access. Membership or role changes are the way to change a team's authorization; the API has no per-object grant or revoke endpoints.
