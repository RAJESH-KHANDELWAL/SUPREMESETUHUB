"""Provider discovery and lifecycle metadata orchestration for Global Domain Core."""
from __future__ import annotations
from typing import Any
from .catalog import get_domain_core_catalog, list_domain_capability_domains
from .policy import DomainCorePolicy
from .provider_catalog import domain_provider_summary, get_domain_provider, list_domain_providers

class GlobalDomainCoreOrchestrator:
    def catalog(self) -> dict[str, Any]:
        return get_domain_core_catalog()

    def list_providers(self, *, enabled_only: bool = False) -> dict[str, Any]:
        providers = list_domain_providers()
        if enabled_only:
            providers = [item for item in providers if item.get("enabled", True)]
        return {"success": True, "count": len(providers),
                "providers": [DomainCorePolicy.safe_provider_summary(item) for item in providers]}

    def get_provider(self, provider_id: str) -> dict[str, Any] | None:
        item = get_domain_provider(provider_id)
        return DomainCorePolicy.safe_provider_summary(item) if item else None

    def domains(self) -> dict[str, Any]:
        domains = list_domain_capability_domains()
        return {"success": True, "domain_count": len(domains), "domains": domains}

    def inventory(self) -> dict[str, Any]:
        return domain_provider_summary()

    def health(self) -> dict[str, Any]:
        catalog = self.catalog()
        providers = list_domain_providers()
        return {
            "success": True,
            "ecosystem_id": catalog["ecosystem_id"],
            "status": "CORE_CATALOG_AVAILABLE",
            "provider_count": len(providers),
            "domain_count": len(list_domain_capability_domains()),
            "catalog_only_count": sum(p["status"] == "CORE_CATALOG_ONLY" for p in providers),
            "live_connections_verified": 0,
            "api_calls_performed": 0,
            "warning": "Core catalog readiness is not evidence of registrar authorization, provider API availability or live connectivity.",
        }

    def dependency_map(self) -> dict[str, Any]:
        return {"success": True, "edges": [
            {"core_module": item["core_module"], "relationship": "DELEGATES_TO_DOMAIN_API_LAYER",
             "api_catalog_ref": None, "verification": "API_REFERENCE_NOT_VERIFIED"}
            for item in list_domain_providers()
        ]}
