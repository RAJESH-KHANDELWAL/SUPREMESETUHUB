"""Google Core Ecosystem read-only service.

Core-level status describes registry and adapter readiness only. It never
claims Google OAuth consent or a live API call has succeeded.
"""
from __future__ import annotations

from typing import Any

from .catalog import GOOGLE_CORE_ECOSYSTEM, get_google_core_catalog


class GoogleCoreEcosystemService:
    NAME = "GOOGLE CORE ECOSYSTEM"

    def status(self) -> dict[str, Any]:
        catalog = get_google_core_catalog()
        children = catalog["children"]
        return {
            "success": True,
            "ecosystem_id": catalog["ecosystem_id"],
            "name": self.NAME,
            "provider": "google",
            "status": catalog["status"],
            "registry_status": self.manager_status()["registered"],
            "module_count": len(children),
            "connected_modules": sum(1 for child in children if child.get("connected") is True),
            "live_connection_verified": False,
            "api_catalog_ref": catalog["api_catalog_ref"],
            "existing_google_core_ref": catalog["existing_google_core_ref"],
        }

    def list_modules(self) -> dict[str, Any]:
        catalog = get_google_core_catalog()
        return {"success": True, "count": len(catalog["children"]), "modules": catalog["children"]}

    def manager_status(self) -> dict[str, Any]:
        """Return status from the canonical GLOBAL CORE registry."""
        from backend.core.global_ecosystem.global_core_ecosystem.manager import (
            GlobalEcosystemManager,
        )

        manager = GlobalEcosystemManager()
        record = manager.get("GOOGLE-CORE-ECOSYSTEM")
        return {
            "success": record is not None,
            "registered": record is not None,
            "ecosystem": record,
            "live_connection_verified": False,
        }

    def list_registered_modules(self) -> dict[str, Any]:
        """Return Google core child modules that are registered in GLOBAL CORE."""
        from backend.core.global_ecosystem.global_core_ecosystem.manager import (
            GlobalEcosystemManager,
        )

        manager = GlobalEcosystemManager()
        items = [
            manager.get(module["ecosystem_id"])
            for module in get_google_core_catalog()["children"]
        ]
        registered = [item for item in items if item is not None]
        return {"success": len(registered) == len(items), "count": len(registered), "modules": registered}


    def get_module(self, ecosystem_id: str) -> dict[str, Any] | None:
        needle = ecosystem_id.strip().casefold()
        if not needle:
            return None
        for module in get_google_core_catalog()["children"]:
            if module["ecosystem_id"].casefold() == needle or module["name"].casefold() == needle:
                return module
        return None
