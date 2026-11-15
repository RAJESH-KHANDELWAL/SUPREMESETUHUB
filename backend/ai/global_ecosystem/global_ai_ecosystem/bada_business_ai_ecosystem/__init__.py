"""BADA BUSINESS AI ECOSYSTEM — AI-domain intelligence package.

Consumes canonical Bada Business resource metadata. It does not own provider
URLs, course records, API routes, CORE business rules or ENGINE execution.
"""
from .catalog import AI_CAPABILITIES, AI_ECOSYSTEM_PROFILE, get_ai_catalog
from .service import BadaBusinessAIService

LAYER = "AI"
ECOSYSTEM_ID = "BADA_BUSINESS_AI_ECOSYSTEM"
STATUS = "AI_DOMAIN_FOUNDATION_READY"

__all__ = [
    "AI_CAPABILITIES", "AI_ECOSYSTEM_PROFILE", "BadaBusinessAIService",
    "get_ai_catalog", "LAYER", "ECOSYSTEM_ID", "STATUS",
]
