"""Ipam Global Ecosystem package."""
from .manager import IpamEcosystemManager, get_manager
ECOSYSTEM_ID = "global-ipam-ecosystem"
STATUS = "STRUCTURE_SCAFFOLD_ONLY"
__all__ = ["ECOSYSTEM_ID", "STATUS", "IpamEcosystemManager", "get_manager"]
