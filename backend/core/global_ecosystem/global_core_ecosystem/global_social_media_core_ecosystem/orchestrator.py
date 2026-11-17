"""Discovery and readiness orchestration for Global Social Media Core."""
from __future__ import annotations
from typing import Any
from .catalog import get_social_media_core_catalog
from .domain_catalog import domain_summary
from .platform_catalog import get_platform, list_platforms

class GlobalSocialMediaCoreOrchestrator:
    def discover(self, query: str | None = None) -> dict[str, Any]:
        items = list_platforms()
        needle = (query or "").strip().lower()
        if needle:
            items = [item for item in items if needle in item["id"].lower() or needle in item["name"].lower() or needle in item["category"].lower()]
        return {"success": True, "count": len(items), "platforms": items, "readiness": "CORE_CATALOG_ONLY"}

    def health(self) -> dict[str, Any]:
        summary = domain_summary()
        return {"success": True, "status": "HEALTHY", "catalog_loaded": summary["platform_package_count"] > 0, "live_connections_verified": 0}

    def dependency_map(self) -> dict[str, Any]:
        return {
            "core": "platform identity, taxonomy, policy metadata and readiness",
            "api": "OAuth/API adapters and provider transport",
            "engine": "queues, retries, scheduling and execution",
            "database": "structured persistence",
            "storage": "media assets and files",
            "application": "sessions, consent and user workflows",
            "provider_catalog_ref": get_social_media_core_catalog()["provider_catalog_ref"],
        }

    @staticmethod
    def get_platform(platform_id: str) -> dict[str, Any]:
        return get_platform(platform_id)
