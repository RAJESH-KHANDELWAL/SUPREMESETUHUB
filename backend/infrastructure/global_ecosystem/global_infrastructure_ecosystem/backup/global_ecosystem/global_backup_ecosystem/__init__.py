"""Global Backup Ecosystem package and structural health entry point."""

from .manager import GlobalBackupEcosystemManager, get_manager

LAYER = "INFRASTRUCTURE"
ECOSYSTEM_ID = "global-backup-ecosystem"
STATUS = "STRUCTURE_SCAFFOLD_ONLY"

__all__ = [
    "LAYER",
    "ECOSYSTEM_ID",
    "STATUS",
    "GlobalBackupEcosystemManager",
    "get_manager",
]
