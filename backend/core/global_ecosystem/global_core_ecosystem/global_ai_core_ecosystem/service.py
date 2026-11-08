"""CORE orchestration for GLOBAL AI ECOSYSTEM.

The executor is injected by the application composition root. This package
contains no API transport, provider SDK, credential handling or ENGINE imports.
"""
from __future__ import annotations

from typing import Any, Callable


class GlobalAICoreService:
    """Validate and orchestrate AI tasks through an injected execution boundary."""

    def __init__(self, executor: Callable[..., dict[str, Any]]) -> None:
        if not callable(executor):
            raise ValueError("AI_EXECUTOR_REQUIRED")
        self._executor = executor

    def generate(
        self,
        *,
        task: str,
        context: dict[str, Any] | None = None,
        provider_id: str = "openai",
        capability: str = "text",
    ) -> dict[str, Any]:
        if not isinstance(task, str) or not task.strip():
            raise ValueError("AI_TASK_REQUIRED")
        if len(task) > 12000:
            raise ValueError("AI_TASK_TOO_LONG")
        if context is not None and not isinstance(context, dict):
            raise ValueError("AI_CONTEXT_MUST_BE_OBJECT")
        if not provider_id.strip() or not capability.strip():
            raise ValueError("AI_PROVIDER_AND_CAPABILITY_REQUIRED")
        result = self._executor(
            provider_id=provider_id,
            capability=capability,
            task=task.strip(),
            context=context or {},
        )
        if not isinstance(result, dict) or not result.get("output"):
            raise RuntimeError("AI_ENGINE_RETURNED_INVALID_RESULT")
        return {
            "success": True,
            "system": "GLOBAL AI ECOSYSTEM",
            "provider": result.get("provider", provider_id),
            "model": result.get("model"),
            "output": result["output"],
            "live_verified": bool(result.get("live_verified", False)),
            "usage": result.get("usage"),
        }
