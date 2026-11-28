"""Agents SDK product-specific binding to the shared OpenAI Core service."""
from ..module_service import OpenAIProductCoreService


class AgentsSdkCoreService(OpenAIProductCoreService):
    ECOSYSTEM_ID = "OPENAI-AGENTS-SDK-CORE-ECOSYSTEM"


def get_manager() -> AgentsSdkCoreService:
    """Return the shared Core service bound to Agents SDK."""
    return AgentsSdkCoreService()
