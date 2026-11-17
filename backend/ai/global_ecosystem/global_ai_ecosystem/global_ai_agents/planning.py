"""Agent planning primitives; plans are descriptions, not executed workflows."""
from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True)
class AgentPlanStep:
    step_id: str
    objective: str
    depends_on: tuple[str, ...] = ()
    approval_required: bool = False

    def validate(self) -> None:
        if not self.step_id.strip() or not self.objective.strip():
            raise ValueError("AI_AGENT_PLAN_STEP_INVALID")

def validate_plan(steps: tuple[AgentPlanStep, ...] | list[AgentPlanStep]) -> None:
    """Validate step identifiers and dependencies without executing any step."""
    identifiers = [step.step_id for step in steps]
    if len(identifiers) != len(set(identifiers)):
        raise ValueError("AI_AGENT_PLAN_STEP_IDS_MUST_BE_UNIQUE")
    known = set(identifiers)
    for step in steps:
        step.validate()
        if set(step.depends_on) - known:
            raise ValueError("AI_AGENT_PLAN_DEPENDENCY_NOT_FOUND")
        if step.step_id in step.depends_on:
            raise ValueError("AI_AGENT_PLAN_SELF_DEPENDENCY")
