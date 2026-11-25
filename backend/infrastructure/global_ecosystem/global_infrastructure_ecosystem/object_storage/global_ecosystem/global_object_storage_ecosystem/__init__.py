"""Object Storage Global Ecosystem package."""
from .manager import ObjectStorageEcosystemManager, get_manager
ECOSYSTEM_ID = "global-object-storage-ecosystem"
STATUS = "STRUCTURE_SCAFFOLD_ONLY"
__all__ = ["ECOSYSTEM_ID", "STATUS", "ObjectStorageEcosystemManager", "get_manager"]
