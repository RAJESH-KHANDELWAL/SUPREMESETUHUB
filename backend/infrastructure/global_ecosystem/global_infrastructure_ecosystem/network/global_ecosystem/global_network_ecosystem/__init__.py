"""Network Global Ecosystem package."""
from .manager import NetworkEcosystemManager, get_manager
ECOSYSTEM_ID = "global-network-ecosystem"
STATUS = "STRUCTURE_SCAFFOLD_ONLY"
__all__ = ["ECOSYSTEM_ID", "STATUS", "NetworkEcosystemManager", "get_manager"]
