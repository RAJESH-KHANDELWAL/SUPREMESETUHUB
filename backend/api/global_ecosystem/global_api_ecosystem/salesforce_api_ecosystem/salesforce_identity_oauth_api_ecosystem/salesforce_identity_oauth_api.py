"""Salesforce Identity and OAuth service-family metadata; catalog scaffold, not a live connector."""
from __future__ import annotations

SERVICE_ECOSYSTEM = {
    "provider_id": "salesforce",
    "service_id": "salesforce_identity_oauth_api",
    "name": "SALESFORCE IDENTITY AND OAUTH API ECOSYSTEM",
    "scope": "OAuth 2.0 flows, Connected Apps, identity, token lifecycle, and org discovery.",
    "authentication_setup": "Salesforce Connected App, client ID/secret, approved callback URL, scopes, and org domain.",
    "documentation_required": True,
    "adapter_implemented": False,
    "live_connection_verified": False,
    "credential_persistence_implemented": False,
}

__all__ = ["SERVICE_ECOSYSTEM"]
