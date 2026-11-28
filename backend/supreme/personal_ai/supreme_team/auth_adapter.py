"""Trusted authentication adapter for SUPREME Team APIs.

Role assignments come only from server-side SUPREME_TEAM_ROLE_MAP JSON.
Never accept roles or actor identity from client-supplied request fields.
"""
from __future__ import annotations

import json
import os

from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from backend.auth.service import AuthenticationService
from .management import Actor

_bearer = HTTPBearer(auto_error=False)
_authentication = AuthenticationService()


def get_team_actor(
    credentials: HTTPAuthorizationCredentials | None = Depends(_bearer),
) -> Actor:
    if credentials is None or credentials.scheme.lower() != "bearer":
        raise HTTPException(status_code=401, detail="AUTHENTICATION_REQUIRED")

    session = _authentication.validate_token(credentials.credentials)
    if not session.get("authenticated"):
        raise HTTPException(status_code=401, detail="INVALID_OR_EXPIRED_SESSION")

    try:
        role_map = json.loads(os.getenv("SUPREME_TEAM_ROLE_MAP", "{}"))
    except json.JSONDecodeError as exc:
        raise HTTPException(status_code=503, detail="SUPREME_TEAM_ROLE_MAP_INVALID") from exc

    if not isinstance(role_map, dict):
        raise HTTPException(status_code=503, detail="SUPREME_TEAM_ROLE_MAP_INVALID")

    username = str(session.get("username", "")).strip().casefold()
    role = role_map.get(username)
    if role not in {
        "OWNER", "CMD", "MD", "DIRECTOR", "DEPARTMENT_HEAD",
        "EXECUTIVE", "MANAGER", "TEAM_LEADER", "TEAM_MEMBER",
    }:
        raise HTTPException(status_code=403, detail="SUPREME_TEAM_ROLE_NOT_ASSIGNED")

    return Actor(
        actor_id=username,
        role=role,
        authenticated=True,
    )
