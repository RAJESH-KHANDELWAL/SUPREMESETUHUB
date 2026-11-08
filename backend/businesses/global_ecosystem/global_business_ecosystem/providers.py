"""Optional AI-provider boundary for future verified integrations.

No network calls or provider credentials are used in this package. Concrete
adapters must be implemented and tested separately before being registered.
"""
from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class ProviderDescriptor:
    provider_id: str
    capability: str
    enabled: bool = False
    live: bool = False
    requires_credentials: bool = True


class BusinessAIProvider(ABC):
    """Contract for an optional external AI provider."""

    @property
    @abstractmethod
    def descriptor(self) -> ProviderDescriptor:
        raise NotImplementedError

    @abstractmethod
    def analyze(self, *, task: str, business_context: dict[str, Any]) -> dict[str, Any]:
        raise NotImplementedError


class ProviderRegistry:
    """Explicit allow-list; unavailable providers are never reported as live."""

    def __init__(self) -> None:
        self._providers: dict[str, BusinessAIProvider] = {}

    def register(self, provider: BusinessAIProvider) -> None:
        descriptor = provider.descriptor
        if not descriptor.provider_id.strip():
            raise ValueError("provider_id is required")
        if descriptor.provider_id in self._providers:
            raise ValueError(f"Provider already registered: {descriptor.provider_id}")
        self._providers[descriptor.provider_id] = provider

    def capabilities(self) -> list[dict[str, Any]]:
        return [
            {
                "provider_id": item.descriptor.provider_id,
                "capability": item.descriptor.capability,
                "enabled": item.descriptor.enabled,
                "live": item.descriptor.live,
                "requires_credentials": item.descriptor.requires_credentials,
            }
            for item in self._providers.values()
        ]

    def analyze(self, provider_id: str, *, task: str, business_context: dict[str, Any]) -> dict[str, Any]:
        provider = self._providers.get(provider_id)
        if provider is None:
            raise LookupError(f"Unknown AI provider: {provider_id}")
        if not provider.descriptor.enabled:
            raise RuntimeError(f"AI provider is not enabled: {provider_id}")
        result = provider.analyze(task=task, business_context=business_context)
        if not isinstance(result, dict):
            raise TypeError("AI provider must return a dictionary")
        return result
