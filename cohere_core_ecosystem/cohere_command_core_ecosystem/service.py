"""Public command capability CORE service entry point."""
from .services.core_service import CapabilityCoreService

CommandCoreService = CapabilityCoreService

__all__ = ["CommandCoreService"]
