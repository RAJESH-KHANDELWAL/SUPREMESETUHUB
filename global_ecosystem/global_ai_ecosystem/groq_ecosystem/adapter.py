"""Provider-specific adapter for the OpenAI-compatible chat API surface."""
from ..adapters.openai_compatible import OpenAICompatibleChatAdapter
from .catalog import PROVIDER


class GroqAdapter(OpenAICompatibleChatAdapter):
    def __init__(self, **kwargs):
        super().__init__(PROVIDER, **kwargs)
