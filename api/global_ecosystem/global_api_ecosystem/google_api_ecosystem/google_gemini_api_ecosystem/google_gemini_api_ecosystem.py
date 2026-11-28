"""Google Gemini API adapter scaffold with explicit, non-persistent key handling.

This module validates a user-supplied or deployment-managed Gemini API key and
provides a small generation interface. It deliberately does not persist secrets.
Production multi-user persistence must use an encrypted per-user secret store.
"""
from __future__ import annotations

import os
from typing import Any


class GeminiConfigurationError(RuntimeError):
    """Raised when Gemini credentials or SDK configuration are missing."""


class GoogleGeminiAPIService:
    """Thin Google Gen AI SDK wrapper; never logs or returns API keys."""

    def __init__(self, model: str | None = None) -> None:
        self.model = (model or os.getenv("GOOGLE_GEMINI_MODEL", "")).strip()

    @staticmethod
    def _client(api_key: str | None = None):
        key = (api_key or os.getenv("GOOGLE_GEMINI_API_KEY", "")).strip()
        if not key:
            raise GeminiConfigurationError(
                "GEMINI_API_KEY_REQUIRED: supply a user key or configure "
                "GOOGLE_GEMINI_API_KEY in the deployment secret manager."
            )
        try:
            from google import genai
        except ImportError as exc:
            raise GeminiConfigurationError(
                "GOOGLE_GENAI_SDK_MISSING: install backend requirements."
            ) from exc
        return genai.Client(api_key=key)

    def test_connection(self, api_key: str | None = None) -> dict[str, Any]:
        """Verify API-key access by listing models; key is never retained."""
        client = self._client(api_key)
        try:
            models = list(client.models.list())
        except Exception as exc:
            # Do not include exception text: SDK errors can contain request data.
            raise GeminiConfigurationError(
                "GEMINI_CONNECTION_FAILED: verify key, project access, API status, "
                "and quota in Google AI Studio / Google Cloud."
            ) from exc
        return {
            "success": True,
            "provider": "google",
            "service": "gemini_api",
            "connection_verified": True,
            "model_count_visible": len(models),
            "credential_persisted": False,
            "credential_source": "user_supplied" if api_key else "deployment_secret",
        }

    def generate_content(
        self,
        prompt: str,
        api_key: str | None = None,
        model: str | None = None,
    ) -> dict[str, Any]:
        """Generate content after an explicit caller request."""
        if not isinstance(prompt, str) or not prompt.strip():
            raise ValueError("PROMPT_REQUIRED")
        selected_model = (model or self.model).strip()
        if not selected_model:
            raise GeminiConfigurationError(
                "GEMINI_MODEL_REQUIRED: configure GOOGLE_GEMINI_MODEL."
            )
        client = self._client(api_key)
        try:
            response = client.models.generate_content(
                model=selected_model,
                contents=prompt,
            )
        except Exception as exc:
            raise GeminiConfigurationError(
                "GEMINI_GENERATION_FAILED: verify model access, quota, and billing."
            ) from exc
        return {
            "success": True,
            "provider": "google",
            "service": "gemini_api",
            "model": selected_model,
            "text": response.text or "",
        }


__all__ = [
    "GeminiConfigurationError",
    "GoogleGeminiAPIService",
]
