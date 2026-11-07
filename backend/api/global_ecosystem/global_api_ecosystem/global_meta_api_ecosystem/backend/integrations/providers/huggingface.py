"""Hugging Face Hub and Inference API client."""
from __future__ import annotations

import os
from typing import Any

import httpx

from ..base import IntegrationProvider


class HuggingFaceProvider(IntegrationProvider):
    """Authenticated Hugging Face API client using a server-side access token."""

    name = "HUGGINGFACE"
    category = "AI_PLATFORM"
    BASE_URL = "https://huggingface.co/api"

    def token(self) -> str:
        return os.getenv("HF_TOKEN", "").strip() or os.getenv("HUGGINGFACEHUB_API_TOKEN", "").strip()

    def metadata(self) -> dict[str, Any]:
        return {
            **super().metadata(),
            "capabilities": ["WHOAMI", "MODEL_SEARCH", "MODEL_DETAILS", "DATASET_SEARCH", "DATASET_DETAILS", "SPACE_SEARCH"],
            "auth_method": "Hugging Face user access token stored server-side",
            "setup_guide": "Set HF_TOKEN in deployment secrets. Never commit or expose the token.",
        }

    def health(self) -> dict[str, Any]:
        configured = bool(self.token())
        return {
            "provider": self.name,
            "category": self.category,
            "status": "CONFIGURED" if configured else "NEEDS_CONFIGURATION",
            "authentication": "TOKEN_CONFIGURED" if configured else "TOKEN_MISSING",
            "connection": "NOT_VERIFIED",
            "required_configuration": ["HF_TOKEN"],
            "live_connection_verified": False,
        }

    def request(self, method: str, path: str, *, params: dict[str, Any] | None = None) -> Any:
        token = self.token()
        if not token:
            raise RuntimeError("HF_TOKEN_NOT_CONFIGURED")
        url = self.BASE_URL + "/" + path.lstrip("/")
        headers = {"Authorization": f"Bearer {token}", "Accept": "application/json"}
        with httpx.Client(timeout=25.0, follow_redirects=True) as client:
            response = client.request(method, url, headers=headers, params=params)
            response.raise_for_status()
            if not response.content:
                return {}
            return response.json()
