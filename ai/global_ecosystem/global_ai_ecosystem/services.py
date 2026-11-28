"""AI service taxonomy; these descriptors do not execute provider requests."""
from .schemas import CatalogRecord

SERVICES = tuple(
    CatalogRecord(key, name, "ai_service", description)
    for key, name, description in (
        ("inference", "Model inference", "Run a selected model through an approved runtime."),
        ("chat_completion", "Chat completion", "Generate conversational responses."),
        ("structured_output", "Structured output", "Produce schema-constrained output."),
        ("image_generation", "Image generation", "Create or edit image assets."),
        ("speech_to_text", "Speech to text", "Transcribe audio into text."),
        ("text_to_speech", "Text to speech", "Synthesize spoken audio."),
        ("video_generation", "Video generation", "Generate video from supported inputs."),
        ("embedding", "Embedding service", "Create vector embeddings."),
        ("reranking", "Reranking service", "Rank retrieved documents or passages."),
        ("moderation", "Content moderation", "Evaluate content against configured policies."),
        ("evaluation", "Model evaluation", "Measure quality, safety and task performance."),
        ("fine_tuning", "Fine-tuning", "Adapt supported models using approved datasets."),
    )
)
