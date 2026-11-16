"""Microsoft Security and Defender service-family metadata; catalog scaffold, not a live connector."""
from __future__ import annotations

SERVICE_ECOSYSTEM = {
    "provider_id": "microsoft",
    "service_id": "microsoft_security_defender_api",
    "name": "MICROSOFT SECURITY AND DEFENDER API ECOSYSTEM",
    "scope": "Microsoft Defender security data and supported security operations APIs.",
    "authentication_setup": "Entra app registration, Security.* permissions, admin consent, and product licensing.",
    "documentation_required": True,
    "adapter_implemented": False,
    "live_connection_verified": False,
    "credential_persistence_implemented": False,
}

__all__ = ["SERVICE_ECOSYSTEM"]
