"""Canonical AI capability taxonomy."""
from .schemas import CatalogRecord

CAPABILITIES = tuple(
    CatalogRecord(key, label, "capability", description)
    for key, label, description in (
        ("text", "Text generation", "Generate, transform and summarize text."),
        ("reasoning", "Reasoning", "Structured problem solving and analysis."),
        ("vision", "Vision", "Interpret images and visual inputs."),
        ("image", "Image generation", "Generate and edit images."),
        ("audio", "Audio understanding", "Understand audio and sound inputs."),
        ("speech", "Speech", "Speech recognition and speech synthesis."),
        ("video", "Video", "Understand, generate and transform video."),
        ("code", "Code", "Generate, explain, review and transform code."),
        ("embeddings", "Embeddings", "Create vector representations of content."),
        ("reranking", "Reranking", "Reorder retrieval candidates by relevance."),
        ("documents", "Document intelligence", "Extract and reason over documents."),
        ("research", "Research", "Multi-source research and grounded synthesis."),
        ("agents", "Agent execution", "Tool-using and goal-directed agent workflows."),
        ("automation", "Automation", "Execute approved multi-step workflows."),
        ("3d", "3D generation", "Create or process 3D assets."),
    )
)
