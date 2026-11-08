"""Microsoft Entra / Graph provider adapter with safe live verification."""
from __future__ import annotations

import os
from typing import Any, Dict

import httpx

from ..base import IntegrationProvider
from .readiness import provider_health


class MicrosoftProvider(IntegrationProvider):
    """Microsoft Graph app-only connection verifier; no token persistence."""

    name = "MICROSOFT"
    category = "PRODUCTIVITY_AND_CLOUD"

    def metadata(self) -> Dict[str, Any]:
        return {
            **super().metadata(),
            "capabilities": ["MICROSOFT_ENTRA_ID", "MICROSOFT_GRAPH", "AZURE"],
            "auth_method": "Microsoft Entra ID OAuth 2.0 client credentials",
            "setup_guide": "docs/GOOGLE_MICROSOFT_AWS_APPLE_SETUP.md",
            "live_verification": True,
        }

    def health(self) -> Dict[str, Any]:
        required = ["MICROSOFT_TENANT_ID", "MICROSOFT_CLIENT_ID", "MICROSOFT_CLIENT_SECRET"]
        configured = all(os.getenv(key, "").strip() for key in required)
        return provider_health(
            provider=self.name,
            category=self.category,
            configured=configured,
            auth_method="Microsoft Entra ID OAuth 2.0 client credentials",
            required_configuration=required,
            capabilities=["MICROSOFT_GRAPH", "OUTLOOK", "ONEDRIVE", "SHAREPOINT", "AZURE"],
        )

    def verify_connection(self) -> dict:
        """Exchange app credentials and verify Microsoft Graph organization access."""
        tenant = os.getenv("MICROSOFT_TENANT_ID", "").strip()
        client_id = os.getenv("MICROSOFT_CLIENT_ID", "").strip()
        client_secret = os.getenv("MICROSOFT_CLIENT_SECRET", "").strip()
        missing = [name for name, value in (
            ("MICROSOFT_TENANT_ID", tenant),
            ("MICROSOFT_CLIENT_ID", client_id),
            ("MICROSOFT_CLIENT_SECRET", client_secret),
        ) if not value]
        if missing:
            return {"success": False, "provider": self.name, "status": "NEEDS_CONFIGURATION",
                    "missing_configuration": missing, "live_connection_verified": False}
        if (any(ch in tenant for ch in "/?#") or len(tenant) > 200
                or tenant.casefold() in {"common", "organizations", "consumers"}):
            return {"success": False, "provider": self.name, "status": "INVALID_CONFIGURATION",
                    "error_code": "MICROSOFT_TENANT_ID_INVALID", "live_connection_verified": False}
        token_url = f"https://login.microsoftonline.com/{tenant}/oauth2/v2.0/token"
        try:
            with httpx.Client(timeout=15.0, follow_redirects=False) as client:
                token_response = client.post(token_url, data={
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "scope": "https://graph.microsoft.com/.default",
                    "grant_type": "client_credentials",
                })
                if token_response.status_code != 200:
                    return {"success": False, "provider": self.name, "status": "AUTHENTICATION_FAILED",
                            "error_code": "MICROSOFT_TOKEN_EXCHANGE_FAILED",
                            "http_status": token_response.status_code, "live_connection_verified": False}
                access_token = token_response.json().get("access_token")
                if not isinstance(access_token, str) or not access_token:
                    return {"success": False, "provider": self.name, "status": "AUTHENTICATION_FAILED",
                            "error_code": "MICROSOFT_ACCESS_TOKEN_MISSING", "live_connection_verified": False}
                graph = client.get(
                    "https://graph.microsoft.com/v1.0/organization?$select=id,displayName",
                    headers={"Authorization": f"Bearer {access_token}", "Accept": "application/json"},
                )
                if graph.status_code != 200:
                    return {"success": False, "provider": self.name, "status": "API_PERMISSION_FAILED",
                            "error_code": "MICROSOFT_GRAPH_ORGANIZATION_CHECK_FAILED",
                            "http_status": graph.status_code, "live_connection_verified": False}
                items = graph.json().get("value", [])
                organization = items[0] if items else {}
                return {"success": True, "provider": self.name, "status": "CONNECTED",
                        "connection": "VERIFIED", "tenant_name": organization.get("displayName"),
                        "tenant_object_id": organization.get("id"), "live_connection_verified": True,
                        "credential_persisted": False,
                        "note": "App-only Graph access verified for this request; tokens are discarded, not stored."}
        except (httpx.HTTPError, ValueError, TypeError):
            return {"success": False, "provider": self.name, "status": "CONNECTION_FAILED",
                    "error_code": "MICROSOFT_GRAPH_UNAVAILABLE_OR_INVALID_RESPONSE",
                    "live_connection_verified": False}


__all__ = ["MicrosoftProvider"]
