"""Read-only provider-neutral catalog API for Anthropic storage taxonomy."""
from __future__ import annotations
from typing import Any
from .anthropic_storage_ecosystem import CHILD_ECOSYSTEMS, describe, load_manifest
from .ecosystem_service import EcosystemService

class AnthropicStorageCatalog:
    """Catalog metadata only; performs no Anthropic API calls or data transfers."""
    def __init__(self) -> None:
        self._service = EcosystemService()
    def health(self) -> dict[str, Any]:
        return self._service.health()
    def list(self) -> list[dict[str, str]]:
        return [{"ecosystem_id": name.upper(), "package_name": name,
                 "status": "CATALOG_ONLY", "provider_product_verified": "false"}
                for name in CHILD_ECOSYSTEMS]
    def get(self, package_name: str) -> dict[str, Any] | None:
        key = package_name.strip().casefold()
        if key not in CHILD_ECOSYSTEMS:
            return None
        return {"ecosystem_id": key.upper(), "package_name": key,
                "status": "CATALOG_ONLY", "provider_product_verified": False}
