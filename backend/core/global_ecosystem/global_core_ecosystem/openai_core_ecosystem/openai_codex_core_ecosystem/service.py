"""Codex product-specific binding to the shared OpenAI Core service."""
from ..module_service import OpenAIProductCoreService


class CodexCoreService(OpenAIProductCoreService):
    ECOSYSTEM_ID = "OPENAI-CODEX-CORE-ECOSYSTEM"


def get_manager() -> CodexCoreService:
    """Return the shared Core service bound to Codex."""
    return CodexCoreService()
