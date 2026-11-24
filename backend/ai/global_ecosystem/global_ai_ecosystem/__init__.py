"""GLOBAL AI ECOSYSTEM — domain-level catalog and orchestration contracts.

This package does not implement HTTP routes, provider SDK calls, credentials,
or model execution. Runtime execution belongs to the existing CORE/ENGINE
composition and is supplied through explicit dependency injection.
"""
from .catalog import get_catalog, get_provider, list_providers
from .service import GlobalAIEcosystemService
from .bada_business_ai_ecosystem import BadaBusinessAIService

LAYER = "AI"
ECOSYSTEM_ID = "global-ai-ecosystem"

__all__ = [
    "LAYER", "ECOSYSTEM_ID", "GlobalAIEcosystemService",
    "BadaBusinessAIService", "get_catalog", "get_provider", "list_providers",
]
