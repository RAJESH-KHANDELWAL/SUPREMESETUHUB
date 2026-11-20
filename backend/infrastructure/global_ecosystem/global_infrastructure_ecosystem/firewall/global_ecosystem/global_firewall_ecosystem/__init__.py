"""Firewall Global Ecosystem package."""
from .manager import FirewallEcosystemManager, get_manager
ECOSYSTEM_ID = "global-firewall-ecosystem"
STATUS = "STRUCTURE_SCAFFOLD_ONLY"
__all__ = ["ECOSYSTEM_ID", "STATUS", "FirewallEcosystemManager", "get_manager"]
