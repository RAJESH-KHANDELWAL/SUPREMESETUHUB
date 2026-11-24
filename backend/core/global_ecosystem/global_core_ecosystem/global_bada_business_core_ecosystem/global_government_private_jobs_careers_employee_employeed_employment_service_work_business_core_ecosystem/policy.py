"""Business-service governance and legal-boundary checks."""
REQUIRED_CONTROLS=("jurisdictional_licensing","transparent_fees","candidate_consent","data_minimization","equal_opportunity","source_provenance","no_guaranteed_job_claims")
FORBIDDEN_FIELDS=("race","religion","caste","sex_life","sexual_orientation","political_opinion")
def validate_provider_record(payload):
 errors=[]
 if not isinstance(payload,dict): return ["PAYLOAD_MUST_BE_OBJECT"]
 if not str(payload.get("record_id","")).strip(): errors.append("RECORD_ID_REQUIRED")
 if not str(payload.get("name","")).strip(): errors.append("NAME_REQUIRED")
 if payload.get("licensed_activity") is True and not payload.get("licence_reference"): errors.append("LICENCE_REFERENCE_REQUIRED")
 if payload.get("live_verified") is True and not payload.get("verification_evidence"): errors.append("VERIFICATION_EVIDENCE_REQUIRED")
 if any(k in payload for k in FORBIDDEN_FIELDS): errors.append("PROTECTED_OR_SENSITIVE_TRAIT_SCREENING_NOT_SUPPORTED")
 if payload.get("guaranteed_job") is True: errors.append("GUARANTEED_JOB_CLAIMS_NOT_SUPPORTED")
 return errors
