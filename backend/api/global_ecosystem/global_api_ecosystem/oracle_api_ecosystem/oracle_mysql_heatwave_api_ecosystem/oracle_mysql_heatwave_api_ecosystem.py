"""MySQL HeatWave API ecosystem catalog.

Catalog metadata only; this module does not claim live OCI connectivity.
"""
from __future__ import annotations

ORACLE_MYSQL_HEATWAVE_API_ECOSYSTEM = {
    "provider_id": "oracle",
    "service_id": "mysql_heatwave",
    "name": "ORACLE MYSQL HEATWAVE API ECOSYSTEM",
    "category": "DATABASE",
    "description": "OCI MySQL HeatWave DB systems, backups, configurations, and lifecycle management.",
    "status": "CATALOG_ONLY",
    "live_connection_verified": False,
    "authentication": "OCI_REQUEST_SIGNATURE_VERSION_1",
    "credential_source": "environment_or_managed_secret_store",
    "requires_least_privilege_iam_policy": True,
}


def get_ecosystem() -> dict[str, object]:
    """Return a copy of this service-family catalog."""
    return dict(ORACLE_MYSQL_HEATWAVE_API_ECOSYSTEM)


__all__ = ["ORACLE_MYSQL_HEATWAVE_API_ECOSYSTEM", "get_ecosystem"]
