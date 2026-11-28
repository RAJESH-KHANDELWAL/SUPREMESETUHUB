"""Bada Business integration provider metadata and resource catalog adapter.

Canonical URLs and program/resource facts remain owned by
backend.global_ecosystem.global_bada_business_ecosystem. This adapter exposes that catalog to the
integration registry without claiming an official API or live connection.
"""
from typing import Any, Dict

from backend.global_ecosystem.global_bada_business_ecosystem.platform_resources import (
    ECOSYSTEM_ID,
    ECOSYSTEM_NAME,
    LIVE_CONNECTION_VERIFIED,
    OFFICIAL_PUBLIC_API_VERIFIED,
    PROVIDER,
    STATUS,
    get_catalog,
)
from backend.integration.base import IntegrationProvider


class BadaBusinessProvider(IntegrationProvider):
    """Expose canonical Bada Business catalog data to integrations."""

    name = "BADA_BUSINESS"
    category = "BUSINESS_ECOSYSTEM"

    def catalog(self) -> Dict[str, Any]:
        """Return the canonical resource catalog without duplicating its data."""
        return get_catalog()

    def metadata(self) -> Dict[str, Any]:
        data = super().metadata()
        catalog = self.catalog()
        data.update(
            {
                "provider": PROVIDER,
                "ecosystem_id": ECOSYSTEM_ID,
                "ecosystem_name": ECOSYSTEM_NAME,
                "catalog_status": STATUS,
                "canonical_catalog": "backend.global_ecosystem.global_bada_business_ecosystem.platform_resources",
                "connector_id": "bada_business",
                "integration_mode": "READ_ONLY_RESOURCE_CATALOG",
                "capabilities": [
                    "RESOURCE_CATALOG",
                    "REFERRAL_LINK_DIRECTORY",
                    "PROGRAM_DIRECTORY",
                    "RESOURCE_LOOKUP",
                ],
                "resource_catalog": catalog,
                "link_count": catalog["link_count"],
                "program_count": catalog["program_count"],
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
                "Canonical Bada Business links and program catalog are available; "
                "no official public API or live provider connection is verified."
            ),
        }


__all__ = ["BadaBusinessProvider"]
