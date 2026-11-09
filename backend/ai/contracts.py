"""Provider-neutral request and result contracts for AI operations."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Mapping
from uuid import uuid4

from backend.ai.capabilities import AICapability, is_supported_capability


@dataclass(frozen=True, slots=True)
class AIRequest:
    """A normalized request passed from domain/application code to an AI engine."""

    capability: AICapability
    provider: str
    payload: Mapping[str, Any] = field(default_factory=dict)
    request_id: str = field(default_factory=lambda: str(uuid4()))

    def __post_init__(self) -> None:
        provider_name = self.provider.strip().lower()
        if not provider_name:
            raise ValueError("AI_PROVIDER_REQUIRED")
        if not is_supported_capability(self.capability.value):
            raise ValueError("AI_CAPABILITY_UNSUPPORTED")
        object.__setattr__(self, "provider", provider_name)
        object.__setattr__(self, "payload", dict(self.payload))
        if not self.request_id.strip():
            raise ValueError("AI_REQUEST_ID_REQUIRED")


@dataclass(frozen=True, slots=True)
class AIResult:
    """A normalized result envelope; provider-specific data remains in data."""

    request_id: str
    capability: AICapability
    provider: str
    success: bool
    data: Any = None
    error_code: str | None = None
    metadata: Mapping[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not self.request_id.strip():
            raise ValueError("AI_REQUEST_ID_REQUIRED")
        if not self.provider.strip():
            raise ValueError("AI_PROVIDER_REQUIRED")
        if self.success and self.error_code is not None:
            raise ValueError("SUCCESS_RESULT_CANNOT_HAVE_ERROR")
        if not self.success and not self.error_code:
            raise ValueError("FAILED_RESULT_REQUIRES_ERROR_CODE")
        object.__setattr__(self, "provider", self.provider.strip().lower())
        object.__setattr__(self, "metadata", dict(self.metadata))
