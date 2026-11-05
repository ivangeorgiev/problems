"""
https://www.datacamp.com/tutorial/introduction-fastapi-tutorial?utm_cid=23781701478
"""

import uuid
from collections.abc import Iterable
from dataclasses import dataclass
from enum import StrEnum, auto
from typing import Annotated

from fastapi import Depends, FastAPI, Header, HTTPException, Request, Response, status
from fastapi.security import APIKeyHeader

app = FastAPI()


api_key_header = APIKeyHeader(name="Authorization", auto_error=False)


@dataclass
class UserTeamRole:
    user_id: int
    team_id: int
    roles: list[str]


class UserId(StrEnum):
    ADMIN = auto()
    MULTI_ADMIN = auto()
    READER = auto()


async def get_authenticated_user_id(
    user_id: Annotated[UserId, Header(alias="X-User-Id")],
):
    return user_id


# Mock database helper
async def get_user_from_db(token: str):
    if token == "super-admin-token":
        return {"username": "alice", "role": "admin"}
    if token == "regular-user-token":
        return {"username": "bob", "role": "user"}
    return None


async def get_user_team_roles(user_id: UserId) -> Iterable[UserTeamRole]:
    match user_id:
        case UserId.ADMIN:
            return [UserTeamRole(user_id, 1, ["admin"])]
        case UserId.MULTI_ADMIN:
            return [
                UserTeamRole(user_id, 1, ["admin"]),
                UserTeamRole(user_id, 2, ["admin"]),
            ]
        case UserId.READER:
            return [UserTeamRole(user_id, 1, ["reader"])]
        case _:
            return []


async def get_owning_team_id(
    response: Response,
    request: Request,
    user_id: Annotated[str, Depends(get_authenticated_user_id)],
):
    teams = [t for t in await get_user_team_roles(user_id) if "admin" in t.roles]
    if not teams:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="No admin role assignments found.",
        )
    if len(teams) > 1:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Multiple admin role assignments found.",
        )
    yield teams[0].team_id
    print("After request")


@app.get("/func", dependencies=[Depends(get_owning_team_id)])
def func(
    correlation_id: Annotated[
        str,
        Header(
            default_factory=lambda: str(uuid.uuid4()),
            description="Correlation Identifier",
            alias="X-Correlation-ID",
        ),
    ],
    team_id: Annotated[str, Depends(get_owning_team_id)],
):
    return {
        "result": "123",
        "correlation_id": correlation_id,
        "team": team_id,
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app="main:app", reload=True)
