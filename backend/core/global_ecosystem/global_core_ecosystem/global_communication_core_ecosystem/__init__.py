"""Global Communication Core Ecosystem metadata package."""
LAYER = "CORE"
CATEGORY = "COMMUNICATION"
ECOSYSTEM_NAME = "GLOBAL COMMUNICATION CORE ECOSYSTEM"
ECOSYSTEM_ID = "GLOBAL-COMMUNICATION-CORE-ECOSYSTEM"
from .manager import CommunicationCoreManager, get_manager
__all__ = ["LAYER", "CATEGORY", "ECOSYSTEM_NAME", "ECOSYSTEM_ID", "CommunicationCoreManager", "get_manager"]
