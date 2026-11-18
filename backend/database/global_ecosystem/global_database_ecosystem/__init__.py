"""Independent GLOBAL DATABASE ECOSYSTEM public interface."""
from .manager import GlobalDatabaseEcosystemManager
from .models import DatabaseEcosystemDescriptor, DatabaseEcosystemIdentity, DatabaseHealth
from .ecosystem_registry import DatabaseEcosystemRegistry
from .registry import GlobalDatabaseEcosystemRegistry as DatabaseProviderRegistry
from .global_vasudhaiva_kutumbakam_sanatan_dharma_bharat_world_culture_database_ecosystem import GlobalCulturalRepository

__all__ = [
    "DatabaseEcosystemDescriptor",
    "DatabaseEcosystemIdentity",
    "DatabaseEcosystemManager",
    "DatabaseEcosystemRegistry",
    "DatabaseHealth",
    "DatabaseProviderRegistry",
    "GlobalDatabaseEcosystemManager",
    "GlobalCulturalRepository",
]

DatabaseEcosystemManager = GlobalDatabaseEcosystemManager
