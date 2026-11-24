"""Salesforce Connected App provider adapter with safe live verification."""
from __future__ import annotations

import os
from urllib.parse import urlparse
from typing import Any, Dict

import httpx

from ..base import IntegrationProvider
from .readiness import provider_health


class SalesforceProvider(IntegrationProvider):
    """Salesforce OAuth client-credentials verifier; tokens are never persisted."""

    name = "SALESFORCE"
    category = "CRM_AND_BUSINESS_APPLICATIONS"

    def metadata(self) -> Dict[str, Any]:
        return {
            **super().metadata(),
            "official_api": "Salesforce REST API",
            "capabilities": ["IDENTITY_OAUTH", "REST", "SOAP", "COMPOSITE", "BULK_API_2",
                             "PLATFORM_EVENTS", "METADATA_TOOLING", "FILES_CONTENT", "ANALYTICS"],
            "auth_method": "Salesforce Connected App OAuth 2.0 client credentials",
            "live_verification": True,
        }

    def health(self) -> Dict[str, Any]:
        required = ["SALESFORCE_CLIENT_ID", "SALESFORCE_CLIENT_SECRET"]
        configured = all(os.getenv(key, "").strip() for key in required)
        return provider_health(
            provider=self.name,
            category=self.category,
            configured=configured,
            auth_method="Salesforce Connected App OAuth 2.0 client credentials",
            required_configuration=required,
            capabilities=["REST", "SOAP", "COMPOSITE", "BULK_API_2", "FILES_CONTENT", "ANALYTICS"],
        )

    def verify_connection(self) -> dict:
        """Obtain an OAuth access token and call the authenticated REST limits API."""
        client_id = os.getenv("SALESFORCE_CLIENT_ID", "").strip()
        client_secret = os.getenv("SALESFORCE_CLIENT_SECRET", "").strip()
        login_url = os.getenv("SALESFORCE_LOGIN_URL", "https://login.salesforce.com").strip().rstrip("/")
        api_version = os.getenv("SALESFORCE_API_VERSION", "v66.0").strip()
        missing = [name for name, value in (
            ("SALESFORCE_CLIENT_ID", client_id),
            ("SALESFORCE_CLIENT_SECRET", client_secret),
        ) if not value]
        if missing:
            return {"success": False, "provider": self.name, "status": "NEEDS_CONFIGURATION",
                    "missing_configuration": missing, "live_connection_verified": False}
        login = urlparse(login_url)
        if login.scheme != "https" or login.hostname not in {"login.salesforce.com", "test.salesforce.com"}:
            return {"success": False, "provider": self.name, "status": "INVALID_CONFIGURATION",
                    "error_code": "SALESFORCE_LOGIN_URL_NOT_ALLOWED", "live_connection_verified": False}
        if not api_version.startswith("v") or not api_version[1:].replace(".", "").isdigit():
            return {"success": False, "provider": self.name, "status": "INVALID_CONFIGURATION",
                    "error_code": "SALESFORCE_API_VERSION_INVALID", "live_connection_verified": False}
        try:
            with httpx.Client(timeout=15.0, follow_redirects=False) as client:
                token_response = client.post(
                    f"{login_url}/services/oauth2/token",
                    data={"grant_type": "client_credentials", "client_id": client_id,
                          "client_secret": client_secret},
                )
                if token_response.status_code != 200:
                    return {"success": False, "provider": self.name, "status": "AUTHENTICATION_FAILED",
                            "error_code": "SALESFORCE_TOKEN_EXCHANGE_FAILED",
                            "http_status": token_response.status_code, "live_connection_verified": False}
                token_data = token_response.json()
                access_token = token_data.get("access_token")
                instance_url = token_data.get("instance_url")
                parsed_instance = urlparse(instance_url or "")
                host = (parsed_instance.hostname or "").lower()
                if (not isinstance(access_token, str) or not access_token
                        or parsed_instance.scheme != "https"
                        or not (host.endswith(".salesforce.com") or host.endswith(".force.com"))):
                    return {"success": False, "provider": self.name, "status": "AUTHENTICATION_FAILED",
                            "error_code": "SALESFORCE_TOKEN_RESPONSE_INVALID", "live_connection_verified": False}
                response = client.get(
                    f"{instance_url}/services/data/{api_version}/limits",
                    headers={"Authorization": f"Bearer {access_token}", "Accept": "application/json"},
                )
                if response.status_code != 200:
                    return {"success": False, "provider": self.name, "status": "API_PERMISSION_FAILED",
                            "error_code": "SALESFORCE_REST_LIMITS_CHECK_FAILED",
                            "http_status": response.status_code, "live_connection_verified": False}
                return {"success": True, "provider": self.name, "status": "CONNECTED",
                        "connection": "VERIFIED", "instance_host": host, "api_version": api_version,
                        "live_connection_verified": True, "credential_persisted": False,
                        "note": "Salesforce OAuth and REST API access verified for this request; tokens are discarded, not stored."}
        except (httpx.HTTPError, ValueError, TypeError):
            return {"success": False, "provider": self.name, "status": "CONNECTION_FAILED",
                    "error_code": "SALESFORCE_API_UNAVAILABLE_OR_INVALID_RESPONSE",
                    "live_connection_verified": False}


__all__ = ["SalesforceProvider"]
