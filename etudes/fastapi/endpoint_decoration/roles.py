from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Security, status
from fastapi.security import APIKeyHeader

app = FastAPI()

# A mock security scheme (e.g., looking for 'Authorization' header)
api_key_header = APIKeyHeader(name="Authorization", auto_error=False)


# Mock database helper
async def get_user_from_db(token: str):
    if token == "super-admin-token":
        return {"username": "alice", "role": "admin"}
    if token == "regular-user-token":
        return {"username": "bob", "role": "user"}
    return None


# 1. AUTHENTICATION: Validates identity
async def get_current_user(token: Annotated[str, Security(api_key_header)]):
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing Token"
        )

    user = await get_user_from_db(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Token"
        )
    return user


# 2. AUTHORIZATION FACTORY: Validates permissions/roles
class RequireRole:
    def __init__(self, allowed_roles: list[str]):
        self.allowed_roles = allowed_roles

    def __call__(self, current_user: Annotated[dict, Depends(get_current_user)]):
        if current_user["role"] not in self.allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You do not have permission to access this resource",
            )
        return current_user


@app.get("/analytics")
async def get_analytics(
    # Only users with 'admin' role can enter; returns the user object if successful
    user: Annotated[dict, Depends(RequireRole(["admin"]))],
):
    return {"message": f"Welcome Admin {user['username']}. Here is secret data."}


@app.get("/dashboard")
async def get_dashboard(
    # Both admins and regular users can enter
    user: Annotated[dict, Depends(RequireRole(["admin", "user"]))],
):
    return {"message": f"Hello {user['username']}"}
