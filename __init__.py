"""Global Infrastructure Ecosystem: domain adapters and cross-layer discovery hub."""
from .catalog import get_catalog, catalog_counts
from .service import GlobalInfrastructureEcosystemService
from .structure import (
    get_canonical_ownership,
    get_ecosystem_domain_paths,
    get_module_paths,
    get_root_module_paths,
)

LAYER = "INFRASTRUCTURE"
ECOSYSTEM_ID = "global-infrastructure-ecosystem"
STATUS = "DOMAIN_ADAPTERS_REGISTERED"

__all__ = [
    "LAYER", "ECOSYSTEM_ID", "STATUS", "GlobalInfrastructureEcosystemService",
    "get_catalog", "catalog_counts", "get_canonical_ownership",
    "get_ecosystem_domain_paths", "get_module_paths", "get_root_module_paths",
]
