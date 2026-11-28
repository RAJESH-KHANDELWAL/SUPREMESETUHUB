"""GLOBAL PHOTO CORE ECOSYSTEM package: read-only control-plane metadata."""
from .catalog import ECOSYSTEM_ID, ECOSYSTEM_NAME, get_catalog
from .manager import PhotoCoreManager, get_manager

LAYER = "CORE"
CATEGORY = "PHOTO"

__all__ = ["LAYER", "CATEGORY", "ECOSYSTEM_ID", "ECOSYSTEM_NAME", "get_catalog", "PhotoCoreManager", "get_manager"]
