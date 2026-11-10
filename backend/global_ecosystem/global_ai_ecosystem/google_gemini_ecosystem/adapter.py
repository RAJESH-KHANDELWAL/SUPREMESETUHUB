"""Native REST adapter for the Google Gemini generateContent API."""
from __future__ import annotations

import os
from urllib.parse import quote
from typing import Any

from ..adapters.contracts import ChatRequest, ChatResponse
from ..adapters.errors import ProviderConfigurationError, ProviderRequestError
from ..adapters.http import JsonHttpClient
from .catalog import PROVIDER


class GeminiAdapter:
    provider_id = "google_gemini"

    def __init__(self, *, api_key: str | None = None, base_url: str | None = None, http_client: JsonHttpClient | None = None):
        self.api_key = api_key or os.getenv(PROVIDER["credential_env"])
        self.base_url = (base_url or os.getenv("GOOGLE_GEMINI_ENDPOINT") or PROVIDER["api_endpoint"]).rstrip("/")
        self.http_client = http_client or JsonHttpClient()
        if not self.api_key:
            raise ProviderConfigurationError("Set GOOGLE_GEMINI_API_KEY before using Gemini.")

    def chat(self, request: ChatRequest) -> ChatResponse:
        system_parts = []
        contents = []
        for message in request.messages:
            if message.role in {"system", "developer"}:
                system_parts.append(message.content)
            else:
                role = "model" if message.role == "assistant" else "user"
                contents.append({"role": role, "parts": [{"text": message.content}]})
        payload: dict[str, Any] = {"contents": contents}
        if system_parts:
            payload["systemInstruction"] = {"parts": [{"text": "\n\n".join(system_parts)}]}
        generation = {}
        if request.temperature is not None:
            generation["temperature"] = request.temperature
        if request.max_tokens is not None:
            generation["maxOutputTokens"] = request.max_tokens
        if generation:
            payload["generationConfig"] = generation
        url = f"{self.base_url}/v1beta/models/{quote(request.model, safe='')}:generateContent"
        result = self.http_client.post_json(
            url, headers={"x-goog-api-key": self.api_key}, payload=payload,
            idempotency_key=request.metadata.get("idempotency_key"),
        )
        candidates = result.get("candidates")
        if not isinstance(candidates, list) or not candidates:
            raise ProviderRequestError("Gemini response did not contain candidates.")
        parts = candidates[0].get("content", {}).get("parts", [])
        text_parts = [part.get("text", "") for part in parts if isinstance(part, dict) and isinstance(part.get("text"), str)]
        if not text_parts:
            raise ProviderRequestError("Gemini response did not contain text output.")
        return ChatResponse(
            provider_id=self.provider_id, model=request.model, content="".join(text_parts),
            finish_reason=candidates[0].get("finishReason"),
            usage=result.get("usageMetadata", {}), raw=result,
        )
