"""Read-only facade for the Global Infrastructure Ecosystem."""
from __future__ import annotations

from .catalog import catalog_counts, get_catalog, get_infrastructure_modules
from .governance import get_governance_policies
from .registry import InfrastructureCatalogRegistry
from .structure import (
    get_canonical_ownership,
    get_module_paths,
    get_root_module_paths,
)


class GlobalInfrastructureEcosystemService:
    """Expose catalog, ownership and integration metadata; never executes provider actions."""

    def __init__(self, registry: InfrastructureCatalogRegistry | None = None) -> None:
        self.registry = registry or InfrastructureCatalogRegistry()

    def get_overview(self) -> dict:
        return {
            "ecosystem_id": "global-infrastructure-ecosystem",
            "layer": "INFRASTRUCTURE",
            "status": "CATALOG_FOUNDATION",
            "module_count": len(get_infrastructure_modules()),
            "catalog_counts": catalog_counts(),
            "integrated_foundation_layers": [
                "CORE",
                "GLOBAL_CORE_ECOSYSTEM",
                "GLOBAL_ECOSYSTEM",
            ],
            "provider_operations_enabled": False,
        }

    def get_catalog(self) -> dict:
        return get_catalog()

    def get_modules(self) -> list[str]:
        return list(get_infrastructure_modules())

    def get_module_paths(self) -> dict:
        return {
            "domain_modules": get_module_paths(),
            "infrastructure_root_modules": get_root_module_paths(),
        }

    def get_ownership_map(self) -> dict:
        return get_canonical_ownership()

    def get_governance(self) -> dict:
        return get_governance_policies()
