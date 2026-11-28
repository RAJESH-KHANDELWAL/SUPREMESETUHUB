"""ChatGPT Education product-specific binding to the shared OpenAI Core service."""
from ..module_service import OpenAIProductCoreService


class ChatgptEducationCoreService(OpenAIProductCoreService):
    ECOSYSTEM_ID = "OPENAI-CHATGPT-EDUCATION-CORE-ECOSYSTEM"


def get_manager() -> ChatgptEducationCoreService:
    """Return the shared Core service bound to ChatGPT Education."""
    return ChatgptEducationCoreService()
