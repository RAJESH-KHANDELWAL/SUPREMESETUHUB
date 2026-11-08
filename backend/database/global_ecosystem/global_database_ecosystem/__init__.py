"""Independent GLOBAL DATABASE ecosystem package."""

from .manager import GlobalDatabaseEcosystemManager
from .models import DatabaseEcosystemDescriptor, DatabaseHealth
from .registry import GlobalDatabaseEcosystemRegistry

__all__ = [
    "DatabaseEcosystemDescriptor",
    "DatabaseHealth",
    "GlobalDatabaseEcosystemManager",
    "GlobalDatabaseEcosystemRegistry",
]
