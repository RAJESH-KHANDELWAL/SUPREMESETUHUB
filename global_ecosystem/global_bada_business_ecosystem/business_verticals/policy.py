"""Business listing guardrails, including lawful adult-industry boundaries."""
ADULT_VERTICAL_IDS = {"adult_relationship_intimacy", "adult_entertainment_industry"}

def get_vertical_guardrails(vertical_id: str) -> dict:
    key = str(vertical_id or "").strip().casefold()
    if key not in ADULT_VERTICAL_IDS:
        return {
            "adult_only": False,
            "requirements": ["follow applicable local laws", "honest marketing", "consumer protection", "privacy and data security"],
        }
    return {
        "adult_only": True,
        "requirements": [
            "all participants and performers must be verified adults",
            "documented, freely given and revocable consent",
            "no coercion, trafficking, exploitation or non-consensual intimate imagery",
            "documented rights, releases, licensing and performer compensation",
            "age assurance and jurisdiction-aware access controls",
            "privacy-by-design and secure handling of sensitive data",
            "content moderation, reporting and prompt takedown workflows",
            "no misleading health, earnings or safety claims",
            "comply with applicable law and platform/payment-provider rules",
        ],
    }

def validate_adult_business_record(record: dict) -> list[str]:
    """Validate minimum governance declarations; this is not legal certification."""
    errors = []
    if not isinstance(record, dict):
        return ["record must be a dictionary"]
    if record.get("vertical_id") not in ADULT_VERTICAL_IDS:
        errors.append("vertical_id must identify a supported adult vertical")
    required_true = ("adult_participants_verified", "consent_documented", "rights_documented",
                     "age_assurance_enabled", "moderation_process_defined", "privacy_controls_defined")
    for field in required_true:
        if record.get(field) is not True:
            errors.append(f"{field} must be true")
    if record.get("jurisdiction_reviewed") is not True:
        errors.append("jurisdiction_reviewed must be true")
    return errors
