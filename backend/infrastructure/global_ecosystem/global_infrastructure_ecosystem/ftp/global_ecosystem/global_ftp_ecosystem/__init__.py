"""Ftp Global Ecosystem package."""
from .manager import FtpEcosystemManager, get_manager
ECOSYSTEM_ID = "global-ftp-ecosystem"
STATUS = "STRUCTURE_SCAFFOLD_ONLY"
__all__ = ["ECOSYSTEM_ID", "STATUS", "FtpEcosystemManager", "get_manager"]
