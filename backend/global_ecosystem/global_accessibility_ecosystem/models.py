"""Shared data models for accessibility capabilities."""

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class AccessibilityFeature:
    """A discoverable accessibility feature or assistive capability."""

    feature_id: str
    name: str
    category: str
    description: str
    supported_platforms: tuple[str, ...] = ()
    maturity: str = "basic_normal"
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class AccessibilityNeed:
    """A user-stated accessibility need; never infer a disability."""

    need_id: str
    description: str
    preferred_languages: tuple[str, ...] = ()
    input_methods: tuple[str, ...] = ()
    output_methods: tuple[str, ...] = ()
