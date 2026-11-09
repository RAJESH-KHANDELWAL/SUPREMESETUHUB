"""Canonical AI capability identifiers for domain-level contracts."""

from enum import StrEnum


class AICapability(StrEnum):
    TEXT = "text"
    IMAGE = "image"
    VIDEO = "video"
    AUDIO = "audio"
    SPEECH = "speech"
    CODE = "code"
    GAME = "game"
    MOVIE = "movie"
    DESIGN = "design"
    THREE_D = "3d"
    DOCUMENT = "document"
    RESEARCH = "research"
    AUTOMATION = "automation"


AI_CAPABILITIES: tuple[str, ...] = tuple(item.value for item in AICapability)


def is_supported_capability(value: str) -> bool:
    """Return whether value is a known capability identifier."""
    return value.strip().lower() in AI_CAPABILITIES
