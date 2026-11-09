"""Agent building-block definitions; no autonomous execution is started here."""
from .schemas import CatalogRecord

AGENT_COMPONENTS = tuple(
    CatalogRecord(key, name, "agent_component", description)
    for key, name, description in (
        ("planner", "Planner", "Breaks a goal into ordered, bounded steps."),
        ("router", "Model and tool router", "Selects an eligible model or tool."),
        ("tool_executor", "Tool executor", "Invokes explicitly permitted tools."),
        ("memory", "Memory manager", "Applies configured memory read/write policies."),
        ("evaluator", "Evaluator", "Checks outputs against task criteria."),
        ("guardrail", "Guardrail", "Enforces safety and policy constraints."),
        ("human_approval", "Human approval gate", "Pauses sensitive actions for approval."),
    )
)
