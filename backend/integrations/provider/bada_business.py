"""Bada Business integration provider metadata and readiness contract.

Canonical platform links and program/resource facts remain owned by
backend.bada_business_ecosystem. This module does not claim an official API
or a verified live connection.
"""
from typing import Any, Dict

from backend.bada_business_ecosystem.platform_resources import (
    ECOSYSTEM_ID,
    ECOSYSTEM_NAME,
    LIVE_CONNECTION_VERIFIED,
    OFFICIAL_PUBLIC_API_VERIFIED,
    PROVIDER,
    STATUS,
)
from backend.integrations.base import IntegrationProvider


class BadaBusinessProvider(IntegrationProvider):
    """Expose canonical Bada Business ecosystem metadata to integrations."""

    name = "BADA_BUSINESS"
    category = "BUSINESS_ECOSYSTEM"

    def metadata(self) -> Dict[str, Any]:
        data = super().metadata()
        data.update(
            {
                "provider": PROVIDER,
                "ecosystem_id": ECOSYSTEM_ID,
                "ecosystem_name": ECOSYSTEM_NAME,
                "catalog_status": STATUS,
                "canonical_catalog": "backend.bada_business_ecosystem.platform_resources",
                "official_public_api_verified": OFFICIAL_PUBLIC_API_VERIFIED,
                "live_connection_verified": LIVE_CONNECTION_VERIFIED,
            }
        )
        return data

    def health(self) -> Dict[str, Any]:
        # Catalog metadata is available, but credentials/API/live connectivity
        # are not asserted by this provider adapter.
        return {
            **self.metadata(),
            "authentication": "NOT_CONFIGURED",
            "connection": "NOT_CONNECTED",
            "live_connection_verified": False,
            "status": "CATALOG_AVAILABLE",
            "message": (
                "Canonical Bada Business resource catalog is available; "
                "no official public API or live provider connection is verified."
            ),
        }


__all__ = ["BadaBusinessProvider"]
