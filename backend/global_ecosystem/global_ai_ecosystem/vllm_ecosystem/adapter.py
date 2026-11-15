"""Adapter for self-hosted vLLM OpenAI-compatible chat endpoints."""
from ..adapters.openai_compatible import OpenAICompatibleChatAdapter
from .catalog import PROVIDER


class VLLMAdapter(OpenAICompatibleChatAdapter):
    def __init__(self, **kwargs):
        super().__init__(PROVIDER, **kwargs)
