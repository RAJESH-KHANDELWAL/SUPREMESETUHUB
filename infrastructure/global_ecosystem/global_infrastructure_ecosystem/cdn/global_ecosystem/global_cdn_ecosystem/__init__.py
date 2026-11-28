"""Cdn Global Ecosystem package."""
from .manager import CdnEcosystemManager, get_manager
ECOSYSTEM_ID = "global-cdn-ecosystem"
STATUS = "STRUCTURE_SCAFFOLD_ONLY"
__all__ = ["ECOSYSTEM_ID", "STATUS", "CdnEcosystemManager", "get_manager"]
