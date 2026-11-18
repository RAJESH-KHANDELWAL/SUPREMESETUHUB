"""Public embed capability CORE service entry point."""
from .services.core_service import CapabilityCoreService

EmbedCoreService = CapabilityCoreService

__all__ = ["EmbedCoreService"]
