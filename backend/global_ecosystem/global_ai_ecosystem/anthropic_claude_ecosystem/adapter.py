"""Native REST adapter for Anthropic's Messages API."""
from __future__ import annotations

import os
from typing import Any

from ..adapters.contracts import ChatRequest, ChatResponse
from ..adapters.errors import ProviderConfigurationError, ProviderRequestError
from ..adapters.http import JsonHttpClient
from .catalog import PROVIDER


class AnthropicClaudeAdapter:
    provider_id = "anthropic_claude"

    def __init__(self, *, api_key: str | None = None, base_url: str | None = None, http_client: JsonHttpClient | None = None):
        self.api_key = api_key or os.getenv(PROVIDER["credential_env"])
        self.base_url = (base_url or PROVIDER["api_endpoint"]).rstrip("/")
        self.http_client = http_client or JsonHttpClient()
        if not self.api_key:
            raise ProviderConfigurationError("Set ANTHROPIC_API_KEY before using Claude.")

    def chat(self, request: ChatRequest) -> ChatResponse:
        system = [item.content for item in request.messages if item.role in {"system", "developer"}]
        messages = [
            {"role": "assistant" if item.role == "assistant" else "user", "content": item.content}
            for item in request.messages if item.role not in {"system", "developer"}
        ]
        payload: dict[str, Any] = {
            "model": request.model,
            "max_tokens": request.max_tokens or 1024,
            "messages": messages,
        }
        if system:
            payload["system"] = "\n\n".join(system)
        if request.temperature is not None:
            payload["temperature"] = request.temperature
        result = self.http_client.post_json(
            f"{self.base_url}/v1/messages",
            headers={"x-api-key": self.api_key, "anthropic-version": "2023-06-01"},
            payload=payload,
            idempotency_key=request.metadata.get("idempotency_key"),
        )
        blocks = result.get("content")
        if not isinstance(blocks, list):
            raise ProviderRequestError("Claude response did not contain content blocks.")
        text_parts = [block.get("text", "") for block in blocks if isinstance(block, dict) and block.get("type") == "text"]
        if not text_parts:
            raise ProviderRequestError("Claude response did not contain text output.")
        return ChatResponse(
            provider_id=self.provider_id, model=result.get("model") or request.model,
            content="".join(text_parts), finish_reason=result.get("stop_reason"),
            usage=result.get("usage", {}), request_id=result.get("id"), raw=result,
        )
