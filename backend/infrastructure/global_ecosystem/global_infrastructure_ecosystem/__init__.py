"""Global Infrastructure Ecosystem package.

This package provides provider-neutral catalogs and metadata only.
It does not provision or mutate external infrastructure.
"""
from .catalog import get_catalog, catalog_counts
from .service import GlobalInfrastructureEcosystemService

LAYER = "INFRASTRUCTURE"
ECOSYSTEM_ID = "global-infrastructure-ecosystem"
STATUS = "CATALOG_FOUNDATION"

__all__ = [
    "LAYER",
    "ECOSYSTEM_ID",
    "STATUS",
    "GlobalInfrastructureEcosystemService",
    "get_catalog",
    "catalog_counts",
]
