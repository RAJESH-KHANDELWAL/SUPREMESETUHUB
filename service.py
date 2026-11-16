"""Read-only facade for the Global Infrastructure Ecosystem."""
from __future__ import annotations

from .catalog import catalog_counts, get_catalog, get_infrastructure_modules
from .governance import get_governance_policies
from .registry import InfrastructureCatalogRegistry
from .structure import (
    INFRASTRUCTURE_MODULES,
    INFRASTRUCTURE_ROOT_MODULES,
    INTEGRATION_PATHS,
    get_canonical_ownership,
    get_ecosystem_domain_paths,
    get_module_paths,
    get_root_module_paths,
)


class GlobalInfrastructureEcosystemService:
    """Expose domain adapters, ownership and integration metadata; no provider mutations."""

    def __init__(self, registry: InfrastructureCatalogRegistry | None = None) -> None:
        self.registry = registry or InfrastructureCatalogRegistry()

    def get_overview(self) -> dict:
        return {
            "ecosystem_id": "global-infrastructure-ecosystem",
            "layer": "INFRASTRUCTURE",
            "status": "DOMAIN_ADAPTERS_REGISTERED",
            "domain_count": len(INFRASTRUCTURE_MODULES),
            "root_module_count": len(INFRASTRUCTURE_ROOT_MODULES),
            "catalog_counts": catalog_counts(),
            "integrated_foundation_layers": ["CORE", "GLOBAL_CORE_ECOSYSTEM", "GLOBAL_ECOSYSTEM"],
            "provider_operations_enabled": False,
            "canonical_implementations_preserved": True,
        }

    def get_catalog(self) -> dict:
        return get_catalog()

    def get_modules(self) -> list[str]:
        return list(get_infrastructure_modules())

    def get_module_paths(self) -> dict:
        return {
            "canonical_domain_sources": get_module_paths(),
            "ecosystem_domain_adapters": get_ecosystem_domain_paths(),
            "infrastructure_root_modules": get_root_module_paths(),
        }

    def get_integrations(self) -> dict[str, str]:
        return dict(INTEGRATION_PATHS)

    def get_ownership_map(self) -> dict:
        return get_canonical_ownership()

    def get_governance(self) -> dict:
        return get_governance_policies()
