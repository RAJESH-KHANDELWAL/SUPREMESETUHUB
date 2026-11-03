"""Validation rules for Government accounts, taxation and audit posts."""
from .models import GovernmentPost
REQUIRED_FIELDS = ("post_id", "post_title", "recruiting_authority", "accounts_or_audit_grade", "department_or_audit_body", "finance_specialism")

def validate_post(post: GovernmentPost) -> None:
    missing = [field for field in REQUIRED_FIELDS if not str(getattr(post, field, "")).strip()]
    if missing:
        raise ValueError("Missing required government_accounts_tax_and_audit fields: " + ", ".join(missing))
    if post.official_notice_url and not post.official_notice_url.startswith(("https://", "http://")):
        raise ValueError("official_notice_url must use HTTP or HTTPS")
