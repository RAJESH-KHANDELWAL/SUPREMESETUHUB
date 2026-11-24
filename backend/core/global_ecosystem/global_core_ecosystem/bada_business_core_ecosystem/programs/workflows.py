"""CORE workflow contracts; execution is delegated to injected handlers."""

WORKFLOWS = {
    "discover_programs": {
        "steps": ("LOAD_CANONICAL_PROGRAMS", "APPLY_QUERY_FILTERS", "RETURN_MATCHES"),
        "side_effects": False,
    },
    "compare_programs": {
        "steps": ("LOAD_SELECTED_PROGRAMS", "NORMALIZE_COMPARISON_FIELDS", "RETURN_COMPARISON"),
        "side_effects": False,
    },
    "prepare_enrollment_request": {
        "steps": ("LOAD_PROGRAM", "VALIDATE_APPLICANT_FIELDS", "RETURN_REVIEW_REQUIRED_REQUEST"),
        "side_effects": False,
        "registration_submitted": False,
        "payment_processed": False,
    },
}
