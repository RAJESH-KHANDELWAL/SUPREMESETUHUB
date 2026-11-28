"""ChatGPT Business product-specific binding to the shared OpenAI Core service."""
from ..module_service import OpenAIProductCoreService


class ChatgptBusinessCoreService(OpenAIProductCoreService):
    ECOSYSTEM_ID = "OPENAI-CHATGPT-BUSINESS-CORE-ECOSYSTEM"


def get_manager() -> ChatgptBusinessCoreService:
    """Return the shared Core service bound to ChatGPT Business."""
    return ChatgptBusinessCoreService()
