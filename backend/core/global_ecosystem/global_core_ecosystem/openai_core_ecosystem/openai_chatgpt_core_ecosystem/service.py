"""ChatGPT product-specific binding to the shared OpenAI Core service."""
from ..module_service import OpenAIProductCoreService


class ChatgptCoreService(OpenAIProductCoreService):
    ECOSYSTEM_ID = "OPENAI-CHATGPT-CORE-ECOSYSTEM"


def get_manager() -> ChatgptCoreService:
    """Return the shared Core service bound to ChatGPT."""
    return ChatgptCoreService()
