"""Dependency mapping for continuity planning, not operational control."""
from __future__ import annotations

SECTORS = ("energy", "water", "healthcare", "telecommunications", "transport",
           "food_supply", "finance", "public_services", "data_centres")

def infrastructure_sectors() -> tuple[str, ...]:
    return SECTORS

def assess_dependencies(dependencies: dict[str, list[str] | tuple[str, ...]]) -> dict[str, object]:
    unknown = set(dependencies) - set(SECTORS)
    if unknown:
        raise ValueError(f"Unknown infrastructure sectors: {sorted(unknown)}")
    normalized = {key: tuple(sorted(set(value))) for key, value in dependencies.items()}
    return {
        "dependency_map": normalized,
        "sectors_without_mapping": tuple(sorted(set(SECTORS) - set(normalized))),
        "assessment_only": True,
        "requires_sector_owner_review": True,
    }
