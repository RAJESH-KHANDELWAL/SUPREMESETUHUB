"""Networking API ecosystem catalog.

Catalog metadata only; this module does not claim live OCI connectivity.
"""
from __future__ import annotations

ORACLE_NETWORKING_API_ECOSYSTEM = {
    "provider_id": "oracle",
    "service_id": "networking",
    "name": "ORACLE NETWORKING API ECOSYSTEM",
    "category": "CLOUD",
    "description": "Virtual cloud networks, subnets, gateways, route tables, security lists, and network security groups.",
    "status": "CATALOG_ONLY",
    "live_connection_verified": False,
    "authentication": "OCI_REQUEST_SIGNATURE_VERSION_1",
    "credential_source": "environment_or_managed_secret_store",
    "requires_least_privilege_iam_policy": True,
}


def get_ecosystem() -> dict[str, object]:
    """Return a copy of this service-family catalog."""
    return dict(ORACLE_NETWORKING_API_ECOSYSTEM)


__all__ = ["ORACLE_NETWORKING_API_ECOSYSTEM", "get_ecosystem"]
