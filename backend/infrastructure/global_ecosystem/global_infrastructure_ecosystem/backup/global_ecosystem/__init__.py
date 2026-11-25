"""Global ecosystem package for the backup infrastructure domain."""

from .global_backup_ecosystem import (
    ECOSYSTEM_ID,
    LAYER,
    STATUS,
    GlobalBackupEcosystemManager,
    get_manager,
)

__all__ = [
    "ECOSYSTEM_ID",
    "LAYER",
    "STATUS",
    "GlobalBackupEcosystemManager",
    "get_manager",
]
