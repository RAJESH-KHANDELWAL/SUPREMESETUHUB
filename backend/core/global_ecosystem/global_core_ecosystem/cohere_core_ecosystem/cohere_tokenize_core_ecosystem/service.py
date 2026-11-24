"""Public tokenize capability CORE service entry point."""
from .services.core_service import CapabilityCoreService

TokenizeCoreService = CapabilityCoreService

__all__ = ["TokenizeCoreService"]
