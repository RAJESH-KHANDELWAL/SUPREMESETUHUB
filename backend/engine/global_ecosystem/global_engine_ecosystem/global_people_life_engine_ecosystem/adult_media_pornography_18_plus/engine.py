"""Adult media execution boundary with classification metadata safeguards."""
from typing import Any

ORIENTATION_LABELS = frozenset({"STRAIGHT", "GAY", "BISEXUAL", "OTHER", "UNSPECIFIED"})
PARTICIPANT_CONFIGURATIONS = frozenset({"DIFFERENT_GENDER", "SAME_GENDER", "MULTIPLE_GENDERS", "UNSPECIFIED"})
ORIENTATION_SOURCES = frozenset({"SELF_DECLARED", "AUTHORIZED_RIGHTS_HOLDER"})


def validate_classification_payload(payload: dict[str, Any]) -> dict[str, Any]:
    if any(key in payload for key in ("media", "media_bytes", "binary_content", "raw_media_url", "viewer_profile", "viewer_orientation_profile")):
        raise ValueError("MEDIA_OR_VIEWER_PROFILE_NOT_ACCEPTED_BY_CLASSIFICATION_BOUNDARY")
    label = str(payload.get("orientation_label", "UNSPECIFIED")).strip().upper()
    if label not in ORIENTATION_LABELS:
        raise ValueError("UNKNOWN_ADULT_ORIENTATION_LABEL")
    subject = str(payload.get("classification_subject_type", "")).strip().upper()
    source = str(payload.get("orientation_source", "")).strip().upper()
    if payload.get("orientation_inferred") is True:
        raise ValueError("ORIENTATION_INFERENCE_PROHIBITED")
    if label != "UNSPECIFIED":
        if subject not in {"CREATOR", "PERFORMER"}:
            raise ValueError("CREATOR_OR_PERFORMER_SUBJECT_REQUIRED")
        if source not in ORIENTATION_SOURCES:
            raise ValueError("SELF_DECLARATION_OR_AUTHORIZED_SOURCE_REQUIRED")
        if not str(payload.get("consent_record_reference", "")).strip():
            raise ValueError("CONSENT_RECORD_REFERENCE_REQUIRED")
        if not str(payload.get("rights_record_reference", "")).strip():
            raise ValueError("RIGHTS_RECORD_REFERENCE_REQUIRED")
    participant_configuration = str(payload.get("participant_configuration", "UNSPECIFIED")).strip().upper()
    if participant_configuration not in PARTICIPANT_CONFIGURATIONS:
        raise ValueError("UNKNOWN_PARTICIPANT_CONFIGURATION")
    return {
        "orientation_label": label,
        "orientation_source": source if label != "UNSPECIFIED" else "UNSPECIFIED",
        "classification_subject_type": subject if label != "UNSPECIFIED" else "UNSPECIFIED",
        "participant_configuration": participant_configuration,
        "orientation_inferred": False,
    }


class ProviderEngine:
    provider = "ADULT MEDIA PORNOGRAPHY 18 PLUS"
    layer = "ENGINE"

    def __init__(self, handler=None):
        self._handler = handler

    def health(self):
        return {
            "provider": self.provider,
            "layer": self.layer,
            "status": "READY" if callable(self._handler) else "NOT_CONFIGURED",
            "classification_validation_available": True,
            "media_execution_enabled": False,
        }

    def execute(self, operation: str, payload: dict[str, Any] | None = None):
        if not callable(self._handler):
            raise NotImplementedError(self.provider + " engine handler is not configured")
        safe_payload = dict(payload or {})
        classification = safe_payload.get("classification")
        if classification is not None:
            if not isinstance(classification, dict):
                raise TypeError("CLASSIFICATION_METADATA_MUST_BE_A_MAPPING")
            safe_payload["classification"] = validate_classification_payload(classification)
        if any(key in safe_payload for key in ("media_bytes", "binary_content")):
            raise ValueError("RAW_MEDIA_PAYLOAD_NOT_ACCEPTED_BY_METADATA_ENGINE")
        return self._handler(operation, safe_payload)
