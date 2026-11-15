"""Shared typed contracts for the GLOBAL AI ECOSYSTEM."""
from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any


@dataclass(frozen=True)
class CatalogRecord:
    id: str
    name: str
    category: str
    description: str
    status: str = "CATALOG_ONLY"
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class ProviderRegistration:
    provider_id: str
    capabilities: tuple[str, ...]
    models: tuple[str, ...] = ()
    status: str = "REGISTERED"


@dataclass(frozen=True)
class AIExecutionRequest:
    task: str
    provider_id: str
    capability: str = "text"
    model_id: str | None = None
    context: dict[str, Any] = field(default_factory=dict)

    def validate(self) -> None:
        if not isinstance(self.task, str) or not self.task.strip():
            raise ValueError("AI_TASK_REQUIRED")
        if len(self.task) > 12000:
            raise ValueError("AI_TASK_TOO_LONG")
        if not self.provider_id.strip() or not self.capability.strip():
            raise ValueError("AI_PROVIDER_AND_CAPABILITY_REQUIRED")
        if not isinstance(self.context, dict):
            raise ValueError("AI_CONTEXT_MUST_BE_OBJECT")
