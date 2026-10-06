# Repository configuration

## Business Scenario

You have a Git repository created for a Python project.


# Tasks

## Task 1: Configure Git Repository for Python Development

Design an appropriate Git repository configuration for a Python project. Consider common Python development artifacts which need to be excluded from source control.


## Task 2: Development-Only (Local) Data

Developers want to reserve a directory named `local/` for development purposes only and exclude it from source control.



## Task 3: Python Virtual Environment Support

Configure the repository to support Python virtual environments.

Assume developers may use:

```bash
python -m venv .venv
```

or

```bash
uv venv
```



## Task 4: Terraform Support

The project uses Terraform for Infrastructure-as-Code (IaC).

Configure the repository appropriately for Terraform development.

Which files would you exclude from source control? Why?



## Additional Tak 1 (exra credits): On commit quality gate

How would you implement a quality gate on commit, so that:
* Tests are executed on commit
* Guarantee minimum test coverage
* Liters are executed on commit against changed files

---

# Scoring

* Total score: 100 points
* Passing score: 80 points
* Additional score: 30 points

## Task 1: Repository Configuration (50 Points)

### `.gitignore` Design (20 Points)

* The proposed `.gitignore` appropriately covers common Python development artifacts.
* Explanation of important exclusions is provided.

Common Python development artifacts
- Compiled Python files
- IDE settings
- Build artifacts
- Cache files
- Logs



### Common Development Artifacts (20 Points)

Candidate identifies and explains exclusion of common files such as:

- Python cache files
- Build artifacts
- IDE files
- Log files
- Test artifacts

Exact memorization of every file pattern is not required if the rationale is explained correctly.

### Repository Structure Discussion (10 Points)

Candidate correctly distinguishes between:

- Files that should be version-controlled
- Files that should remain local

---

## Task 2: Development-Only Data (10 Points)

Candidate proposes a practical solution for the `local/` directory.

Examples include:

- Ignoring the directory through `.gitignore`
- Using placeholder files where appropriate
- Explaining team development considerations

---

## Task 3: Python Virtual Environment Support (10 Points)

Candidate correctly handles virtual environments.

Expected considerations include:

- Excluding `.venv`
- Avoiding commits of environment-specific files
- Retaining dependency definitions such as `requirements.txt` or `pyproject.toml`

---

## Task 4: Terraform Support (30 Points)

### Terraform State Files (10 Points)

Candidate excludes Terraform state files:

```text
*.tfstate
```

### Terraform Backup State Files (10 Points)

Candidate excludes Terraform state variations:

```text
*.tfstate*
```

### Terraform Working Directory (5 Points)

Candidate excludes:

```text
.terraform/
```

### Terraform Variable Files (5 Poi*ts)

Candidate excludes sensitive *ariable files:

```text
*.tfvars
```


---


**Skills Assessed

- Git fundamental*
- Source control best practices
- `.gitignore` configuration
- Python development workflows
- Virtual environment management
- Terraform development practices
- Local vs shared configuration management - Repository structure design
- Security awareness (state files and secrets)
```



