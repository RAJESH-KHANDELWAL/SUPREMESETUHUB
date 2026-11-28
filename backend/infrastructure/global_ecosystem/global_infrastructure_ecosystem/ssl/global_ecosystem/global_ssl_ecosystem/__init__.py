"""Ssl Global Ecosystem package."""
from .manager import SslEcosystemManager, get_manager
ECOSYSTEM_ID = "global-ssl-ecosystem"
STATUS = "STRUCTURE_SCAFFOLD_ONLY"
__all__ = ["ECOSYSTEM_ID", "STATUS", "SslEcosystemManager", "get_manager"]
