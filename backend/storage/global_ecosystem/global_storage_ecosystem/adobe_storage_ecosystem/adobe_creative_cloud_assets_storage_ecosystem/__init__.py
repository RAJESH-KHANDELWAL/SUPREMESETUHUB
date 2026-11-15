"""adobe_creative_cloud_assets_storage_ecosystem package."""
from .models import StorageObjectRecord
from .registry import StorageMetadataRegistry
from .service import StorageEcosystemService
__all__=["StorageObjectRecord","StorageMetadataRegistry","StorageEcosystemService"]
