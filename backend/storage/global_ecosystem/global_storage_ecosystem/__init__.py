"""Independent GLOBAL STORAGE ECOSYSTEM public interface."""
from .manager import GlobalStorageEcosystemManager, StorageEcosystemManager
from .models import StorageEcosystemIdentity, StorageHealth, StorageObject
from .ecosystem_registry import StorageEcosystemRegistry
from .provider_contract import StorageProviderAdapter
from .registry import list_providers, get_provider

__all__ = ["GlobalStorageEcosystemManager", "StorageEcosystemManager",
           "StorageEcosystemIdentity", "StorageHealth", "StorageObject",
           "StorageEcosystemRegistry", "StorageProviderAdapter",
           "list_providers", "get_provider"]
