"""Non-operational preparedness exercise planner."""
from __future__ import annotations

_TYPES = ("tabletop", "communications_drill", "evacuation_drill",
          "cyber_incident_simulation", "business_continuity_exercise")

def exercise_types() -> tuple[str, ...]:
    return _TYPES

def build_exercise_plan(title: str, exercise_type: str, objectives: list[str]) -> dict[str, object]:
    if not title.strip():
        raise ValueError("title is required")
    if exercise_type not in _TYPES:
        raise ValueError("Unsupported exercise_type")
    clean_objectives = tuple(item.strip() for item in objectives if item.strip())
    if not clean_objectives:
        raise ValueError("At least one objective is required")
    return {"title": title.strip(), "exercise_type": exercise_type,
            "objectives": clean_objectives, "requires_facilitator": True,
            "requires_after_action_review": True}
