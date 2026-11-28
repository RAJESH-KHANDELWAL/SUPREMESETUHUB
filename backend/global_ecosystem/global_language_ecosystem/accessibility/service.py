"""Accessibility metadata checks for multilingual content."""
def validate_accessibility_metadata(*, language_code: str, has_transcript: bool,
                                    has_captions: bool, plain_language_reviewed: bool) -> tuple[str, ...]:
    issues = []
    if not language_code.strip(): issues.append("missing_language_code")
    if not has_transcript: issues.append("transcript_missing")
    if not has_captions: issues.append("captions_missing")
    if not plain_language_reviewed: issues.append("plain_language_review_pending")
    return tuple(issues)
