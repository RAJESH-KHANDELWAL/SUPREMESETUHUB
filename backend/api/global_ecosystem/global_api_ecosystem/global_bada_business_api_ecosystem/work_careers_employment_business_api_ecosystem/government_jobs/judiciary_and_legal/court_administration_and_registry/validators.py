"""Validation rules for Court administration and registry posts."""
from .models import GovernmentPost
REQUIRED_FIELDS = ("post_id", "post_title", "recruiting_authority", "court_staff_grade", "court_or_registry", "court_function")

def validate_post(post: GovernmentPost) -> None:
    missing = [field for field in REQUIRED_FIELDS if not str(getattr(post, field, "")).strip()]
    if missing:
        raise ValueError("Missing required court_administration_and_registry fields: " + ", ".join(missing))
    if post.official_notice_url and not post.official_notice_url.startswith(("https://", "http://")):
        raise ValueError("official_notice_url must use HTTP or HTTPS")
