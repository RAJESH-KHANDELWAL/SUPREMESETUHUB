"""Domain policies for Bada Business program operations."""

ALLOWED_PROGRAM_STATES = frozenset({
    "AVAILABLE",
    "UPCOMING",
    "PAST_EVENT_DATE",
    "UNCONFIRMED",
    "UNKNOWN",
})

def normalize_program_id(program_id: str) -> str:
    if not isinstance(program_id, str) or not program_id.strip():
        raise ValueError("program_id must be a non-empty string")
    return program_id.strip().lower().replace("-", "_").replace(" ", "_")


def validate_enrollment_request(program: dict, applicant: dict) -> dict:
    """Validate request completeness; never submit registration or collect payment."""
    if not isinstance(program, dict) or not program.get("program_id"):
        raise ValueError("A known program is required")
    if not isinstance(applicant, dict):
        raise ValueError("applicant must be a mapping")
    required = ("name", "mobile_number", "email")
    missing = [field for field in required if not str(applicant.get(field, "")).strip()]
    if missing:
        raise ValueError("Missing applicant fields: " + ", ".join(missing))
    return {
        "valid": True,
        "program_id": program["program_id"],
        "applicant_fields_present": list(required),
        "registration_submitted": False,
        "payment_processed": False,
        "next_step": "Confirm current eligibility, price, schedule and terms with Bada Business.",
    }
