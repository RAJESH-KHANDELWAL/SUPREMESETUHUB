"""API-boundary adapter for canonical adult-media classification metadata."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from backend.core.global_ecosystem.global_core_ecosystem.global_people_life_core_ecosystem.adult_media_pornography_18_plus.taxonomy import (
    validate_classification_metadata,
)


def validate_adult_media_classification(payload: Mapping[str, Any]) -> dict[str, Any]:
    """Validate metadata using the canonical CORE contract; accepts no media bytes."""
    if not isinstance(payload, Mapping):
        raise TypeError("CLASSIFICATION_PAYLOAD_MUST_BE_A_MAPPING")
    return validate_classification_metadata(payload)


__all__ = ["validate_adult_media_classification"]
