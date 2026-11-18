"""Power Platform service-family metadata; catalog scaffold, not a live connector."""
from __future__ import annotations

SERVICE_ECOSYSTEM = {
    "provider_id": "microsoft",
    "service_id": "microsoft_power_platform_api",
    "name": "POWER PLATFORM API ECOSYSTEM",
    "scope": "Power Apps, Power Automate, Dataverse, and environment administration APIs.",
    "authentication_setup": "Tenant/environment IDs, Entra app registration, Dataverse application user, and environment roles.",
    "documentation_required": True,
    "adapter_implemented": False,
    "live_connection_verified": False,
    "credential_persistence_implemented": False,
}

__all__ = ["SERVICE_ECOSYSTEM"]
