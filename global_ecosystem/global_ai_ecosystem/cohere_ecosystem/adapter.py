"""Native adapter for Cohere's v2 chat API."""
from __future__ import annotations

import os
from typing import Any

from ..adapters.contracts import ChatRequest, ChatResponse
from ..adapters.errors import ProviderConfigurationError, ProviderRequestError
from ..adapters.http import JsonHttpClient
from .catalog import PROVIDER


class CohereAdapter:
    provider_id = "cohere"

    def __init__(self, *, api_key: str | None = None, base_url: str | None = None, http_client: JsonHttpClient | None = None):
        self.api_key = api_key or os.getenv(PROVIDER["credential_env"])
        self.base_url = (base_url or os.getenv("COHERE_ENDPOINT") or PROVIDER["api_endpoint"]).rstrip("/")
        self.http_client = http_client or JsonHttpClient()
        if not self.api_key:
            raise ProviderConfigurationError("Set COHERE_API_KEY before using Cohere.")

    def chat(self, request: ChatRequest) -> ChatResponse:
        payload: dict[str, Any] = {
            "model": request.model,
            "messages": [{"role": item.role, "content": item.content} for item in request.messages],
        }
        if request.temperature is not None:
            payload["temperature"] = request.temperature
        if request.max_tokens is not None:
            payload["max_tokens"] = request.max_tokens
        result = self.http_client.post_json(
            f"{self.base_url}/v2/chat",
            headers={"Authorization": f"Bearer {self.api_key}"},
            payload=payload,
            idempotency_key=request.metadata.get("idempotency_key"),
        )
        message = result.get("message", {})
        blocks = message.get("content", []) if isinstance(message, dict) else []
        parts = [block.get("text", "") for block in blocks if isinstance(block, dict) and block.get("type") == "text"]
        if not parts:
            raise ProviderRequestError("Cohere response did not contain text output.")
        return ChatResponse(
            provider_id=self.provider_id, model=result.get("model") or request.model,
            content="".join(parts), finish_reason=result.get("finish_reason"),
            usage=result.get("usage", {}), request_id=result.get("id"), raw=result,
        )
