"""Adapter for providers exposing the OpenAI-compatible chat-completions contract."""
from __future__ import annotations

import os
from typing import Any

from .contracts import ChatRequest, ChatResponse
from .errors import ProviderConfigurationError, ProviderRequestError
from .http import JsonHttpClient


class OpenAICompatibleChatAdapter:
    def __init__(
        self, provider: dict[str, Any], *, api_key: str | None = None,
        base_url: str | None = None, http_client: JsonHttpClient | None = None,
    ) -> None:
        self.provider_id = provider["id"]
        self.provider_name = provider["name"]
        self.api_key = api_key or os.getenv(provider.get("credential_env") or "")
        self.base_url = (base_url or provider.get("api_endpoint") or "").rstrip("/")
        self.http_client = http_client or JsonHttpClient()
        if not self.base_url:
            raise ProviderConfigurationError(f"No API endpoint is configured for {self.provider_name}.")
        if not self.api_key:
            raise ProviderConfigurationError(
                f"Set {provider.get('credential_env') or 'the provider API credential'} before using {self.provider_name}."
            )

    def chat(self, request: ChatRequest) -> ChatResponse:
        payload: dict[str, Any] = {
            "model": request.model,
            "messages": [{"role": item.role, "content": item.content} for item in request.messages],
            "stream": False,
        }
        if request.temperature is not None:
            payload["temperature"] = request.temperature
        if request.max_tokens is not None:
            payload["max_tokens"] = request.max_tokens
        result = self.http_client.post_json(
            f"{self.base_url}/chat/completions",
            headers={"Authorization": f"Bearer {self.api_key}"},
            payload=payload,
            idempotency_key=request.metadata.get("idempotency_key"),
        )
        choices = result.get("choices")
        if not isinstance(choices, list) or not choices:
            raise ProviderRequestError("Provider response did not contain chat choices.")
        first = choices[0]
        message = first.get("message", {}) if isinstance(first, dict) else {}
        content = message.get("content") if isinstance(message, dict) else None
        if not isinstance(content, str):
            raise ProviderRequestError("Provider response did not contain text content.")
        usage = result.get("usage") if isinstance(result.get("usage"), dict) else {}
        return ChatResponse(
            provider_id=self.provider_id,
            model=result.get("model") or request.model,
            content=content,
            finish_reason=first.get("finish_reason") if isinstance(first, dict) else None,
            usage=usage,
            request_id=result.get("id"),
            raw=result,
        )
