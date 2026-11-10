"""Adult-language and sexual-health language support, with safeguards."""
from .service import classify_adult_language_request, validate_adult_content_context
__all__ = ["classify_adult_language_request", "validate_adult_content_context"]
