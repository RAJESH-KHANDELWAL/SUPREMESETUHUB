"""Read-only catalog and workload facade for Global Cloud Core."""
from __future__ import annotations

from collections import Counter
from typing import Any

from backend.global_ecosystem.global_cloud_ecosystem import (
    CLOUD_CAPABILITIES,
    CLOUD_SCOPES,
    get_cloud_provider,
    get_cloud_workload,
    list_cloud_providers,
    list_cloud_workloads,
    validate_cloud_catalog,
    validate_cloud_workloads,
)

from .policy import (
    readiness_for_provider,
    safe_provider_snapshot,
    safe_workload_snapshot,
)


class GlobalCloudCoreService:
    """Read-only cloud control-plane metadata facade; no provider execution."""

    layer = "CORE"
    ecosystem = "GLOBAL_CLOUD_ECOSYSTEM"

    def resolve_provider(self, provider_id: str) -> dict[str, Any]:
        if not isinstance(provider_id, str) or not provider_id.strip():
            raise ValueError("CLOUD_PROVIDER_ID_REQUIRED")
        provider = get_cloud_provider(provider_id.strip().lower())
        if provider is None:
            raise KeyError(f"Unknown cloud provider: {provider_id}")
        return provider

    def provider_snapshot(self, provider_id: str) -> dict[str, Any]:
        provider = self.resolve_provider(provider_id)
        return {
            "provider": safe_provider_snapshot(provider),
            "readiness": readiness_for_provider(provider),
            "execution": "NOT_PERFORMED",
            "persistence": "NOT_PERFORMED",
        }

    def catalog_snapshot(self) -> dict[str, Any]:
        providers = list_cloud_providers()
        statuses = Counter(
            item.get("integration_status", "unknown") for item in providers
        )
        live_verified = sum(
            1 for item in providers
            if item.get("integration_status") == "live_verified"
            and item.get("live_connection_verified") is True
        )
        return {
            "layer": self.layer,
            "ecosystem": self.ecosystem,
            "provider_count": len(providers),
            "provider_origins": dict(sorted(Counter(
                item.get("origin", "unknown") for item in providers
            ).items())),
            "integration_status_counts": dict(sorted(statuses.items())),
            "live_verified_provider_count": live_verified,
            "capability_group_count": len(CLOUD_CAPABILITIES),
            "capability_count": sum(len(items) for items in CLOUD_CAPABILITIES.values()),
            "scope_count": len(CLOUD_SCOPES),
            "workload_count": len(list_cloud_workloads()),
            "execution": "NOT_PERFORMED",
            "persistence": "NOT_PERFORMED",
        }

    def list_workloads(
        self,
        *,
        tier: str | None = None,
        region: str | None = None,
        adult_industry: bool | None = None,
    ) -> tuple[dict[str, Any], ...]:
        return tuple(
            safe_workload_snapshot(item)
            for item in list_cloud_workloads(
                tier=tier, region=region, adult_industry=adult_industry
            )
        )

    def workload_snapshot(self, workload_id: str) -> dict[str, Any]:
        if not isinstance(workload_id, str) or not workload_id.strip():
            raise ValueError("CLOUD_WORKLOAD_ID_REQUIRED")
        workload = get_cloud_workload(workload_id.strip().lower())
        if workload is None:
            raise KeyError(f"Unknown cloud workload: {workload_id}")
        return {
            "workload": safe_workload_snapshot(workload),
            "execution": "NOT_PERFORMED",
            "persistence": "NOT_PERFORMED",
        }

    def health_snapshot(self) -> dict[str, Any]:
        catalog_errors = validate_cloud_catalog()
        workload_errors = validate_cloud_workloads()
        snapshot = self.catalog_snapshot()
        return {
            "success": not catalog_errors and not workload_errors,
            "ecosystem": self.ecosystem,
            "catalog_valid": not catalog_errors,
            "catalog_errors": list(catalog_errors),
            "workloads_valid": not workload_errors,
            "workload_errors": list(workload_errors),
            "provider_count": snapshot["provider_count"],
            "live_verified_provider_count": snapshot["live_verified_provider_count"],
            "execution": "NOT_PERFORMED",
            "persistence": "NOT_PERFORMED",
        }


__all__ = ["GlobalCloudCoreService"]
