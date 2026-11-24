"""ChatKit product-specific binding to the shared OpenAI Core service."""
from ..module_service import OpenAIProductCoreService


class ChatkitCoreService(OpenAIProductCoreService):
    ECOSYSTEM_ID = "OPENAI-CHATKIT-CORE-ECOSYSTEM"


def get_manager() -> ChatkitCoreService:
    """Return the shared Core service bound to ChatKit."""
    return ChatkitCoreService()
