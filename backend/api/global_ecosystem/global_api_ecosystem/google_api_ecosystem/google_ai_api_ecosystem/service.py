"""Unified catalog and dispatch boundary for Google AI APIs."""
from __future__ import annotations

from typing import Any


def provider_catalog() -> list[dict[str, str]]:
    """Return supported Google AI integration families and their auth models."""
    return [
        {
            "id": "gemini_developer_api",
            "name": "Google Gemini Developer API",
            "package": "google_gemini_api_ecosystem",
            "authentication": "user_supplied_google_ai_studio_api_key",
            "status": "adapter_available",
        },
        {
            "id": "vertex_ai",
            "name": "Google Cloud Vertex AI",
            "package": "google_vertex_ai_api_ecosystem",
            "authentication": "google_cloud_iam_or_oauth",
            "status": "client_factory_available_configuration_required",
        },
    ]


class GoogleAIAPIService:
    """Facade for Google AI provider adapters; does not own credential persistence."""

    def gemini(self, api_key: str):
        from ..google_gemini_api_ecosystem.service import GeminiAPIService
        return GeminiAPIService(api_key=api_key)

    def vertex_ai_client(self) -> Any:
        from ..google_vertex_ai_api_ecosystem.service import build_client
        return build_client()
