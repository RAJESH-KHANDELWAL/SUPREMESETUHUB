"""Mistral API adapter with secret-safe readiness and live model-list verification."""
from __future__ import annotations
import os
from typing import Any, Dict
import httpx
from ..base import IntegrationProvider
from .readiness import provider_health

class MistralProvider(IntegrationProvider):
    name = "MISTRAL"
    category = "AI"
    BASE_URL = "https://api.mistral.ai/v1"

    def metadata(self) -> Dict[str, Any]:
        return {
            **super().metadata(),
            "provider_id": "mistral",
            "base_url": self.BASE_URL,
            "official_api_families": ["CHAT_COMPLETIONS", "MODELS", "EMBEDDINGS", "AGENTS", "OCR", "FINE_TUNING", "BATCH", "FIM_COMPLETIONS", "AUDIO"],
            "auth_method": "Bearer API key via server-side MISTRAL_API_KEY",
            "setup_guide": "backend/api/global_ecosystem/global_api_ecosystem/global_mistral_api_ecosystem/README.md",
            "connection": "NOT_TESTED",
            "live_connection_verified": False,
        }

    def health(self) -> Dict[str, Any]:
        configured = bool(os.getenv("MISTRAL_API_KEY", "").strip())
        return provider_health(
            provider=self.name, category=self.category, configured=configured,
            auth_method="Mistral Bearer API key",
            required_configuration=["MISTRAL_API_KEY"],
            capabilities=["CHAT_COMPLETIONS", "MODELS", "EMBEDDINGS", "AGENTS", "OCR", "FINE_TUNING", "BATCH", "FIM_COMPLETIONS", "AUDIO"],
        )

    def verify_connection(self) -> Dict[str, Any]:
        """Verify key access to GET /v1/models without returning or persisting the key."""
        api_key = os.getenv("MISTRAL_API_KEY", "").strip()
        if not api_key:
            return {"success": False, "provider": self.name, "status": "NEEDS_CONFIGURATION", "live_connection_verified": False, "missing_configuration": ["MISTRAL_API_KEY"]}
        try:
            with httpx.Client(timeout=httpx.Timeout(15.0), follow_redirects=False) as client:
                response = client.get(f"{self.BASE_URL}/models", headers={"Authorization": f"Bearer {api_key}"})
                response.raise_for_status()
                payload = response.json()
            models = payload.get("data", []) if isinstance(payload, dict) else []
            if not isinstance(models, list):
                raise ValueError("Unexpected models response")
            ids = [item["id"] for item in models if isinstance(item, dict) and isinstance(item.get("id"), str)]
            return {"success": True, "provider": self.name, "status": "CONNECTED", "connection": "VERIFIED", "live_connection_verified": True, "verification_endpoint": "/v1/models", "available_model_count": len(ids), "available_model_ids": ids[:50]}
        except httpx.HTTPStatusError as exc:
            code = exc.response.status_code
            return {"success": False, "provider": self.name, "status": "AUTHENTICATION_FAILED" if code in (401, 403) else "PROVIDER_REQUEST_FAILED", "connection": "FAILED", "live_connection_verified": False, "http_status": code}
        except (httpx.TimeoutException, httpx.RequestError):
            return {"success": False, "provider": self.name, "status": "PROVIDER_UNREACHABLE", "connection": "FAILED", "live_connection_verified": False}
        except (ValueError, TypeError):
            return {"success": False, "provider": self.name, "status": "INVALID_PROVIDER_RESPONSE", "connection": "FAILED", "live_connection_verified": False}

__all__ = ["MistralProvider"]
