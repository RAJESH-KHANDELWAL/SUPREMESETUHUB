"""Apps SDK product-specific binding to the shared OpenAI Core service."""
from ..module_service import OpenAIProductCoreService


class AppsSdkCoreService(OpenAIProductCoreService):
    ECOSYSTEM_ID = "OPENAI-APPS-SDK-CORE-ECOSYSTEM"


def get_manager() -> AppsSdkCoreService:
    """Return the shared Core service bound to Apps SDK."""
    return AppsSdkCoreService()
