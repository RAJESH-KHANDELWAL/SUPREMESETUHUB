"""Declarative CORE workflows. External side effects are deliberately disabled."""
WORKFLOWS = {
 "discover_programs": {"steps": ("READ_CANONICAL_PROGRAM_CATALOG", "RETURN_PROGRAM_RECORDS"), "side_effects": False},
 "discover_courses": {"steps": ("READ_CANONICAL_COURSE_CATALOG", "APPLY_SEARCH", "RETURN_MATCHES"), "side_effects": False},
 "discover_events": {"steps": ("READ_EVENT_SNAPSHOTS", "DERIVE_DATE_STATUS", "RETURN_EVENTS"), "side_effects": False},
 "prepare_registration": {"steps": ("VALIDATE_REQUIRED_FIELDS", "RETURN_VALIDATION_RESULT"), "side_effects": False, "registration_submitted": False, "payment_processed": False},
}
