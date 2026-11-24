"""Agent domain service; delegates execution through an injected executor."""
from __future__ import annotations
from typing import Any, Callable
from .catalog import get_agent
from .contracts import AgentRequest, AgentResult
from .policies import DEFAULT_AGENT_POLICY

class GlobalAIAgentService:
    """Validate requests and delegate execution; contains no model runtime."""
    def __init__(self, executor: Callable[..., dict[str, Any]] | None = None) -> None:
        self._executor = executor

    def describe(self, agent_id: str) -> dict[str, Any]:
        return get_agent(agent_id)

    def execute(self, request: AgentRequest) -> AgentResult:
        request.validate()
        profile = get_agent(request.agent_id)
        if self._executor is None:
            raise RuntimeError("AI_AGENT_EXECUTOR_NOT_CONFIGURED")
        requested_tools = set(request.tools)
        if not requested_tools.issubset(set(profile.get("tools", []))):
            raise ValueError("AI_AGENT_TOOL_NOT_ALLOWED_FOR_PROFILE")
        if request.require_human_approval or profile.get("approval_required", False):
            return AgentResult(agent_id=request.agent_id, status="pending_approval", requires_approval=True)
        raw = self._executor(
            agent_id=request.agent_id.strip().lower(), task=request.task.strip(),
            context=request.context, tools=tuple(sorted(requested_tools)),
            memory_scope=request.memory_scope, policy=DEFAULT_AGENT_POLICY,
        )
        if not isinstance(raw, dict):
            raise RuntimeError("AI_AGENT_EXECUTOR_RETURNED_INVALID_RESULT")
        result = AgentResult(
            agent_id=request.agent_id.strip().lower(), status=raw.get("status", "completed"),
            output=raw.get("output"), steps=tuple(raw.get("steps", ())),
            artifacts=tuple(raw.get("artifacts", ())),
            requires_approval=bool(raw.get("requires_approval", False)),
            error_code=raw.get("error_code"),
        )
        result.validate()
        return result
