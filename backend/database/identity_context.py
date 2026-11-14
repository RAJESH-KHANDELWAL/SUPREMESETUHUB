"""Request-local identity context helpers.

API middleware should call set_identity only after authentication and
IdentityGateService authorization. Always reset the returned token in finally.
"""
from __future__ import annotations

from contextvars import ContextVar, Token
from dataclasses import dataclass

from backend.database.gde_connection import IDENTITIES


@dataclass(frozen=True)
class IdentityContext:
    identity_code: str
    principal_id: str


_current_identity: ContextVar[IdentityContext | None] = ContextVar(
    "supremesetuhub_identity_context", default=None
)


def set_identity(identity_code: str, principal_id: str) -> Token:
    code = identity_code.strip().upper()
    principal = principal_id.strip()
    if code not in IDENTITIES or not principal:
        raise ValueError("A valid identity code and authenticated principal are required.")
    return _current_identity.set(IdentityContext(code, principal))


def get_identity(required: bool = True) -> IdentityContext | None:
    value = _current_identity.get()
    if required and value is None:
        raise RuntimeError("No identity context is active for this request.")
    return value


def reset_identity(token: Token) -> None:
    _current_identity.reset(token)


__all__ = ["IdentityContext", "set_identity", "get_identity", "reset_identity"]
