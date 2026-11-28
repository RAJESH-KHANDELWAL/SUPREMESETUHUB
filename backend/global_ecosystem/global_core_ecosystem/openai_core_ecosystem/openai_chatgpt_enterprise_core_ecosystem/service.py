"""ChatGPT Enterprise product-specific binding to the shared OpenAI Core service."""
from ..module_service import OpenAIProductCoreService


class ChatgptEnterpriseCoreService(OpenAIProductCoreService):
    ECOSYSTEM_ID = "OPENAI-CHATGPT-ENTERPRISE-CORE-ECOSYSTEM"


def get_manager() -> ChatgptEnterpriseCoreService:
    """Return the shared Core service bound to ChatGPT Enterprise."""
    return ChatgptEnterpriseCoreService()
