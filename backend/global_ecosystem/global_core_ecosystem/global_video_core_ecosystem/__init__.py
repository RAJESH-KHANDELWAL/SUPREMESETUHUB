"""Global Video Core Ecosystem package."""
from .catalog import ECOSYSTEM_ID, ECOSYSTEM_NAME, get_catalog
from .manager import VideoCoreManager, get_manager

LAYER = "CORE"
CATEGORY = "VIDEO"

__all__ = ["LAYER", "CATEGORY", "ECOSYSTEM_ID", "ECOSYSTEM_NAME", "get_catalog", "VideoCoreManager", "get_manager"]
