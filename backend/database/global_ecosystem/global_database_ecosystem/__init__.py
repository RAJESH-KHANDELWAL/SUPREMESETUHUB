"""Independent GLOBAL DATABASE ECOSYSTEM public interface."""
from .manager import GlobalDatabaseEcosystemManager
from .models import DatabaseEcosystemDescriptor, DatabaseEcosystemIdentity, DatabaseHealth
from .ecosystem_registry import DatabaseEcosystemRegistry
from .registry import GlobalDatabaseEcosystemRegistry as DatabaseProviderRegistry

__all__ = [
    "DatabaseEcosystemDescriptor",
    "DatabaseEcosystemIdentity",
    "DatabaseEcosystemManager",
    "DatabaseEcosystemRegistry",
    "DatabaseHealth",
    "DatabaseProviderRegistry",
    "GlobalDatabaseEcosystemManager",
]


DatabaseEcosystemManager = GlobalDatabaseEcosystemManager
