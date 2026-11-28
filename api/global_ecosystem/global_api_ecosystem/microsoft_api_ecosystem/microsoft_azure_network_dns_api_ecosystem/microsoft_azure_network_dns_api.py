"""Azure Networking and DNS service-family metadata; catalog scaffold, not a live connector."""
from __future__ import annotations

SERVICE_ECOSYSTEM = {
    "provider_id": "microsoft",
    "service_id": "microsoft_azure_network_dns_api",
    "name": "AZURE NETWORKING AND DNS API ECOSYSTEM",
    "scope": "Virtual networks, subnets, network security groups, public IPs, and DNS zones.",
    "authentication_setup": "Azure subscription and narrowly scoped Network/DNS resource roles.",
    "documentation_required": True,
    "adapter_implemented": False,
    "live_connection_verified": False,
    "credential_persistence_implemented": False,
}

__all__ = ["SERVICE_ECOSYSTEM"]
