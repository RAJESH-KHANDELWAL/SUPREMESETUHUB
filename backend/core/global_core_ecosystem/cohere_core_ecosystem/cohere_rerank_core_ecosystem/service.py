"""Public rerank capability CORE service entry point."""
from .services.core_service import CapabilityCoreService

RerankCoreService = CapabilityCoreService

__all__ = ["RerankCoreService"]
