"""Stable contracts shared by provider-specific adapters."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Protocol, Sequence


@dataclass(frozen=True, slots=True)
class ChatMessage:
    role: str
    content: str

    def __post_init__(self) -> None:
        if self.role not in {"system", "developer", "user", "assistant"}:
            raise ValueError(f"Unsupported chat role: {self.role}")
        if not isinstance(self.content, str):
            raise TypeError("Chat message content must be a string.")


@dataclass(frozen=True, slots=True)
class ChatRequest:
    model: str
    messages: Sequence[ChatMessage]
    temperature: float | None = None
    max_tokens: int | None = None
    metadata: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not self.model.strip():
            raise ValueError("A model identifier is required.")
        if not self.messages:
            raise ValueError("At least one chat message is required.")
        if self.temperature is not None and not 0 <= self.temperature <= 2:
            raise ValueError("temperature must be between 0 and 2.")
        if self.max_tokens is not None and self.max_tokens < 1:
            raise ValueError("max_tokens must be positive.")


@dataclass(frozen=True, slots=True)
class ChatResponse:
    provider_id: str
    model: str
    content: str
    finish_reason: str | None = None
    usage: dict[str, Any] = field(default_factory=dict)
    request_id: str | None = None
    raw: dict[str, Any] = field(default_factory=dict, repr=False)


class ProviderAdapter(Protocol):
    provider_id: str

    def chat(self, request: ChatRequest) -> ChatResponse:
        """Submit one non-streaming chat completion request."""
