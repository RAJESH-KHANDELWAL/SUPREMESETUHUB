"""Communication Core safety and capability policy."""
ADULT_ACCESS_DEFAULT = "disabled"
MINIMUM_ADULT_AGE = 18
ALLOW_MINORS_IN_ADULT_CATEGORIES = False
ALLOW_NONCONSENSUAL_OR_EXPLOITATIVE_CONTENT = False
ALLOW_ILLEGAL_CONTENT = False
REQUIRE_REGIONAL_LEGAL_REVIEW = True
REQUIRE_EXPLICIT_CONSENT = True
def validate_provider_id(provider_id, known_ids):
    if provider_id not in known_ids:
        raise ValueError("Unknown communication provider")
    return provider_id
def adult_category_enabled(category_id):
    return False
