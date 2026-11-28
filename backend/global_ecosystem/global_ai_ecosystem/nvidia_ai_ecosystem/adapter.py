"""Adapter for NVIDIA NIM endpoints exposing OpenAI-compatible chat completions."""
from ..adapters.openai_compatible import OpenAICompatibleChatAdapter
from .catalog import PROVIDER


class NVIDIAAdapter(OpenAICompatibleChatAdapter):
    def __init__(self, **kwargs):
        super().__init__(PROVIDER, **kwargs)
