"""Agents API product-specific binding to the shared OpenAI Core service."""
from ..module_service import OpenAIProductCoreService


class AgentsApiCoreService(OpenAIProductCoreService):
    ECOSYSTEM_ID = "OPENAI-AGENTS-API-CORE-ECOSYSTEM"


def get_manager() -> AgentsApiCoreService:
    """Return the shared Core service bound to Agents API."""
    return AgentsApiCoreService()
