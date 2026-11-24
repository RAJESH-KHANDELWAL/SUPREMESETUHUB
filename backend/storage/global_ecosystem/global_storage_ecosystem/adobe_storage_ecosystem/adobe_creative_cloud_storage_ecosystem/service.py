"""Adobe-specific metadata/readiness service; no remote file operations."""
from .ecosystem_service import CategoryEcosystemService
from .models import StorageObjectRecord
from .registry import StorageMetadataRegistry

ECOSYSTEM_ID = "creative_cloud"
ECOSYSTEM_NAME = "Adobe Creative Cloud Storage"
CANONICAL_ECOSYSTEM_ID = "ADOBE_CREATIVE_CLOUD_STORAGE_ECOSYSTEM"
RELATED_API_FAMILY = "See adobe_storage_capability_matrix.json"

class StorageEcosystemService(CategoryEcosystemService):
    def __init__(self, *, enabled: bool = True, registry: StorageMetadataRegistry | None = None, config: dict | None = None):
        super().__init__(config=config)
        self.enabled = bool(enabled and self.config.get("enabled", True))
        self.registry = registry or StorageMetadataRegistry()

    def describe(self) -> dict:
        return {
            **super().describe(),
            "provider_id": "adobe",
            "ecosystem_id": CANONICAL_ECOSYSTEM_ID,
            "legacy_ecosystem_id": ECOSYSTEM_ID,
            "name": ECOSYSTEM_NAME,
            "enabled": self.enabled,
            "related_api_family": RELATED_API_FAMILY,
            "capabilities": ["IDENTITY", "METADATA_MODEL", "IN_MEMORY_METADATA_REGISTRY"],
        }

    def health(self) -> dict:
        return {
            **super().health(),
            "success": self.enabled,
            "status": "FOUNDATION_READY" if self.enabled else "DISABLED",
            "connection_state": "NOT_CONFIGURED",
            "external_connections_verified": False,
            "metadata_records": self.registry.count(),
        }

    def register_metadata(self, record: StorageObjectRecord) -> dict:
        if record.provider_id != "adobe" or record.ecosystem_id not in (ECOSYSTEM_ID, CANONICAL_ECOSYSTEM_ID):
            raise ValueError("RECORD_PROVIDER_OR_ECOSYSTEM_MISMATCH")
        return self.registry.register(record)

class AdobeCreativeCloudStorage(StorageEcosystemService):
    """Canonical category-specific entry point."""
    pass
