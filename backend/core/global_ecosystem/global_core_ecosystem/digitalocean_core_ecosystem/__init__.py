"""Public interface for the DigitalOcean Core Ecosystem control plane."""

from .catalog import get_catalog, list_capabilities
from .contracts import CoreResult, Readiness, SecretReference, TenantContext
from .manager import DigitalOceanCoreManager, get_manager
from .orchestrator import DigitalOceanCoreOrchestrator
from .service import DigitalOceanCoreService

__all__ = [
    "get_catalog",
    "list_capabilities",
    "CoreResult",
    "Readiness",
    "SecretReference",
    "TenantContext",
    "DigitalOceanCoreManager",
    "get_manager",
    "DigitalOceanCoreOrchestrator",
    "DigitalOceanCoreService",
]
