"""Capability taxonomy for discovery; this file does not execute capabilities."""
from __future__ import annotations

from typing import Any

AI_MODALITIES: tuple[dict[str, Any], ...] = (
    {"id": "text", "name": "Text and language", "tasks": ["chat", "summarization", "translation", "classification", "extraction", "reasoning"]},
    {"id": "image", "name": "Image and vision", "tasks": ["image_generation", "image_understanding", "ocr", "visual_question_answering", "image_editing"]},
    {"id": "audio", "name": "Audio and speech", "tasks": ["speech_to_text", "text_to_speech", "audio_understanding", "speaker_diarization", "voice_generation"]},
    {"id": "video", "name": "Video", "tasks": ["video_generation", "video_understanding", "transcription", "summarization", "scene_detection"]},
    {"id": "multimodal", "name": "Multimodal", "tasks": ["text_image", "text_audio", "text_video", "cross_modal_reasoning"]},
    {"id": "code", "name": "Code and software", "tasks": ["code_generation", "code_review", "debugging", "test_generation", "documentation"]},
    {"id": "embedding", "name": "Embeddings and retrieval", "tasks": ["embeddings", "reranking", "semantic_search", "retrieval_augmented_generation"]},
    {"id": "spatial_3d", "name": "Spatial, 3D and embodied", "tasks": ["3d_generation", "pose_estimation", "spatial_reasoning", "robotics_perception"]},
)

AI_CAPABILITY_GROUPS: tuple[dict[str, Any], ...] = (
    {"id": "assistant", "name": "Assistant and conversational systems", "modalities": ["text", "audio", "multimodal"]},
    {"id": "generative_media", "name": "Generative media", "modalities": ["image", "audio", "video", "spatial_3d"]},
    {"id": "knowledge", "name": "Knowledge, search and retrieval", "modalities": ["text", "embedding", "multimodal"]},
    {"id": "developer_tools", "name": "Developer and software engineering", "modalities": ["text", "code", "embedding"]},
    {"id": "enterprise_automation", "name": "Enterprise automation and analytics", "modalities": ["text", "embedding", "multimodal"]},
    {"id": "speech_language", "name": "Speech, translation and Indic languages", "modalities": ["text", "audio"]},
    {"id": "safety_governance", "name": "Safety, moderation and governance", "modalities": ["text", "image", "audio", "video"]},
)


def list_ai_modalities() -> tuple[dict[str, Any], ...]:
    return tuple({**item, "tasks": list(item["tasks"])} for item in AI_MODALITIES)


def list_ai_capability_groups() -> tuple[dict[str, Any], ...]:
    return tuple({**item, "modalities": list(item["modalities"])} for item in AI_CAPABILITY_GROUPS)
