"""Typed contracts for AI agent requests and results.

These are domain contracts, not HTTP schemas and not execution-engine code.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any

@dataclass(frozen=True)
class AgentRequest:
    agent_id: str
    task: str
    context: dict[str, Any] = field(default_factory=dict)
    tools: tuple[str, ...] = ()
    memory_scope: str = "session"
    require_human_approval: bool = False
    metadata: dict[str, Any] = field(default_factory=dict)

    def validate(self) -> None:
        if not self.agent_id.strip():
            raise ValueError("AI_AGENT_ID_REQUIRED")
        if not self.task.strip():
            raise ValueError("AI_AGENT_TASK_REQUIRED")
        if self.memory_scope not in {"none", "session", "user", "project"}:
            raise ValueError("AI_AGENT_MEMORY_SCOPE_INVALID")
        if len(set(self.tools)) != len(self.tools):
            raise ValueError("AI_AGENT_TOOLS_MUST_BE_UNIQUE")

@dataclass(frozen=True)
class AgentResult:
    agent_id: str
    status: str
    output: Any = None
    steps: tuple[dict[str, Any], ...] = ()
    artifacts: tuple[dict[str, Any], ...] = ()
    requires_approval: bool = False
    error_code: str | None = None

    def validate(self) -> None:
        if not self.agent_id.strip():
            raise ValueError("AI_AGENT_RESULT_ID_REQUIRED")
        if self.status not in {"completed", "pending_approval", "failed", "cancelled"}:
            raise ValueError("AI_AGENT_RESULT_STATUS_INVALID")
        if self.status == "failed" and not self.error_code:
            raise ValueError("AI_AGENT_ERROR_CODE_REQUIRED")
