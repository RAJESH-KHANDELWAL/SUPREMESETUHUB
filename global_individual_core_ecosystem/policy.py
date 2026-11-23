SENSITIVE_FIELDS={"password","token","access_token","refresh_token","secret","client_secret","private_key","government_id","payment_card"}
PROHIBITED_ADULT_CATEGORIES=("minors","child sexual abuse material","non-consensual intimate imagery","coercion","trafficking","exploitation")
def redact_metadata(value):
    if isinstance(value,dict): return {k:("[REDACTED]" if k.lower() in SENSITIVE_FIELDS else redact_metadata(v)) for k,v in value.items()}
    if isinstance(value,list): return [redact_metadata(v) for v in value]
    return value
def adult_safety_boundary(): return {"lawful_consenting_adults_only":True,"age_assurance_required":True,"consent_and_rights_verification_required":True,"moderation_and_takedown_required":True,"prohibited_categories":list(PROHIBITED_ADULT_CATEGORIES)}
