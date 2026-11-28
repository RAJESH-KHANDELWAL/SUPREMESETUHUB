"""Provider-neutral Global Infrastructure CORE contracts and validation."""
from .catalog import get_domain_catalog, get_provider_catalog
from .manager import GlobalInfrastructureCoreOrchestrator
from .service import GlobalInfrastructureCoreService

__all__ = [
    "GlobalInfrastructureCoreOrchestrator",
    "GlobalInfrastructureCoreService",
    "get_domain_catalog",
    "get_provider_catalog",
]
