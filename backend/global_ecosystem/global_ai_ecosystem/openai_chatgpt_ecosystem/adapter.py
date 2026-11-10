"""Provider-specific adapter using the OpenAI-compatible chat-completions API."""
from ..adapters.openai_compatible import OpenAICompatibleChatAdapter
from .catalog import PROVIDER


class OpenAIAdapter(OpenAICompatibleChatAdapter):
    def __init__(self, **kwargs):
        super().__init__(PROVIDER, **kwargs)
