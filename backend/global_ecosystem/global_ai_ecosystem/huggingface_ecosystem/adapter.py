"""Adapter for Hugging Face Inference Providers OpenAI-compatible chat routing."""
from __future__ import annotations

import os

from ..adapters.openai_compatible import OpenAICompatibleChatAdapter
from .catalog import PROVIDER


class HuggingFaceAdapter(OpenAICompatibleChatAdapter):
    def __init__(self, *, api_key: str | None = None, base_url: str | None = None, **kwargs):
        endpoint = base_url or os.getenv("HF_INFERENCE_ENDPOINT") or f"{PROVIDER['api_endpoint'].rstrip('/')}/v1"
        super().__init__(PROVIDER, api_key=api_key, base_url=endpoint, **kwargs)
