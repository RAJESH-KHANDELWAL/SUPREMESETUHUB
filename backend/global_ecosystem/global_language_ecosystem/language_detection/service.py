"""Validate outputs returned by a separately hosted language detector."""
from dataclasses import dataclass
@dataclass(frozen=True)
class DetectionResult:
 language_code: str
 confidence: float
 script: str | None = None

def validate_detection_result(result: DetectionResult) -> DetectionResult:
 if not result.language_code.strip(): raise ValueError("language_code is required")
 if not 0.0 <= result.confidence <= 1.0: raise ValueError("confidence must be between 0 and 1")
 return result
