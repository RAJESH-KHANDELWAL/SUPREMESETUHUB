"""Containers Global Ecosystem package."""
from .manager import ContainersEcosystemManager, get_manager
ECOSYSTEM_ID = "global-containers-ecosystem"
STATUS = "STRUCTURE_SCAFFOLD_ONLY"
__all__ = ["ECOSYSTEM_ID", "STATUS", "ContainersEcosystemManager", "get_manager"]
