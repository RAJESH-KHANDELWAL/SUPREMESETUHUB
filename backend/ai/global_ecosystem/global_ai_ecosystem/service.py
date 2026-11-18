"""AI ecosystem catalog service and optional injected execution boundary."""
from __future__ import annotations

from typing import Any, Callable

from .catalog import catalog_counts, get_catalog, get_provider
from .registry import AIAdapterRegistry
from .schemas import AIExecutionRequest


class GlobalAIEcosystemService:
    """Expose catalog metadata and delegate execution only to injected adapters."""

    def __init__(self, registry: AIAdapterRegistry | None = None,
                 executor: Callable[..., dict[str, Any]] | None = None) -> None:
        self.registry = registry or AIAdapterRegistry()
        self._executor = executor

    def catalog(self) -> dict[str, list[dict[str, Any]]]:
        return get_catalog()

    def provider(self, provider_id: str) -> dict[str, Any]:
        return get_provider(provider_id)

    def status(self) -> dict[str, Any]:
        return {
            "ecosystem": "GLOBAL AI ECOSYSTEM",
            "status": "CATALOG_READY",
            "runtime_enabled": self._executor is not None,
            "registered_adapter_count": len(self.registry.list()),
            "catalog_counts": catalog_counts(),
        }

    def execute(self, request: AIExecutionRequest) -> dict[str, Any]:
        request.validate()
        if self._executor is None:
            raise RuntimeError("AI_RUNTIME_NOT_CONFIGURED")
        result = self._executor(
            provider_id=request.provider_id,
            capability=request.capability,
            model_id=request.model_id,
            task=request.task.strip(),
            context=request.context,
        )
        if not isinstance(result, dict):
            raise RuntimeError("AI_EXECUTOR_RETURNED_INVALID_RESULT")
        return result
