"""Domain taxonomy for central recruitment authorities."""
AUTHORITY_TYPES = ("ministry", "department", "constitutional_body", "statutory_body", "recruiting_commission", "public_institution")
AUTHORITY_RECORD_FIELDS = ("id", "name", "authority_type", "jurisdiction", "official_website", "recruitment_scope")

def get_authority_taxonomy() -> dict:
    return {"domain_id": "central_recruitment_authorities", "authority_types": AUTHORITY_TYPES, "required_fields": AUTHORITY_RECORD_FIELDS, "classification_note": "Classify the legal and administrative authority separately from the body conducting an examination."}
