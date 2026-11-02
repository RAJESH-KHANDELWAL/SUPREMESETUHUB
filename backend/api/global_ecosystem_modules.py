"""GLOBAL ECOSYSTEM MODULES registry for API-layer discovery."""

from __future__ import annotations

from copy import deepcopy
from typing import Any


MODULES: tuple[dict[str, Any], ...] = (
    {"module_id": "AUTH", "name": "AUTH API", "path": "backend.api.auth"},
    {"module_id": "USERS", "name": "USERS API", "path": "backend.api.users"},
    {"module_id": "IDENTITY", "name": "IDENTITY API", "path": "backend.api.identity"},
    {"module_id": "PROFILES", "name": "PROFILES API", "path": "backend.api.profiles"},
    {"module_id": "BUSINESSES", "name": "BUSINESSES API", "path": "backend.api.businesses"},
    {"module_id": "PROJECTS", "name": "PROJECTS API", "path": "backend.api.projects"},
    {"module_id": "OPPORTUNITIES", "name": "OPPORTUNITIES API", "path": "backend.api.opportunities"},
    {"module_id": "MATCHING", "name": "MATCHING API", "path": "backend.api.matching"},
    {"module_id": "ROLES", "name": "ROLES API", "path": "backend.api.roles"},
    {"module_id": "SUPREME", "name": "SUPREME API", "path": "backend.api.supreme"},
    {"module_id": "DASHBOARD", "name": "DASHBOARD API", "path": "backend.api.dashboard"},
    {"module_id": "INFRASTRUCTURE", "name": "INFRASTRUCTURE API", "path": "backend.api.infrastructure"},
    {"module_id": "DNS", "name": "DNS API", "path": "backend.api.dns"},
    {"module_id": "USER_HUB", "name": "USER HUB API", "path": "backend.api.user_hub"},
    {"module_id": "AI", "name": "AI API", "path": "backend.api.ai"},
    {"module_id": "THEME_HUB", "name": "THEME HUB API", "path": "backend.api.theme_hub"},
    {"module_id": "CONNECTORS", "name": "CONNECTORS API", "path": "backend.api.connectors"},
    {"module_id": "LINKSETU", "name": "LINKSETU API", "path": "backend.api.linksetu"},
    {"module_id": "EMAIL", "name": "EMAIL API", "path": "backend.api.email"},
    {"module_id": "GALLARY_WOULT", "name": "GALLARY WOULT API", "path": "backend.api.gallary_woult"},
    {"module_id": "MUKTI_MAHAL", "name": "MUKTI MAHAL API", "path": "backend.api.mukti_mahal"},
    {"module_id": "MUKTI_MAHAL_CREATION", "name": "MUKTI MAHAL CREATION API", "path": "backend.api.mukti_mahal_creation"},
    {"module_id": "MUKTI_MAHAL_MEDIA", "name": "MUKTI MAHAL MEDIA API", "path": "backend.api.mukti_mahal_media"},
    {"module_id": "GLOBAL_ECOSYSTEM", "name": "GLOBAL ECOSYSTEM API", "path": "backend.api.global_ecosystem"},
    {"module_id": "CLOUD", "name": "CLOUD API", "path": "backend.api.cloud"},
    {"module_id": "STORAGE", "name": "STORAGE API", "path": "backend.api.storage"},
)


class GlobalEcosystemModules:
    """Discover API modules without importing or starting their routers."""

    VERSION = "1.0.0"

    def __init__(self) -> None:
        self._modules = {
            module["module_id"]: deepcopy(module)
            for module in MODULES
        }

    def status(self) -> dict[str, Any]:
        return {
            "success": True,
            "name": "GLOBAL ECOSYSTEM MODULES",
            "version": self.VERSION,
            "module_count": len(self._modules),
            "status": "REGISTRY_READY",
        }

    def list_modules(self) -> dict[str, Any]:
        modules = [
            deepcopy(module)
            for module in self._modules.values()
        ]
        return {
            "success": True,
            "count": len(modules),
            "modules": modules,
        }

    def names(self) -> dict[str, Any]:
        names = [
            module["name"]
            for module in self._modules.values()
        ]
        return {
            "success": True,
            "count": len(names),
            "names": names,
        }

    def get_module(self, module_id: str) -> dict[str, Any]:
        key = module_id.strip().upper()
        module = self._modules.get(key)

        if module is None:
            return {
                "success": False,
                "module_id": key,
                "error": "API_MODULE_NOT_FOUND",
            }

        return {
            "success": True,
            "module": deepcopy(module),
        }


EcosystemModules = GlobalEcosystemModules
