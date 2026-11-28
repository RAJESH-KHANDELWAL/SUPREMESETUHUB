"""Email Global Ecosystem package."""
from .manager import EmailEcosystemManager, get_manager
ECOSYSTEM_ID = "global-email-ecosystem"
STATUS = "STRUCTURE_SCAFFOLD_ONLY"
__all__ = ["ECOSYSTEM_ID", "STATUS", "EmailEcosystemManager", "get_manager"]
