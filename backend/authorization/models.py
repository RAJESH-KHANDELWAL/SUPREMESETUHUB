"""
MAIN BASE FOUNDATION
AUTHORIZATION MODELS

Data models used by the authorization layer.

This module defines authorization request data only.
It does not contain:
- API logic
- database logic
- engine logic
- core logic
- WordPress logic
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class AuthorizationRequest:
    """Represent an authorization request."""

    request_id: str
    subject_id: str
    resource: str
    action: str
    scope: str

    provider_id: Optional[str] = None
    server_id: Optional[str] = None
    connection_id: Optional[str] = None

    status: str = "PENDING"

    reason: Optional[str] = None

    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    def to_dict(self) -> dict:
        """Return authorization request as a dictionary."""

        return {
            "request_id": self.request_id,
            "subject_id": self.subject_id,
            "resource": self.resource,
            "action": self.action,
            "scope": self.scope,
            "provider_id": self.provider_id,
            "server_id": self.server_id,
            "connection_id": self.connection_id,
            "status": self.status,
            "reason": self.reason,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }


__all__ = [
    "AuthorizationRequest",
]
