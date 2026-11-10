"""Readiness scorecard; does not direct field operations."""
from __future__ import annotations

DIMENSIONS = ("people", "process", "communications", "equipment",
              "continuity", "training", "governance")

def assess_readiness(scores: dict[str, int]) -> dict[str, object]:
    unknown = set(scores) - set(DIMENSIONS)
    if unknown:
        raise ValueError(f"Unknown readiness dimensions: {sorted(unknown)}")
    invalid = {key: value for key, value in scores.items()
               if not isinstance(value, int) or not 0 <= value <= 5}
    if invalid:
        raise ValueError("Scores must be integers from 0 to 5")
    missing = tuple(name for name in DIMENSIONS if name not in scores)
    complete = not missing
    average = sum(scores.values()) / len(DIMENSIONS) if complete else None
    return {"complete": complete, "missing_dimensions": missing,
            "average_score": average, "scale": "0-5", "human_review_required": True}
