"""Storage Global Ecosystem package."""
from .manager import StorageEcosystemManager, get_manager
ECOSYSTEM_ID = "global-storage-ecosystem"
STATUS = "STRUCTURE_SCAFFOLD_ONLY"
__all__ = ["ECOSYSTEM_ID", "STATUS", "StorageEcosystemManager", "get_manager"]
