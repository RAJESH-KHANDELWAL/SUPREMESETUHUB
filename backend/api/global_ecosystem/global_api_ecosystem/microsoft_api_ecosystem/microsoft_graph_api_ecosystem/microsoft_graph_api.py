"""Microsoft Graph service-family metadata; catalog scaffold, not a live connector."""
from __future__ import annotations

SERVICE_ECOSYSTEM = {
    "provider_id": "microsoft",
    "service_id": "microsoft_graph_api",
    "name": "MICROSOFT GRAPH API ECOSYSTEM",
    "scope": "Users, groups, directory objects, devices, applications, and Microsoft 365 resources exposed through Microsoft Graph.",
    "authentication_setup": "Microsoft Entra app registration, Graph delegated/application permissions, admin consent, tenant ID, client ID, and certificate or client secret.",
    "documentation_required": True,
    "adapter_implemented": False,
    "live_connection_verified": False,
    "credential_persistence_implemented": False,
}

__all__ = ["SERVICE_ECOSYSTEM"]
