"""Typed, provider-neutral request and health records."""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Mapping

@dataclass(frozen=True)
class DeepSeekRequestPlan:
    operation: str
    model: str
    input_summary: Mapping[str, Any] = field(default_factory=dict)
    requires_api_key: bool = True
    live_execution: bool = False

    def to_dict(self) -> dict[str, Any]:
        return {
            "provider": "deepseek", "operation": self.operation, "model": self.model,
            "input_summary": dict(self.input_summary),
            "requires_api_key": self.requires_api_key,
            "live_execution": self.live_execution, "status": "PLAN_ONLY",
        }

@dataclass(frozen=True)
class DeepSeekHealth:
    configured: bool
    connection_verified: bool = False
    status: str = "CONNECTION_NOT_VERIFIED"

    def to_dict(self) -> dict[str, Any]:
        return {
            "provider": "deepseek", "configured": self.configured,
            "connection_verified": self.connection_verified, "status": self.status,
        }

__all__ = ["DeepSeekRequestPlan", "DeepSeekHealth"]
