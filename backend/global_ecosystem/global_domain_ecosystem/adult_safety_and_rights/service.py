REQUIRED_CONTROLS=("age_assurance","informed_consent","performer_release_records","privacy_controls","moderation","reporting_and_takedown","secure_payouts","jurisdiction_review")
def get_adult_safety_framework():
    return {"required_controls":list(REQUIRED_CONTROLS),"excluded":["sexual_content_involving_minors","non_consensual_intimate_imagery","coercion","trafficking","sexual_extortion"],"scope":"lawful_consensual_adults_only","status":"SAFETY_REFERENCE"}
__all__=["REQUIRED_CONTROLS","get_adult_safety_framework"]
