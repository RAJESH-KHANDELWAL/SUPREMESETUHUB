"""Autonomous Database API ecosystem catalog.

Catalog metadata only; this module does not claim live OCI connectivity.
"""
from __future__ import annotations

ORACLE_AUTONOMOUS_DATABASE_API_ECOSYSTEM = {
    "provider_id": "oracle",
    "service_id": "autonomous_database",
    "name": "ORACLE AUTONOMOUS DATABASE API ECOSYSTEM",
    "category": "DATABASE",
    "description": "Autonomous Database lifecycle, configuration, backups, and connection metadata.",
    "status": "CATALOG_ONLY",
    "live_connection_verified": False,
    "authentication": "OCI_REQUEST_SIGNATURE_VERSION_1",
    "credential_source": "environment_or_managed_secret_store",
    "requires_least_privilege_iam_policy": True,
}


def get_ecosystem() -> dict[str, object]:
    """Return a copy of this service-family catalog."""
    return dict(ORACLE_AUTONOMOUS_DATABASE_API_ECOSYSTEM)


__all__ = ["ORACLE_AUTONOMOUS_DATABASE_API_ECOSYSTEM", "get_ecosystem"]
