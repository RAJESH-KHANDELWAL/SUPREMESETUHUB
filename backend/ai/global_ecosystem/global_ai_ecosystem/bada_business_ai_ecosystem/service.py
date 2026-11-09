"""Bada Business AI domain service with injected execution boundary."""
from __future__ import annotations
from typing import Any, Callable
from .agents import get_bada_business_agent
from .catalog import get_ai_catalog
from .policies import BADA_BUSINESS_AI_POLICY
from .resource_adapter import load_provider_resources, resource_summary


class BadaBusinessAIService:
    """Expose AI metadata and delegate tasks only to an injected executor."""

    def __init__(self, executor: Callable[..., dict[str, Any]] | None = None) -> None:
        self._executor = executor

    def catalog(self) -> dict[str, Any]:
        return get_ai_catalog()

    def resources(self) -> dict[str, Any]:
        return resource_summary(load_provider_resources())

    def agent(self, agent_id: str) -> dict[str, Any]:
        return get_bada_business_agent(agent_id)

    def status(self) -> dict[str, Any]:
        return {
            "ecosystem": "BADA BUSINESS AI ECOSYSTEM",
            "layer": "AI",
            "status": "AI_DOMAIN_FOUNDATION_READY",
            "runtime_status": "CONFIGURED_NOT_VERIFIED" if self._executor is not None else "NOT_CONFIGURED",
        }

    def execute(self, agent_id: str, task: str, context: dict[str, Any] | None = None) -> dict[str, Any]:
        if not agent_id.strip() or not task.strip():
            raise ValueError("BADA_BUSINESS_AI_AGENT_AND_TASK_REQUIRED")
        agent = get_bada_business_agent(agent_id)

        # Approval-required agents must stop before the execution boundary.
        if agent.get("approval_required", False):
            return {
                "ecosystem": "BADA_BUSINESS_AI_ECOSYSTEM",
                "agent_id": agent["id"],
                "status": "pending_approval",
                "requires_approval": True,
                "message": "Explicit human approval is required before this agent can execute.",
            }

        if self._executor is None:
            raise RuntimeError("BADA_BUSINESS_AI_EXECUTOR_NOT_CONFIGURED")

        resources = load_provider_resources()
        result = self._executor(
            ecosystem="BADA_BUSINESS_AI_ECOSYSTEM",
            agent=agent,
            task=task.strip(),
            context=dict(context or {}),
            provider_resources=resources,
            policy=BADA_BUSINESS_AI_POLICY,
        )
        if not isinstance(result, dict):
            raise RuntimeError("BADA_BUSINESS_AI_EXECUTOR_INVALID_RESULT")
        return result
