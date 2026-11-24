"""Adapter for Azure OpenAI chat-completions deployments."""
from __future__ import annotations

import os
from urllib.parse import quote
from typing import Any

from ..adapters.contracts import ChatRequest, ChatResponse
from ..adapters.errors import ProviderConfigurationError, ProviderRequestError
from ..adapters.http import JsonHttpClient


class AzureOpenAIAdapter:
    provider_id = "microsoft_azure_ai"

    def __init__(
        self, *, endpoint: str | None = None, api_key: str | None = None,
        deployment: str | None = None, api_version: str | None = None,
        http_client: JsonHttpClient | None = None,
    ):
        self.endpoint = (endpoint or os.getenv("AZURE_OPENAI_ENDPOINT") or "").rstrip("/")
        self.api_key = api_key or os.getenv("AZURE_OPENAI_API_KEY")
        self.deployment = deployment or os.getenv("AZURE_OPENAI_DEPLOYMENT")
        self.api_version = api_version or os.getenv("AZURE_OPENAI_API_VERSION", "2024-10-21")
        self.http_client = http_client or JsonHttpClient()
        if not all((self.endpoint, self.api_key, self.deployment)):
            raise ProviderConfigurationError(
                "Set AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_API_KEY and AZURE_OPENAI_DEPLOYMENT."
            )

    def chat(self, request: ChatRequest) -> ChatResponse:
        payload: dict[str, Any] = {
            "messages": [{"role": item.role, "content": item.content} for item in request.messages],
            "stream": False,
        }
        if request.temperature is not None:
            payload["temperature"] = request.temperature
        if request.max_tokens is not None:
            payload["max_tokens"] = request.max_tokens
        url = (
            f"{self.endpoint}/openai/deployments/{quote(self.deployment, safe='')}/chat/completions"
            f"?api-version={quote(self.api_version, safe='')}"
        )
        result = self.http_client.post_json(
            url, headers={"api-key": self.api_key}, payload=payload,
            idempotency_key=request.metadata.get("idempotency_key"),
        )
        choices = result.get("choices")
        if not isinstance(choices, list) or not choices:
            raise ProviderRequestError("Azure OpenAI response did not contain choices.")
        first = choices[0]
        message = first.get("message", {}) if isinstance(first, dict) else {}
        text = message.get("content") if isinstance(message, dict) else None
        if not isinstance(text, str):
            raise ProviderRequestError("Azure OpenAI response did not contain text output.")
        return ChatResponse(
            provider_id=self.provider_id, model=result.get("model") or self.deployment,
            content=text, finish_reason=first.get("finish_reason"),
            usage=result.get("usage", {}), request_id=result.get("id"), raw=result,
        )
