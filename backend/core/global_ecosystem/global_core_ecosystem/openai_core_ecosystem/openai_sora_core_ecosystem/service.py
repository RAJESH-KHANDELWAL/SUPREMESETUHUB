"""Sora (retired reference) product-specific binding to the shared OpenAI Core service."""
from ..module_service import OpenAIProductCoreService


class SoraCoreService(OpenAIProductCoreService):
    ECOSYSTEM_ID = "OPENAI-SORA-CORE-ECOSYSTEM"


def get_manager() -> SoraCoreService:
    """Return the shared Core service bound to Sora (retired reference)."""
    return SoraCoreService()
