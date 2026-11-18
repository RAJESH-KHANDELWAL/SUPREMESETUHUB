"""Typed task contracts for modalities beyond text chat.

These are provider-neutral data contracts only. Media execution adapters are
registered separately and must not be inferred from contract availability.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True, slots=True)
class EmbeddingRequest:
    model: str
    inputs: tuple[str, ...]

    def __post_init__(self):
        if not self.model.strip() or not self.inputs or any(not item.strip() for item in self.inputs):
            raise ValueError("Embedding model and non-empty inputs are required.")


@dataclass(frozen=True, slots=True)
class EmbeddingResponse:
    provider_id: str
    model: str
    vectors: tuple[tuple[float, ...], ...]
    usage: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True, slots=True)
class ImageGenerationRequest:
    model: str
    prompt: str
    count: int = 1
    aspect_ratio: str | None = None

    def __post_init__(self):
        if not self.model.strip() or not self.prompt.strip():
            raise ValueError("Image model and prompt are required.")
        if not 1 <= self.count <= 8:
            raise ValueError("Image count must be between 1 and 8.")


@dataclass(frozen=True, slots=True)
class SpeechSynthesisRequest:
    model: str
    text: str
    voice_id: str | None = None
    output_format: str | None = None

    def __post_init__(self):
        if not self.model.strip() or not self.text.strip():
            raise ValueError("Speech model and text are required.")


@dataclass(frozen=True, slots=True)
class AudioTranscriptionRequest:
    model: str
    audio: bytes
    filename: str
    content_type: str
    language: str | None = None

    def __post_init__(self):
        if not self.model.strip() or not self.audio:
            raise ValueError("Transcription model and audio bytes are required.")
        if not self.filename.strip() or not self.content_type.strip():
            raise ValueError("Audio filename and content type are required.")


@dataclass(frozen=True, slots=True)
class VideoGenerationRequest:
    model: str
    prompt: str
    duration_seconds: int | None = None
    aspect_ratio: str | None = None

    def __post_init__(self):
        if not self.model.strip() or not self.prompt.strip():
            raise ValueError("Video model and prompt are required.")
        if self.duration_seconds is not None and self.duration_seconds < 1:
            raise ValueError("Video duration must be positive.")
