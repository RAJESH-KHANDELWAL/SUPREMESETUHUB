"""Validation rules for Prosecution and government legal posts."""
from .models import GovernmentPost
REQUIRED_FIELDS = ("post_id", "post_title", "recruiting_authority", "legal_officer_grade", "prosecution_or_department", "legal_specialism")

def validate_post(post: GovernmentPost) -> None:
    missing = [field for field in REQUIRED_FIELDS if not str(getattr(post, field, "")).strip()]
    if missing:
        raise ValueError("Missing required prosecution_and_government_legal fields: " + ", ".join(missing))
    if post.official_notice_url and not post.official_notice_url.startswith(("https://", "http://")):
        raise ValueError("official_notice_url must use HTTP or HTTPS")
