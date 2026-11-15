"""Read-only facade for the Global Infrastructure Ecosystem."""
from __future__ import annotations

from .catalog import catalog_counts, get_catalog, get_infrastructure_modules
from .governance import get_governance_policies
from .registry import InfrastructureCatalogRegistry


class GlobalInfrastructureEcosystemService:
    """Expose catalog and governance metadata; never executes provider actions."""

    def __init__(self, registry: InfrastructureCatalogRegistry | None = None) -> None:
        self.registry = registry or InfrastructureCatalogRegistry()

    def get_overview(self) -> dict:
        return {
            "ecosystem_id": "global-infrastructure-ecosystem",
            "layer": "INFRASTRUCTURE",
            "status": "CATALOG_FOUNDATION",
            "module_count": len(get_infrastructure_modules()),
            "catalog_counts": catalog_counts(),
            "provider_operations_enabled": False,
        }

    def get_catalog(self) -> dict:
        return get_catalog()

    def get_modules(self) -> list[str]:
        return list(get_infrastructure_modules())

    def get_governance(self) -> dict:
        return get_governance_policies()
