"""Catalog service for GOOGLE_STORAGE_ECOSYSTEM; never performs provider I/O."""
import json
from pathlib import Path
from typing import Any

from .ecosystem_config import ECOSYSTEM_ID, get_config


class EcosystemService:
    ecosystem_id = ECOSYSTEM_ID
    provider = "GOOGLE"

    def __init__(self, config: dict | None = None) -> None:
        self.config = dict(config or get_config())

    def load_taxonomy(self) -> dict[str, Any]:
        path = Path(__file__).parent / "taxonomy" / "google_storage_taxonomy.json"
        with path.open("r", encoding="utf-8") as handle:
            return json.load(handle)

    def load_category_index(self) -> dict[str, Any]:
        path = Path(__file__).parent / "category_index.json"
        with path.open("r", encoding="utf-8") as handle:
            return json.load(handle)

    def describe(self) -> dict[str, Any]:
        taxonomy = self.load_taxonomy()
        index = self.load_category_index()
        category_count = sum(len(group["categories"]) for group in taxonomy["groups"])
        folder_count = len(index["folders"])
        unique_folder_count = len({item["folder"] for item in index["folders"]})
        return {
            "ecosystem_id": self.ecosystem_id,
            "provider": self.provider,
            "package_type": "STORAGE_TAXONOMY_AND_METADATA_FOUNDATION",
            "category_count": category_count,
            "indexed_folder_count": folder_count,
            "unique_folder_count": unique_folder_count,
            "taxonomy_only": True,
            "implementation_state": "TAXONOMY_AND_CATALOG_FOUNDATION",
            "connection_state": "NOT_CONFIGURED",
            "provider_product_verification_required": True,
            "storage_operations_enabled": False,
        }

    def health(self) -> dict[str, Any]:
        status = self.describe()
        consistent = (
            status["category_count"] == status["indexed_folder_count"]
            == status["unique_folder_count"]
        )
        return {
            "success": consistent,
            "status": "CATALOG_READY" if consistent else "CATALOG_INCONSISTENT",
            "external_connection_verified": False,
            "category_index_consistent": consistent,
        }
