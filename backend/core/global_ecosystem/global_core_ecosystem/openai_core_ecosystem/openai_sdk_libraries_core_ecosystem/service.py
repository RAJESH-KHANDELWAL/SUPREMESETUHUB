"""OpenAI SDK Libraries product-specific binding to the shared OpenAI Core service."""
from ..module_service import OpenAIProductCoreService


class SdkLibrariesCoreService(OpenAIProductCoreService):
    ECOSYSTEM_ID = "OPENAI-SDK-LIBRARIES-CORE-ECOSYSTEM"


def get_manager() -> SdkLibrariesCoreService:
    """Return the shared Core service bound to OpenAI SDK Libraries."""
    return SdkLibrariesCoreService()
