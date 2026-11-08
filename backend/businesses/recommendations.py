"""Prioritized operational action plans from Business assessments."""
from __future__ import annotations

from typing import Any

from backend.businesses.intelligence import BusinessAssessment


class BusinessActionPlanner:
    """Converts assessment signals into transparent follow-up tasks."""

    PRIORITY = {"CRITICAL": 1, "WARNING": 2, "CAUTION": 3, "INFO": 4}

    def build(self, assessment: BusinessAssessment) -> dict[str, Any]:
        ordered = sorted(
            assessment.signals,
            key=lambda signal: (
                self.PRIORITY.get(signal.level, 9), -signal.score, signal.code
            ),
        )
        tasks = [
            {
                "priority": index + 1,
                "signal_code": signal.code,
                "level": signal.level,
                "task": signal.action,
            }
            for index, signal in enumerate(ordered)
        ]
        for recommendation in assessment.recommendations:
            tasks.append({
                "priority": len(tasks) + 1,
                "signal_code": "GENERAL_RECOMMENDATION",
                "level": "INFO",
                "task": recommendation,
            })
        return {
            "business_id": assessment.business_id,
            "plan_type": "PROFILE_AND_OPERATIONS_IMPROVEMENT",
            "tasks": tasks,
            "completion_note": (
                "Track task completion separately; this plan does not certify "
                "compliance or business performance."
            ),
        }
