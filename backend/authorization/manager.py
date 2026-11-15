"""
MAIN BASE FOUNDATION
AUTHORIZATION MANAGER

Manages authorization requests.

This module is responsible only for authorization-request
lifecycle management.

It does not contain:
- API routing
- database operations
- WordPress operations
- hosting operations
- domain operations
- server operations
- engine logic
"""

from __future__ import annotations

from typing import Dict, Optional

from .models import AuthorizationRequest


class AuthorizationManager:
    """Manage authorization requests."""

    def __init__(self) -> None:
        self.requests: Dict[
            str,
            AuthorizationRequest,
        ] = {}

    # ------------------------------------------------------------------
    # REQUEST
    # ------------------------------------------------------------------

    def request(
        self,
        request_id: str,
        subject_id: str,
        resource: str,
        action: str,
        scope: str,
        provider_id: Optional[str] = None,
        server_id: Optional[str] = None,
        connection_id: Optional[str] = None,
        reason: Optional[str] = None,
    ) -> dict:
        """Create a new authorization request."""

        if request_id in self.requests:
            return {
                "success": False,
                "error": "REQUEST_ID_ALREADY_EXISTS",
                "request_id": request_id,
            }

        authorization = AuthorizationRequest(
            request_id=request_id,
            subject_id=subject_id,
            resource=resource,
            action=action,
            scope=scope,
            provider_id=provider_id,
            server_id=server_id,
            connection_id=connection_id,
            reason=reason,
        )

        self.requests[request_id] = authorization

        return {
            "success": True,
            "authorization": authorization.to_dict(),
        }

    # ------------------------------------------------------------------
    # GET
    # ------------------------------------------------------------------

    def get(
        self,
        request_id: str,
    ) -> dict:
        """Return one authorization request."""

        authorization = self.requests.get(
            request_id
        )

        if authorization is None:
            return {
                "success": False,
                "error": "REQUEST_NOT_FOUND",
                "request_id": request_id,
            }

        return {
            "success": True,
            "authorization": authorization.to_dict(),
        }

    # ------------------------------------------------------------------
    # APPROVE
    # ------------------------------------------------------------------

    def approve(
        self,
        request_id: str,
    ) -> dict:
        """Approve an authorization request."""

        authorization = self.requests.get(
            request_id
        )

        if authorization is None:
            return {
                "success": False,
                "error": "REQUEST_NOT_FOUND",
                "request_id": request_id,
            }

        authorization.status = "APPROVED"

        return {
            "success": True,
            "authorization": authorization.to_dict(),
        }

    # ------------------------------------------------------------------
    # DENY
    # ------------------------------------------------------------------

    def deny(
        self,
        request_id: str,
        reason: Optional[str] = None,
    ) -> dict:
        """Deny an authorization request."""

        authorization = self.requests.get(
            request_id
        )

        if authorization is None:
            return {
                "success": False,
                "error": "REQUEST_NOT_FOUND",
                "request_id": request_id,
            }

        authorization.status = "DENIED"

        if reason:
            authorization.reason = reason

        return {
            "success": True,
            "authorization": authorization.to_dict(),
        }

    # ------------------------------------------------------------------
    # REVOKE
    # ------------------------------------------------------------------

    def revoke(
        self,
        request_id: str,
        reason: Optional[str] = None,
    ) -> dict:
        """Revoke an approved authorization."""

        authorization = self.requests.get(
            request_id
        )

        if authorization is None:
            return {
                "success": False,
                "error": "REQUEST_NOT_FOUND",
                "request_id": request_id,
            }

        authorization.status = "REVOKED"

        if reason:
            authorization.reason = reason

        return {
            "success": True,
            "authorization": authorization.to_dict(),
        }

    # ------------------------------------------------------------------
    # LIST
    # ------------------------------------------------------------------

    def list(self) -> dict:
        """Return all authorization requests."""

        return {
            "success": True,
            "count": len(self.requests),
            "requests": [
                request.to_dict()
                for request in self.requests.values()
            ],
        }

    # ------------------------------------------------------------------
    # HEALTH
    # ------------------------------------------------------------------

    def health(self) -> dict:
        """Return authorization manager health."""

        return {
            "system": "Authorization Manager",
            "health": "HEALTHY",
            "requests": len(self.requests),
        }


__all__ = [
    "AuthorizationManager",
]
