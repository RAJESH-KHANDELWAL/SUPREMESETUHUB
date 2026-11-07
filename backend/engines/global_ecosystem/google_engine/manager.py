"""Google provider engine manager; keeps engine state separate from API clients."""
from __future__ import annotations

from typing import Any

from backend.core.global_ecosystem.global_core_ecosystem.google_core_ecosystem.catalog import (
    get_google_core_catalog,
)
from .models import GoogleEngineIdentity
from .registry import GoogleEngineRegistry


class GoogleEngineManager:
    NAME = "GOOGLE ENGINE MANAGER"
    VERSION = "1.0.0"

    def __init__(self) -> None:
        self.registry = GoogleEngineRegistry()
        self._register_catalog_engines()

    def _register_catalog_engines(self) -> None:
        catalog = get_google_core_catalog()
        for child in catalog["children"]:
            engine_id = child["ecosystem_id"].replace("-CORE-ECOSYSTEM", "-ENGINE")
            self.registry.register(
                GoogleEngineIdentity(
                    engine_id=engine_id,
                    name=child["name"].replace(" CORE ECOSYSTEM", " ENGINE"),
                    engine_type=child["ecosystem_type"],
                    status=child.get("status", "CATALOG_ONLY"),
                    enabled=bool(child.get("enabled", True)),
                    capabilities=list(child.get("capabilities", [])),
                    api_catalog_ref=child.get("api_catalog_ref"),
                    core_catalog_ref=catalog["ecosystem_id"],
                    metadata={"core_ecosystem_id": child["ecosystem_id"], "connected": False},
                )
            )

    def status(self) -> dict[str, Any]:
        items = self.registry.list()
        return {
            "success": True,
            "name": self.NAME,
            "version": self.VERSION,
            "engine_count": len(items),
            "connected_engines": sum(1 for item in items if item["metadata"].get("connected") is True),
            "live_connection_verified": False,
            "status": "ENGINE_CATALOG_READY",
        }

    def list(self) -> dict[str, Any]:
        items = self.registry.list()
        return {"success": True, "count": len(items), "engines": items}

    def get(self, engine_id: str) -> dict[str, Any] | None:
        return self.registry.get(engine_id)
