"""Translation job specification helpers; no machine translation is performed."""
from dataclasses import dataclass


@dataclass(frozen=True)
class TranslationJob:
    source_language: str
    target_language: str
    content_type: str = "text"
    preserve_formatting: bool = True
    glossary_id: str | None = None


def build_translation_job(source_language: str, target_language: str, *,
                          content_type: str = "text",
                          preserve_formatting: bool = True,
                          glossary_id: str | None = None) -> TranslationJob:
    if not source_language.strip() or not target_language.strip():
        raise ValueError("source_language and target_language are required")
    allowed = {"text", "document", "website", "subtitle", "software"}
    if content_type not in allowed:
        raise ValueError(f"content_type must be one of {sorted(allowed)}")
    return TranslationJob(source_language.strip(), target_language.strip(),
                          content_type, preserve_formatting, glossary_id)
