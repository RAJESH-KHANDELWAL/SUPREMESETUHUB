"""Runtime provider manager for GLOBAL AI ENGINE ECOSYSTEM."""
from __future__ import annotations

from typing import Any

from .catalog import list_engines
from .openai_provider import OpenAITextEngine
from .registry import EngineRegistry
from .provider_adapter_engine import ProviderChatEngine
from backend.global_ecosystem.global_ai_ecosystem.adapters import list_chat_adapter_provider_ids


class EcosystemEngineManager:
    """Owns model-provider execution; no API or CORE transport logic."""

    def __init__(self):
        self.registry = EngineRegistry()
        self.catalog = list_engines()
        self._providers: dict[str, Any] = {}
        openai = OpenAITextEngine()
        self._providers[openai.PROVIDER_ID] = openai
        self.registry.register(openai.PROVIDER_ID, openai)
        for provider_id in list_chat_adapter_provider_ids():
            engine = ProviderChatEngine(provider_id)
            self._providers[provider_id] = engine
            self.registry.register(provider_id, engine)

    def register(self, key, value):
        return self.registry.register(key, value)

    def get(self, key):
        return self.registry.get(key)

    def provider_status(self) -> list[dict[str, Any]]:
        return [provider.status() for provider in self._providers.values()]

    def generate(
        self, *, provider_id: str, capability: str, task: str,
        context: dict[str, Any] | None = None, model_id: str | None = None,
    ) -> dict[str, Any]:
        provider = self._providers.get(provider_id.strip().lower())
        if provider is None:
            raise LookupError("AI_PROVIDER_NOT_REGISTERED")
        if capability.strip().lower() not in provider.status()["capabilities"]:
            raise ValueError("AI_CAPABILITY_NOT_SUPPORTED")
        if not provider.status()["enabled"]:
            raise RuntimeError("AI_PROVIDER_NOT_CONFIGURED")
        return provider.generate(task=task, context=context, model_id=model_id)

    def status(self):
        providers = self.provider_status()
        return {
            "layer": "ENGINE",
            "ecosystem": "GLOBAL AI",
            "catalog_count": len(self.catalog),
            "registered_count": self.registry.count(),
            "provider_count": len(providers),
            "providers": providers,
            "capabilities": sorted({cap for item in providers for cap in item["capabilities"]}),
            "status": "READY",
        }
