"""Authentication API routes."""

from __future__ import annotations

import secrets

from fastapi import APIRouter, Depends, Header, HTTPException
from pydantic import BaseModel

from backend.auth.controller import AuthenticationController
from backend.security.dependencies import get_current_user


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)

controller = AuthenticationController()


class SignInRequest(BaseModel):
    username: str | None = None
    password: str | None = None
    master_id: str | None = None


class AuthenticateRequest(BaseModel):
    master_id: str


class TokenRequest(BaseModel):
    token: str | None = None
    session_id: str | None = None


@router.get("/initialize")
def initialize():
    return controller.initialize()


@router.post("/signin")
def signin(request: SignInRequest):
    # A master ID identifies an account; it cannot authenticate without a password.
    if not request.username or not request.password:
        raise HTTPException(
            status_code=403,
            detail="PASSWORD_SIGNIN_REQUIRED",
        )

    result = controller.signin(
        username=request.username,
        password=request.password,
    )

    if hasattr(result, "to_dict"):
        result = result.to_dict()

    if isinstance(result, dict) and not result.get("authenticated", False):
        raise HTTPException(
            status_code=401,
            detail=result.get("message") or "INVALID_USERNAME_OR_PASSWORD",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return result


@router.post("/authenticate")
def authenticate(request: AuthenticateRequest):
    # A master ID is an identifier, not an authentication factor.
    # Do not issue an authenticated result based on possession of an ID alone.
    raise HTTPException(
        status_code=403,
        detail="MASTER_ID_ONLY_AUTHENTICATION_DISABLED_USE_PASSWORD_SIGNIN",
    )


@router.post("/validate")
def validate_token(request: TokenRequest):
    return controller.validate_token(
        request.token or ""
    )


@router.post("/signout")
@router.post("/logout", include_in_schema=False)
def signout(
    request: TokenRequest,
    authorization: str | None = Header(default=None, alias="Authorization"),
    current_user: dict = Depends(get_current_user),
):
    """Revoke only the session authenticated by the Bearer token."""
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=401,
            detail="BEARER_TOKEN_REQUIRED",
            headers={"WWW-Authenticate": "Bearer"},
        )

    bearer_token = authorization[len("Bearer "):].strip()
    if not bearer_token:
        raise HTTPException(
            status_code=401,
            detail="BEARER_TOKEN_REQUIRED",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Request-body identifiers must never select a different session.
    if request.session_id and request.session_id != current_user.get("session_id"):
        raise HTTPException(status_code=403, detail="CANNOT_REVOKE_ANOTHER_SESSION")

    # If legacy clients send a body token, it must match the authenticated token.
    if request.token and not secrets.compare_digest(request.token, bearer_token):
        raise HTTPException(status_code=403, detail="SIGNOUT_TOKEN_MISMATCH")

    return controller.signout(token=bearer_token)
