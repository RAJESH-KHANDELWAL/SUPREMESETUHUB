"""Catalog of supported language content formats and contexts."""
CONTENT_TYPES = {
    "text": ("plain_text", "rich_text", "documents", "forms"),
    "digital": ("websites", "software_interfaces", "mobile_apps", "chatbots"),
    "audio_visual": ("audio", "video", "subtitles", "captions", "transcripts"),
    "learning": ("lessons", "tests", "vocabulary", "grammar_exercises"),
    "professional": ("legal", "technical", "medical", "financial", "business"),
    "adult_restricted": ("adult_education", "sexual_health_information", "adult_entertainment_metadata"),
}

def get_language_content_types() -> dict[str, tuple[str, ...]]:
    return dict(CONTENT_TYPES)
