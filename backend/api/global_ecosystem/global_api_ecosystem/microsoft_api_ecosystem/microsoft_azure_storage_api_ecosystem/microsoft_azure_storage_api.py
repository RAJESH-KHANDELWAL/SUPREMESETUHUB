"""Azure Storage service-family metadata; catalog scaffold, not a live connector."""
from __future__ import annotations

SERVICE_ECOSYSTEM = {
    "provider_id": "microsoft",
    "service_id": "microsoft_azure_storage_api",
    "name": "AZURE STORAGE API ECOSYSTEM",
    "scope": "Blob containers, objects, queues, tables, and storage account management.",
    "authentication_setup": "Storage account endpoint and managed identity or scoped SAS/RBAC credentials.",
    "documentation_required": True,
    "adapter_implemented": False,
    "live_connection_verified": False,
    "credential_persistence_implemented": False,
}

__all__ = ["SERVICE_ECOSYSTEM"]
