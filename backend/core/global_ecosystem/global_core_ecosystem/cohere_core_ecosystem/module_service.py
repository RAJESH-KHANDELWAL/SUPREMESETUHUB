"""Read-only provider capability metadata service."""
from __future__ import annotations

from typing import Any

from .catalog import get_cohere_core_catalog, list_capabilities
from .domain_catalog import list_domains


class CohereModuleService:
    """Expose Cohere CORE metadata without network calls or provider execution."""

    def catalog(self) -> dict[str, Any]:
        return get_cohere_core_catalog()

    def capabilities(self) -> dict[str, dict[str, Any]]:
        return list_capabilities()

    def domains(self) -> dict[str, tuple[str, ...]]:
        return list_domains()

    def status(self) -> dict[str, Any]:
        catalog = self.catalog()
        return {
            "success": True,
            "ecosystem_id": catalog["ecosystem_id"],
            "provider": "cohere",
            "layer": "CORE",
            "status": "interface_only",
            "capability_count": len(catalog["children"]),
            "live_provider_calls_enabled": False,
            "api_calls_performed": 0,
        }
