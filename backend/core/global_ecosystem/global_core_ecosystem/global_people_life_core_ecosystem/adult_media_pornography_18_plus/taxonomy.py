"""Canonical adult-media content taxonomy.

Orientation labels are optional content metadata, not viewer/user profile fields.
No inference from appearance, scenes, partners, behaviour or browsing history.
"""
from __future__ import annotations

from collections.abc import Mapping
from copy import deepcopy
from typing import Any

TAXONOMY_VERSION = "1.0.0"
ORIENTATION_LABELS = (
    {"id": "STRAIGHT", "label": "Straight", "meaning": "Heterosexual orientation label"},
    {"id": "GAY", "label": "Gay", "meaning": "Homosexual orientation label"},
    {"id": "BISEXUAL", "label": "Bisexual", "meaning": "Attraction to more than one gender"},
    {"id": "OTHER", "label": "Other", "meaning": "Optional self-described label outside the listed terms"},
    {"id": "UNSPECIFIED", "label": "Unspecified", "meaning": "No orientation label supplied"},
)
PARTICIPANT_CONFIGURATIONS = (
    "DIFFERENT_GENDER", "SAME_GENDER", "MULTIPLE_GENDERS", "UNSPECIFIED"
)
ALLOWED_SOURCES = ("SELF_DECLARED", "AUTHORIZED_RIGHTS_HOLDER")
ALLOWED_SUBJECT_TYPES = ("CREATOR", "PERFORMER")


class AdultContentClassificationError(ValueError):
    """Raised when classification metadata violates the canonical contract."""


def get_classification_catalog() -> dict[str, Any]:
    return {
        "taxonomy_version": TAXONOMY_VERSION,
        "orientation_labels": deepcopy(list(ORIENTATION_LABELS)),
        "participant_configurations": list(PARTICIPANT_CONFIGURATIONS),
        "allowed_sources": list(ALLOWED_SOURCES),
        "allowed_subject_types": list(ALLOWED_SUBJECT_TYPES),
        "orientation_inference_enabled": False,
        "viewer_orientation_profiling_enabled": False,
        "orientation_is_content_metadata_only": True,
    }


def validate_classification_metadata(record: Mapping[str, Any]) -> dict[str, Any]:
    """Validate a metadata-only content record; never accepts media or viewer profiles."""
    if not isinstance(record, Mapping):
        raise TypeError("CLASSIFICATION_RECORD_MUST_BE_A_MAPPING")
    forbidden = {"media", "media_bytes", "binary_content", "raw_media_url", "viewer_profile", "viewer_orientation_profile"}
    if forbidden.intersection(record):
        raise AdultContentClassificationError("MEDIA_OR_VIEWER_PROFILE_NOT_ACCEPTED")

    label = str(record.get("orientation_label", "UNSPECIFIED")).strip().upper()
    labels = {item["id"] for item in ORIENTATION_LABELS}
    if label not in labels:
        raise AdultContentClassificationError("UNKNOWN_ORIENTATION_LABEL")

    subject = str(record.get("classification_subject_type", "")).strip().upper()
    source = str(record.get("orientation_source", "")).strip().upper()
    if record.get("orientation_inferred") is True:
        raise AdultContentClassificationError("ORIENTATION_INFERENCE_PROHIBITED")
    if label != "UNSPECIFIED":
        if subject not in ALLOWED_SUBJECT_TYPES:
            raise AdultContentClassificationError("CREATOR_OR_PERFORMER_SUBJECT_REQUIRED")
        if source not in ALLOWED_SOURCES:
            raise AdultContentClassificationError("SELF_DECLARATION_OR_AUTHORIZED_SOURCE_REQUIRED")
        if not str(record.get("consent_record_reference", "")).strip():
            raise AdultContentClassificationError("CONSENT_RECORD_REFERENCE_REQUIRED")
        if not str(record.get("rights_record_reference", "")).strip():
            raise AdultContentClassificationError("RIGHTS_RECORD_REFERENCE_REQUIRED")

    configuration = str(
        record.get("participant_configuration", "UNSPECIFIED")
    ).strip().upper()
    if configuration not in PARTICIPANT_CONFIGURATIONS:
        raise AdultContentClassificationError("UNKNOWN_PARTICIPANT_CONFIGURATION")

    return {
        "taxonomy_version": TAXONOMY_VERSION,
        "orientation_label": label,
        "orientation_source": source if label != "UNSPECIFIED" else "UNSPECIFIED",
        "classification_subject_type": subject if label != "UNSPECIFIED" else "UNSPECIFIED",
        "participant_configuration": configuration,
        "orientation_inferred": False,
        "viewer_orientation_profile_created": False,
    }


__all__ = [
    "AdultContentClassificationError",
    "ALLOWED_SOURCES",
    "ALLOWED_SUBJECT_TYPES",
    "ORIENTATION_LABELS",
    "PARTICIPANT_CONFIGURATIONS",
    "TAXONOMY_VERSION",
    "get_classification_catalog",
    "validate_classification_metadata",
]
