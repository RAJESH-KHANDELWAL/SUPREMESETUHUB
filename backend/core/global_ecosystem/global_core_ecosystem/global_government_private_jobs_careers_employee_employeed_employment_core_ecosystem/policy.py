"""Employment data governance and candidate-protection policies."""
FORBIDDEN_SCREENING_FIELDS=("race","religion","caste","sex_life","sexual_orientation","political_opinion","disability_without_lawful_accommodation_context")
REQUIRED_CONTROLS=("equal_opportunity","purpose_limitation","candidate_consent","data_minimization","source_provenance","jurisdictional_compliance")
def validate_record(payload):
    errors=[]
    if not isinstance(payload,dict): return ["PAYLOAD_MUST_BE_OBJECT"]
    if not str(payload.get("record_id","")).strip(): errors.append("RECORD_ID_REQUIRED")
    if not str(payload.get("name","")).strip(): errors.append("NAME_REQUIRED")
    if payload.get("live_verified") is True and not payload.get("verification_evidence"): errors.append("VERIFICATION_EVIDENCE_REQUIRED")
    if any(k in payload for k in FORBIDDEN_SCREENING_FIELDS): errors.append("PROTECTED_OR_SENSITIVE_TRAIT_SCREENING_NOT_SUPPORTED")
    return errors
