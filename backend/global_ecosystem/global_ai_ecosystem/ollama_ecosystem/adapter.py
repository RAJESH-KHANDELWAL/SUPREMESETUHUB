"""Native adapter for the local Ollama /api/chat endpoint."""
from __future__ import annotations

import os
from typing import Any

from ..adapters.contracts import ChatRequest, ChatResponse
from ..adapters.errors import ProviderConfigurationError, ProviderRequestError
from ..adapters.http import JsonHttpClient
from .catalog import PROVIDER


class OllamaAdapter:
    provider_id = "ollama"

    def __init__(self, *, base_url: str | None = None, http_client: JsonHttpClient | None = None, **_: Any):
        self.base_url = (base_url or os.getenv("OLLAMA_ENDPOINT") or os.getenv("OLLAMA_HOST") or PROVIDER["api_endpoint"]).rstrip("/")
        self.http_client = http_client or JsonHttpClient()
        if not self.base_url:
            raise ProviderConfigurationError("Configure OLLAMA_HOST or OLLAMA_ENDPOINT before using Ollama.")

    def chat(self, request: ChatRequest) -> ChatResponse:
        result = self.http_client.post_json(
            f"{self.base_url}/api/chat",
            headers={},
            payload={
                "model": request.model,
                "messages": [{"role": item.role, "content": item.content} for item in request.messages],
                "stream": False,
                **({"options": {"temperature": request.temperature}} if request.temperature is not None else {}),
            },
            idempotency_key=request.metadata.get("idempotency_key"),
        )
        message = result.get("message")
        content = message.get("content") if isinstance(message, dict) else None
        if not isinstance(content, str):
            raise ProviderRequestError("Ollama response did not contain message content.")
        return ChatResponse(
            provider_id=self.provider_id,
            model=result.get("model") or request.model,
            content=content,
            finish_reason=result.get("done_reason"),
            usage={key: result[key] for key in ("prompt_eval_count", "eval_count") if key in result},
            raw=result,
        )
