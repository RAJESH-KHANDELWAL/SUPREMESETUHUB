"""Business directory contract; records require independent verification."""
REQUIRED_FIELDS = ("business_id", "legal_name", "country_code", "category_id", "verification_status", "source_url", "last_verified_at")
VERIFICATION_STATES = ("unverified", "pending", "verified", "suspended", "rejected")
