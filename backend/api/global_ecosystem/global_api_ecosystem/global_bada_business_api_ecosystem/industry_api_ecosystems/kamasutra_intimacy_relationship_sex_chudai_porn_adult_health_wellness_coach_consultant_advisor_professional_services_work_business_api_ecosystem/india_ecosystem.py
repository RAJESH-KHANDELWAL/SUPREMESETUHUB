"""Bharat-specific taxonomy extension; validate all law and provider data before publication."""
REGION = "IN"
COVERAGE = ("national", "state", "union_territory", "district", "city")
LOCALISATION_FIELDS = ("state_code", "district_code", "language", "service_region")
LEGAL_REVIEW_REQUIRED = True
