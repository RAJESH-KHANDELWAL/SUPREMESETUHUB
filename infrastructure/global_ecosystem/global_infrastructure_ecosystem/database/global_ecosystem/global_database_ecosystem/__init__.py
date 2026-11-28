"""Database Global Ecosystem package."""
from .manager import DatabaseEcosystemManager, get_manager
ECOSYSTEM_ID = "global-database-ecosystem"
STATUS = "STRUCTURE_SCAFFOLD_ONLY"
__all__ = ["ECOSYSTEM_ID", "STATUS", "DatabaseEcosystemManager", "get_manager"]
