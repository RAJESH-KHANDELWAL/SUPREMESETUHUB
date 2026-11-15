"""Azure Database Services service-family metadata; catalog scaffold, not a live connector."""
from __future__ import annotations

SERVICE_ECOSYSTEM = {
    "provider_id": "microsoft",
    "service_id": "microsoft_azure_database_api",
    "name": "AZURE DATABASE SERVICES API ECOSYSTEM",
    "scope": "Azure SQL, Cosmos DB, and managed database resource operations.",
    "authentication_setup": "Azure subscription/RBAC plus database-native authentication and network rules.",
    "documentation_required": True,
    "adapter_implemented": False,
    "live_connection_verified": False,
    "credential_persistence_implemented": False,
}

__all__ = ["SERVICE_ECOSYSTEM"]
