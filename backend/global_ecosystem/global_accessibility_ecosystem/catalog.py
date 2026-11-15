"""Starter catalogue of accessibility capabilities."""

from .models import AccessibilityFeature

FEATURES = (
    AccessibilityFeature(
        feature_id="screen_reader_support",
        name="Screen reader support",
        category="digital_accessibility",
        description="Expose meaningful labels, headings, landmarks and reading order.",
        supported_platforms=("web", "mobile", "desktop"),
    ),
    AccessibilityFeature(
        feature_id="keyboard_navigation",
        name="Keyboard navigation",
        category="digital_accessibility",
        description="Make interactive controls usable without a pointer.",
        supported_platforms=("web", "desktop"),
    ),
    AccessibilityFeature(
        feature_id="captions_and_subtitles",
        name="Captions and subtitles",
        category="captions",
        description="Provide synchronized text for spoken audio and meaningful sounds.",
        supported_platforms=("web", "mobile", "desktop", "video"),
    ),
    AccessibilityFeature(
        feature_id="language_access",
        name="Language access",
        category="language_access",
        description="Support localization, translated interfaces and language selection.",
        supported_platforms=("web", "mobile", "desktop"),
    ),
    AccessibilityFeature(
        feature_id="adaptive_input",
        name="Adaptive input",
        category="adaptive_technologies",
        description="Support alternative input methods and configurable controls.",
        supported_platforms=("web", "mobile", "desktop", "device"),
    ),
)


def list_features(category: str | None = None) -> list[AccessibilityFeature]:
    """Return catalogue entries, optionally filtered by category."""
    if category is None:
        return list(FEATURES)
    return [item for item in FEATURES if item.category == category]
