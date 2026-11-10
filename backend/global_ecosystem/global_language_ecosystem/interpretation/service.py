"""Build interpretation requests; no live interpreter is booked here."""
from dataclasses import dataclass
@dataclass(frozen=True)
class InterpretationRequest:
 source_language: str
 target_language: str
 mode: str
 context: str = "general"

def build_interpretation_request(source_language: str, target_language: str, *, mode: str = "consecutive", context: str = "general") -> InterpretationRequest:
 if not source_language.strip() or not target_language.strip(): raise ValueError("source and target languages are required")
 if mode not in {"consecutive", "simultaneous", "telephone", "video"}: raise ValueError("unsupported interpretation mode")
 return InterpretationRequest(source_language.strip(), target_language.strip(), mode, context)
