"""CLOUD provider adapter protocol and explicit adapter registry."""
from __future__ import annotations
from typing import Any, Protocol
from .models import CloudOperationRequest, CloudOperationResult

class CloudProviderAdapter(Protocol):
    provider_id: str
    def describe(self) -> dict[str, Any]: ...
    def execute(self, request: CloudOperationRequest) -> CloudOperationResult: ...

class CloudAdapterRegistry:
    def __init__(self) -> None:
        self._adapters: dict[str, CloudProviderAdapter] = {}

    def register(self, adapter: CloudProviderAdapter) -> None:
        provider_id = adapter.provider_id.strip().lower()
        if not provider_id:
            raise ValueError("CLOUD_ADAPTER_PROVIDER_ID_REQUIRED")
        if provider_id in self._adapters:
            raise ValueError(f"CLOUD_ADAPTER_ALREADY_REGISTERED:{provider_id}")
        self._adapters[provider_id] = adapter

    def get(self, provider_id: str) -> CloudProviderAdapter:
        normalized = provider_id.strip().lower()
        try:
            return self._adapters[normalized]
        except KeyError as exc:
            raise KeyError(f"CLOUD_ADAPTER_NOT_REGISTERED:{normalized}") from exc

    def list_ids(self) -> tuple[str, ...]:
        return tuple(sorted(self._adapters))
