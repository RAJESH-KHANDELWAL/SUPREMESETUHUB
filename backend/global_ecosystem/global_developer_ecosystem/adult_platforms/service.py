"""Safety-first requirements for lawful adult-only digital platforms."""
from __future__ import annotations

REQUIRED_CONTROLS = (
    "age_assurance", "informed_consent", "performer_release_records",
    "privacy_controls", "content_moderation", "reporting_and_takedown",
    "secure_payouts", "jurisdiction_review",
)
DISALLOWED_CONTENT = (
    "sexual_content_involving_minors", "non_consensual_intimate_imagery",
    "coercion", "trafficking", "sexual_extortion", "hidden_camera_content",
)

def validate_adult_platform(controls: list[str] | tuple[str, ...]) -> dict:
    supplied = set(controls)
    missing = [item for item in REQUIRED_CONTROLS if item not in supplied]
    return {
        "eligible_for_design_review": not missing,
        "required_controls": list(REQUIRED_CONTROLS),
        "missing_controls": missing,
        "excluded_content": list(DISALLOWED_CONTENT),
        "note": "Adult-only lawful use cases require local legal review and robust age/consent safeguards.",
    }

__all__ = ["REQUIRED_CONTROLS", "DISALLOWED_CONTENT", "validate_adult_platform"]
