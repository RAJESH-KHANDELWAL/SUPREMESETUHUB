"""Security Global Ecosystem package."""
from .manager import SecurityEcosystemManager, get_manager
ECOSYSTEM_ID = "global-security-ecosystem"
STATUS = "STRUCTURE_SCAFFOLD_ONLY"
__all__ = ["ECOSYSTEM_ID", "STATUS", "SecurityEcosystemManager", "get_manager"]
