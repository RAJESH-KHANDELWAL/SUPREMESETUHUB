"""Azure Compute service-family metadata; catalog scaffold, not a live connector."""
from __future__ import annotations

SERVICE_ECOSYSTEM = {
    "provider_id": "microsoft",
    "service_id": "microsoft_azure_compute_api",
    "name": "AZURE COMPUTE API ECOSYSTEM",
    "scope": "Virtual Machines, disks, images, scale sets, and compute resource management.",
    "authentication_setup": "Azure subscription, Entra service principal, Azure Resource Manager role assignment.",
    "documentation_required": True,
    "adapter_implemented": False,
    "live_connection_verified": False,
    "credential_persistence_implemented": False,
}

__all__ = ["SERVICE_ECOSYSTEM"]
