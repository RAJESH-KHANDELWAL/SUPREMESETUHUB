"""Microsoft Entra Identity and OAuth service-family metadata; catalog scaffold, not a live connector."""
from __future__ import annotations

SERVICE_ECOSYSTEM = {
    "provider_id": "microsoft",
    "service_id": "microsoft_entra_identity_oauth_api",
    "name": "MICROSOFT ENTRA IDENTITY AND OAUTH API ECOSYSTEM",
    "scope": "OAuth 2.0, OpenID Connect, app registrations, service principals, and identity lifecycle.",
    "authentication_setup": "Tenant ID, client ID, approved redirect URI, certificate/client secret, and least-privilege scopes.",
    "documentation_required": True,
    "adapter_implemented": False,
    "live_connection_verified": False,
    "credential_persistence_implemented": False,
}

__all__ = ["SERVICE_ECOSYSTEM"]
