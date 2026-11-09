"""Virtual Cloud Networks API ecosystem catalog.

Catalog metadata only; this module does not claim live OCI connectivity.
"""
from __future__ import annotations

ORACLE_VIRTUAL_CLOUD_NETWORKS_API_ECOSYSTEM = {
    "provider_id": "oracle",
    "service_id": "virtual_cloud_networks",
    "name": "ORACLE VIRTUAL CLOUD NETWORKS API ECOSYSTEM",
    "category": "VPS",
    "description": "VPS-oriented VCN, subnet, routing, security, and public/private network resources.",
    "status": "CATALOG_ONLY",
    "live_connection_verified": False,
    "authentication": "OCI_REQUEST_SIGNATURE_VERSION_1",
    "credential_source": "environment_or_managed_secret_store",
    "requires_least_privilege_iam_policy": True,
}


def get_ecosystem() -> dict[str, object]:
    """Return a copy of this service-family catalog."""
    return dict(ORACLE_VIRTUAL_CLOUD_NETWORKS_API_ECOSYSTEM)


__all__ = ["ORACLE_VIRTUAL_CLOUD_NETWORKS_API_ECOSYSTEM", "get_ecosystem"]
