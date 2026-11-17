"""Typed contracts for adult-content classification metadata."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any


class Orientation(str, Enum):
    STRAIGHT = "STRAIGHT"
    GAY = "GAY"
    BISEXUAL = "BISEXUAL"
    OTHER = "OTHER"
    UNSPECIFIED = "UNSPECIFIED"


class ParticipantConfiguration(str, Enum):
    DIFFERENT_GENDER = "DIFFERENT_GENDER"
    SAME_GENDER = "SAME_GENDER"
    MULTIPLE_GENDERS = "MULTIPLE_GENDERS"
    UNSPECIFIED = "UNSPECIFIED"


@dataclass(frozen=True)
class ContentClassification:
    """Classification supplied by an authorised source, never inferred by CORE."""

    orientation_label: Orientation = Orientation.UNSPECIFIED
    orientation_source: str = "UNSPECIFIED"
    participant_configuration: ParticipantConfiguration = (
        ParticipantConfiguration.UNSPECIFIED
    )


@dataclass(frozen=True)
class PolicyEvidence:
    """Boolean attestations supplied by trusted application/governance workflows."""

    all_depicted_persons_verified_adults: bool = False
    informed_consent_documented: bool = False
    distribution_rights_documented: bool = False
    moderation_approved: bool = False
    jurisdiction_permitted: bool = False
    prohibited_content_detected: bool = False


def result_envelope(
    *, allowed: bool, status: str, reasons: list[str], data: dict[str, Any] | None = None
) -> dict[str, Any]:
    return {
        "allowed": allowed,
        "status": status,
        "reasons": list(reasons),
        "data": dict(data or {}),
        "execution_enabled": False,
        "live_verification": False,
    }
