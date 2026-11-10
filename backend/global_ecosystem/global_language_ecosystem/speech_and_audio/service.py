"""Speech task specification; inference engines are supplied by separate layers."""
from dataclasses import dataclass


@dataclass(frozen=True)
class SpeechTask:
    task_type: str
    language_code: str
    output_format: str = "text"
    speaker_labels: bool = False


def build_speech_task(task_type: str, language_code: str, *,
                      output_format: str = "text",
                      speaker_labels: bool = False) -> SpeechTask:
    if task_type not in {"recognition", "transcription", "text_to_speech", "subtitles"}:
        raise ValueError("unsupported speech task_type")
    if not language_code.strip():
        raise ValueError("language_code is required")
    if output_format not in {"text", "srt", "vtt", "wav", "mp3"}:
        raise ValueError("unsupported output_format")
    return SpeechTask(task_type, language_code, output_format, speaker_labels)
