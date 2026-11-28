"""Dns Global Ecosystem package."""
from .manager import DnsEcosystemManager, get_manager
ECOSYSTEM_ID = "global-dns-ecosystem"
STATUS = "STRUCTURE_SCAFFOLD_ONLY"
__all__ = ["ECOSYSTEM_ID", "STATUS", "DnsEcosystemManager", "get_manager"]
