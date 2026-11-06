"""Google Gemini Developer API adapter using the official Google Gen AI SDK."""
from __future__ import annotations

from typing import Any


class GeminiConfigurationError(RuntimeError):
    """Raised for missing or invalid Gemini API configuration."""


def build_client(api_key: str):
    """Create a Gemini client from a user-supplied API key without persisting it."""
    key = (api_key or "").strip()
    if not key:
        raise GeminiConfigurationError("A Google AI Studio API key is required")
    try:
        from google import genai
    except ImportError as exc:
        raise GeminiConfigurationError(
            "The google-genai package is required; install backend/requirements.txt"
        ) from exc
    return genai.Client(api_key=key)


class GeminiAPIService:
    """Per-request Gemini service; callers own credential storage and tenant isolation."""

    def __init__(self, api_key: str):
        self._client = build_client(api_key)

    def validate_api_key(self) -> dict[str, Any]:
        """Verify the key with a lightweight model-list request; never expose the key."""
        try:
            page = self._client.models.list(config={"page_size": 1})
            first_model = next(iter(page), None)
        except Exception as exc:
            # Do not include SDK exception text: providers may echo request details.
            raise GeminiConfigurationError(
                "Gemini API key validation failed; verify the key, API access, quota, and network."
            ) from exc
        return {
            "provider": "Google Gemini Developer API",
            "connected": True,
            "validation": "api_request_succeeded",
            "sample_model_available": bool(first_model),
        }

    def generate_content(
        self,
        *,
        model: str,
        contents: Any,
        config: Any | None = None,
    ) -> Any:
        """Generate content with the caller-selected model and SDK configuration."""
        if not model or not model.strip():
            raise ValueError("A Gemini model name is required")
        return self._client.models.generate_content(
            model=model.strip(),
            contents=contents,
            config=config,
        )
