"""Global taxonomy extension with jurisdiction-aware country records."""
COVERAGE = ("country", "subdivision", "city", "cross_border")
REQUIRED_JURISDICTION_FIELDS = ("country_code", "legal_review_status", "reviewed_at", "source_urls")
LEGAL_REVIEW_REQUIRED = True
