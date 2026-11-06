
from __future__ import annotations

import os
import logging
from typing import Any, Callable

import httpx

from backend.engines.base import BaseEngine


logger = logging.getLogger(__name__)


class AIEngine(BaseEngine):
    """
    Central AI Engine for SUPREMESETUHUB.

    Supports multiple providers and capabilities through
    a single registry and dispatch interface.
    """

    CAPABILITIES = {
        "text",
        "image",
        "video",
        "audio",
        "speech",
        "code",
        "game",
        "movie",
        "design",
        "3d",
        "document",
        "research",
        "automation",
    }

    def __init__(self):
        super().__init__("SUPREME AI ENGINE")

        self._providers: dict[str, dict[str, Any]] = {}

        # Existing image and video provider services
        from backend.creation.providers.photo_provider import PhotoProvider
        from backend.creation.video_service import VideoCreationService

        self.photo_provider = PhotoProvider()
        self.video_provider = VideoCreationService()

        # Register OpenAI Image Provider
        self.register_provider(
            name="openai_image",
            capabilities=["image"],
            models=["gpt-image-1"],
            handler=lambda capability, **payload: (
                self.photo_provider.generate(**payload)
            ),
        )

        # Register Google Veo Video Provider
        self.register_provider(
            name="google_veo",
            capabilities=["video"],
            models=[self.video_provider.model],
            handler=lambda capability, **payload: (
                self.video_provider.create_video(**payload)
            ),
        )

        # Register NSFWInfra Image Provider
        self.register_provider(
            name="nsfwinfra",
            capabilities=["image"],
            models=["nsfwinfra-image"],
            handler=self._generate_nsfwinfra_image,
        )

    def _generate_nsfwinfra_image(
        self,
        capability: str,
        **payload: Any,
    ) -> dict[str, Any]:
        """Generate an image through the NSFWInfra API."""

        api_key = os.getenv("NSFWINFRA_API_KEY")

        if not api_key:
            raise RuntimeError(
                "NSFWINFRA_API_KEY is not configured"
            )

        prompt = str(payload.get("prompt", "")).strip()

        if not prompt:
            raise ValueError("PROMPT_REQUIRED")

        # Send only the prompt supported by the supplied API example.
        response = httpx.post(
            "https://api.nsfwinfra.com/v1/images/generate",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
            json={"prompt": prompt},
            timeout=60.0,
        )

        if not response.is_success:
            logger.error(
                "NSFWInfra request failed with HTTP status %s",
                response.status_code,
            )
            raise RuntimeError(
                f"NSFWINFRA_HTTP_ERROR_{response.status_code}"
            )

        try:
            return response.json()
        except ValueError as exc:
            logger.error("NSFWInfra returned a non-JSON response")
            raise RuntimeError(
                "NSFWINFRA_INVALID_JSON_RESPONSE"
            ) from exc

    def register_provider(
        self,
        name: str,
        capabilities: list[str],
        handler: Callable[..., Any],
        models: list[str] | None = None,
    ) -> dict[str, Any]:
        """Register or update a provider in the existing registry."""

        provider_name = name.strip().lower()

        if not provider_name:
            raise ValueError("PROVIDER_NAME_REQUIRED")

        if not callable(handler):
            raise ValueError("PROVIDER_HANDLER_MUST_BE_CALLABLE")

        supported = set(capabilities)

        if not supported:
            raise ValueError("PROVIDER_CAPABILITIES_REQUIRED")

        unsupported = supported - self.CAPABILITIES

        if unsupported:
            raise ValueError(
                f"UNSUPPORTED_CAPABILITIES: {sorted(unsupported)}"
            )

        self._providers[provider_name] = {
            "name": provider_name,
            "capabilities": sorted(supported),
            "models": models or [],
            "handler": handler,
            "status": "REGISTERED",
        }

        return self.provider_info(provider_name)

    def unregister_provider(self, name: str) -> dict[str, Any]:
        """Remove a provider from the registry."""

        provider_name = name.strip().lower()

        if provider_name not in self._providers:
            raise ValueError("PROVIDER_NOT_FOUND")

        del self._providers[provider_name]

        return {
            "success": True,
            "provider": provider_name,
            "status": "UNREGISTERED",
        }

    def provider_info(self, name: str) -> dict[str, Any]:
        """Return safe provider information without exposing secrets."""

        provider_name = name.strip().lower()
        provider = self._providers.get(provider_name)

        if provider is None:
            raise ValueError("PROVIDER_NOT_FOUND")

        return {
            "name": provider["name"],
            "capabilities": provider["capabilities"],
            "models": provider["models"],
            "status": provider["status"],
        }

    def list_providers(self) -> list[dict[str, Any]]:
        """List all registered providers."""

        return [
            self.provider_info(name)
            for name in sorted(self._providers)
        ]

    def providers_for(self, capability: str) -> list[dict[str, Any]]:
        """Find providers supporting a capability."""

        capability_name = capability.strip().lower()

        if capability_name not in self.CAPABILITIES:
            raise ValueError("UNSUPPORTED_CAPABILITY")

        return [
            self.provider_info(name)
            for name, provider in sorted(self._providers.items())
            if capability_name in provider["capabilities"]
        ]

    def generate(
        self,
        capability: str,
        provider: str,
        **payload: Any,
    ) -> Any:
        """Dispatch a request to a registered provider."""

        capability_name = capability.strip().lower()
        provider_name = provider.strip().lower()

        if capability_name not in self.CAPABILITIES:
            raise ValueError("UNSUPPORTED_CAPABILITY")

        selected = self._providers.get(provider_name)

        if selected is None:
            raise ValueError("PROVIDER_NOT_FOUND")

        if capability_name not in selected["capabilities"]:
            raise ValueError(
                "CAPABILITY_NOT_SUPPORTED_BY_PROVIDER"
            )

        return selected["handler"](
            capability=capability_name,
            **payload,
        )

    def status(self) -> dict[str, Any]:
        """Return central AI engine status."""

        return {
            **super().status(),
            "architecture": "MULTI_PROVIDER",
            "provider_count": len(self._providers),
            "capabilities": sorted(self.CAPABILITIES),
            "providers": self.list_providers(),
        }
