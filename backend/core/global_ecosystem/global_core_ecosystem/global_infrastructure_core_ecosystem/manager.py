"""Metadata-only orchestration facade for the Infrastructure CORE."""
from __future__ import annotations

from .catalog import ECOSYSTEM_ID, get_catalog


class GlobalInfrastructureCoreOrchestrator:
    def catalog(self) -> dict:
        return get_catalog()

    def health(self) -> dict:
        # This reports local catalog readiness, not live provider or system health.
        return {
            "ecosystem_id": ECOSYSTEM_ID,
            "status": "CATALOG_ONLY",
            "health_check_performed": False,
            "provider_operations_enabled": False,
            "live_connections_verified": False,
        }


__all__ = ["GlobalInfrastructureCoreOrchestrator"]
