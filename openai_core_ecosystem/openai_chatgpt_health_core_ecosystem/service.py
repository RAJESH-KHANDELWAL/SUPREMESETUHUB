"""ChatGPT Health product-specific binding to the shared OpenAI Core service."""
from ..module_service import OpenAIProductCoreService


class ChatgptHealthCoreService(OpenAIProductCoreService):
    ECOSYSTEM_ID = "OPENAI-CHATGPT-HEALTH-CORE-ECOSYSTEM"


def get_manager() -> ChatgptHealthCoreService:
    """Return the shared Core service bound to ChatGPT Health."""
    return ChatgptHealthCoreService()
