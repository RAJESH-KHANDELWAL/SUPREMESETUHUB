"""Hosting Global Ecosystem package."""
from .manager import HostingEcosystemManager, get_manager
ECOSYSTEM_ID = "global-hosting-ecosystem"
STATUS = "STRUCTURE_SCAFFOLD_ONLY"
__all__ = ["ECOSYSTEM_ID", "STATUS", "HostingEcosystemManager", "get_manager"]
