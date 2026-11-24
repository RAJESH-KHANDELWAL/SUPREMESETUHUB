"""Policy guardrails for accessibility features."""

PRINCIPLES = {
    "user_control": "Ask users for preferences; do not infer disability or needs.",
    "privacy": "Collect only the minimum data required and protect sensitive preferences.",
    "consent": "Obtain informed consent before processing voice, video or personal data.",
    "language": "Respect user-selected language and regional requirements.",
    "human_review": "Allow users to correct automated captions, translations and labels.",
    "accessibility": "Test with assistive technologies and people with varied access needs.",
}


def get_principles() -> dict[str, str]:
    """Return a copy of the accessibility policy principles."""
    return dict(PRINCIPLES)
