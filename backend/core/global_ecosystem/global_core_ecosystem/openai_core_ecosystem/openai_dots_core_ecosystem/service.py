"""Dots product-specific binding to the shared OpenAI Core service."""
from ..module_service import OpenAIProductCoreService


class DotsCoreService(OpenAIProductCoreService):
    ECOSYSTEM_ID = "OPENAI-DOTS-CORE-ECOSYSTEM"


def get_manager() -> DotsCoreService:
    """Return the shared Core service bound to Dots."""
    return DotsCoreService()
