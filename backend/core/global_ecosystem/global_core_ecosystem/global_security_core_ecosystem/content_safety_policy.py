"""Protective metadata guardrails for adult-platform and sensitive-content safety.

This module validates classification metadata only. It does not inspect, store,
generate, transmit, or moderate media and is not a production age-verification
or consent-verification service.
"""
from __future__ import annotations
from collections.abc import Mapping

ADULT_ORIENTATION_LABELS = frozenset({"STRAIGHT", "GAY", "BISEXUAL", "OTHER", "UNSPECIFIED"})
ADULT_PARTICIPANT_CONFIGURATIONS = frozenset({"DIFFERENT_GENDER", "SAME_GENDER", "MULTIPLE_GENDERS", "UNSPECIFIED"})
ADULT_ORIENTATION_SOURCES = frozenset({"SELF_DECLARED", "AUTHORIZED_RIGHTS_HOLDER"})

PROHIBITED_CONTENT_CLASSES = frozenset({
    "CHILD_SEXUAL_ABUSE_MATERIAL",
    "NON_CONSENSUAL_INTIMATE_IMAGERY",
    "TRAFFICKING_OR_COERCIVE_SEXUAL_EXPLOITATION",
})

def content_safety_baseline() -> dict:
    return {
        "adult_restricted_access_requires_age_assurance": True,
        "consent_and_provenance_review_required_for_intimate_content": True,
        "child_safety_protection_required": True,
        "non_consensual_intimate_imagery_prohibited": True,
        "exploitation_and_trafficking_prohibited": True,
        "reporting_and_takedown_workflows_required": True,
        "sensitive_data_minimization_required": True,
        "orientation_classification_is_content_metadata_only": True,
        "orientation_inference_prohibited": True,
        "viewer_orientation_profiling_prohibited": True,
        "participant_configuration_is_separate": True,
        "media_storage_or_generation_in_core": False,
        "production_enforcement_verified": False,
    }

def validate_content_safety_metadata(record: Mapping) -> dict:
    """Validate a classification record; never accept media bytes or media URLs."""
    if not isinstance(record, Mapping):
        raise TypeError("CONTENT_SAFETY_METADATA_MUST_BE_A_MAPPING")
    if any(key in record for key in ("media", "media_bytes", "binary_content", "raw_media_url")):
        raise ValueError("MEDIA_PAYLOADS_NOT_ACCEPTED_BY_SECURITY_CORE")
    category = str(record.get("content_class", "")).strip().upper()
    if category in PROHIBITED_CONTENT_CLASSES:
        raise ValueError("PROHIBITED_CONTENT_CLASS")
    if category == "AGE_RESTRICTED_ADULT":
        if record.get("age_gate_configured") is not True:
            raise ValueError("AGE_GATE_CONFIGURATION_REQUIRED")
        if record.get("age_assurance_policy_ref") in (None, ""):
            raise ValueError("AGE_ASSURANCE_POLICY_REFERENCE_REQUIRED")
    if "orientation_label" in record:
        label = str(record.get("orientation_label", "")).strip().upper()
        if label not in ADULT_ORIENTATION_LABELS:
            raise ValueError("UNKNOWN_ADULT_ORIENTATION_LABEL")
        if label != "UNSPECIFIED":
            if str(record.get("classification_subject_type", "")).strip().upper() not in {"CREATOR", "PERFORMER"}:
                raise ValueError("CREATOR_OR_PERFORMER_SUBJECT_REQUIRED")
            if str(record.get("orientation_source", "")).strip().upper() not in ADULT_ORIENTATION_SOURCES:
                raise ValueError("SELF_DECLARATION_OR_AUTHORIZED_SOURCE_REQUIRED")
            if record.get("orientation_inferred") is True:
                raise ValueError("ORIENTATION_INFERENCE_PROHIBITED")
    if "participant_configuration" in record:
        if str(record.get("participant_configuration")).strip().upper() not in ADULT_PARTICIPANT_CONFIGURATIONS:
            raise ValueError("UNKNOWN_PARTICIPANT_CONFIGURATION")
    if record.get("viewer_orientation_profile") is not None:
        raise ValueError("VIEWER_ORIENTATION_PROFILING_PROHIBITED")
    if record.get("intimate_content") is True and record.get("consent_review_required") is not True:
        raise ValueError("CONSENT_REVIEW_REQUIRED")
    return {"accepted": True, "content_class": category, "status": "METADATA_VALIDATED_ONLY"}
