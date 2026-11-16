"""Discovery and metadata orchestration for Global Hosting Core."""
from __future__ import annotations
from typing import Any
from .catalog import get_hosting_core_catalog, list_hosting_capability_domains
from .policy import HostingCorePolicy
from .provider_catalog import (get_hosting_provider, hosting_provider_summary,
                               list_hosting_capability_packages, list_hosting_providers)

class GlobalHostingCoreOrchestrator:
    def catalog(self) -> dict[str, Any]:
        return get_hosting_core_catalog()

    def list_providers(self, *, category: str | None = None) -> dict[str, Any]:
        providers = list_hosting_providers(category=category)
        return {"success": True, "count": len(providers),
                "providers": [HostingCorePolicy.safe_provider_summary(item) for item in providers]}

    def get_provider(self, provider_id: str) -> dict[str, Any] | None:
        item = get_hosting_provider(provider_id)
        return HostingCorePolicy.safe_provider_summary(item) if item else None

    def capability_packages(self) -> dict[str, Any]:
        packages = list_hosting_capability_packages()
        return {"success": True, "count": len(packages), "packages": packages}

    def domains(self) -> dict[str, Any]:
        domains = list_hosting_capability_domains()
        return {"success": True, "domain_count": len(domains), "domains": domains}

    def inventory(self) -> dict[str, Any]:
        return hosting_provider_summary()

    def health(self) -> dict[str, Any]:
        catalog = self.catalog()
        summary = hosting_provider_summary()
        return {"success": True, "ecosystem_id": catalog["ecosystem_id"],
                "status": "CORE_CATALOG_AVAILABLE", **summary,
                "warning": "Catalog registration does not establish provider API availability or live connectivity."}

    def dependency_map(self) -> dict[str, Any]:
        return {"success": True, "edges": [
            {"provider_id": item["provider_id"], "core_module": item["package_name"],
             "relationship": "DELEGATES_TO_HOSTING_API_LAYER",
             "api_catalog_ref": None, "verification": "API_REFERENCE_NOT_VERIFIED"}
            for item in list_hosting_providers()
        ]}
