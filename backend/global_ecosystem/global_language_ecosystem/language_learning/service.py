"""Simple structured language-learning plan builder."""
from dataclasses import dataclass


@dataclass(frozen=True)
class LearningPlan:
    target_language: str
    learner_level: str
    weekly_minutes: int
    focus_areas: tuple[str, ...]


def create_learning_plan(target_language: str, learner_level: str,
                         weekly_minutes: int = 150,
                         focus_areas: tuple[str, ...] = ("speaking", "listening", "reading", "writing")) -> LearningPlan:
    levels = {"beginner", "elementary", "intermediate", "advanced", "proficient"}
    if learner_level not in levels:
        raise ValueError(f"learner_level must be one of {sorted(levels)}")
    if weekly_minutes < 15:
        raise ValueError("weekly_minutes must be at least 15")
    if not target_language.strip() or not focus_areas:
        raise ValueError("target_language and focus_areas are required")
    return LearningPlan(target_language.strip(), learner_level, weekly_minutes, tuple(focus_areas))
