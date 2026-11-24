"""Read-only adapter over the canonical Global Cloud provider and workload catalogs."""
from __future__ import annotations
from typing import Any
from backend.global_ecosystem.global_cloud_ecosystem import (
    CLOUD_CAPABILITIES, CLOUD_SCOPES, get_cloud_provider, get_cloud_workload,
    list_cloud_providers, list_cloud_workloads, validate_cloud_catalog,
    validate_cloud_workloads,
)

class GlobalCloudCoreService:
    NAME = "GLOBAL CLOUD CORE ECOSYSTEM"

    def status(self) -> dict[str, Any]:
        providers = list_cloud_providers()
        workloads = list_cloud_workloads()
        provider_errors = validate_cloud_catalog()
        workload_errors = validate_cloud_workloads()
        errors = [*provider_errors, *workload_errors]
        return {
            "success": not errors, "ecosystem_id": "GLOBAL-CLOUD-CORE-ECOSYSTEM",
            "name": self.NAME, "layer": "CORE",
            "provider_count": len(providers), "workload_count": len(workloads),
            "scope_count": len(CLOUD_SCOPES), "capability_group_count": len(CLOUD_CAPABILITIES),
            "provider_catalog_valid": not provider_errors,
            "workload_catalog_valid": not workload_errors,
            "validation_errors": errors,
            "live_connections_verified": 0, "api_calls_performed": 0,
            "provisioning_performed": False, "persistence_performed": False,
        }

    def health(self) -> dict[str, Any]:
        result = self.status()
        return {**result, "status": "CORE_CATALOG_AVAILABLE" if result["success"] else "CATALOG_VALIDATION_FAILED"}

    def list_products(self, *, origin: str | None = None) -> dict[str, Any]:
        providers = list_cloud_providers(origin=origin)
        return {"success": True, "count": len(providers), "products": list(providers)}

    def get_product(self, provider_id: str) -> dict[str, Any] | None:
        return get_cloud_provider(provider_id)

    def list_offerings(self, *, tier: str | None = None, region: str | None = None,
                       adult_industry: bool | None = None) -> dict[str, Any]:
        items = list_cloud_workloads(tier=tier, region=region, adult_industry=adult_industry)
        return {"success": True, "count": len(items), "offerings": list(items)}

    def get_offering(self, workload_id: str) -> dict[str, Any] | None:
        return get_cloud_workload(workload_id)

    def list_scopes(self) -> dict[str, Any]:
        return {"success": True, "count": len(CLOUD_SCOPES),
                "scopes": [{"id": key, "capabilities": list(value)} for key, value in CLOUD_SCOPES.items()]}

    def list_capabilities(self) -> dict[str, Any]:
        return {"success": True, "count": len(CLOUD_CAPABILITIES),
                "capabilities": {key: list(value) for key, value in CLOUD_CAPABILITIES.items()}}

    def dependency_map(self) -> dict[str, Any]:
        return {
            "success": True, "core": "GLOBAL-CLOUD-CORE-ECOSYSTEM",
            "dependencies": {
                "provider_metadata": "backend/global_ecosystem/global_cloud_ecosystem/catalog.py",
                "capability_taxonomy": "backend/global_ecosystem/global_cloud_ecosystem/capabilities.py",
                "regional_scope": "backend/global_ecosystem/global_cloud_ecosystem/scope.py",
                "workload_taxonomy": "backend/global_ecosystem/global_cloud_ecosystem/workloads.py",
                "api_transport_and_credentials": "CLOUD API ECOSYSTEM",
                "provisioning_and_execution": "CLOUD ENGINE ECOSYSTEM",
                "durable_data": "CLOUD DATABASE / STORAGE ECOSYSTEMS",
                "master_catalog": "backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json",
            },
            "core_execution": "NOT_PERFORMED", "core_persistence": "NOT_PERFORMED",
        }

__all__ = ["GlobalCloudCoreService"]
