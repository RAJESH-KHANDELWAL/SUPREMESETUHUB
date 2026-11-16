"""Evidence-aware historical event record and chronology validation."""
from dataclasses import dataclass
from typing import Optional, Tuple

@dataclass(frozen=True)
class HistoricalEvent:
    event_id: str
    title: str
    start_label: str
    end_label: Optional[str] = None
    region: Optional[str] = None
    event_type: str = "unspecified"
    evidence_refs: Tuple[str, ...] = ()
    dating_method: str = "unknown"
    confidence: str = "unknown"
    disputed: bool = False
    notes: str = ""

    def __post_init__(self):
        if not self.event_id.strip() or not self.title.strip() or not self.start_label.strip():
            raise ValueError("EVENT_ID_TITLE_AND_START_DATE_REQUIRED")
        if self.confidence not in {"high","medium","low","contested","unknown"}:
            raise ValueError("INVALID_EVENT_CONFIDENCE")
        if not self.evidence_refs and self.confidence == "high":
            raise ValueError("HIGH_CONFIDENCE_EVENT_REQUIRES_EVIDENCE_REFERENCE")

def validate_event_sequence(events):
    """Return ordering diagnostics; unknown date labels are never silently parsed."""
    seen=set()
    diagnostics=[]
    for event in events:
        if event.event_id in seen:
            diagnostics.append({"event_id":event.event_id,"issue":"DUPLICATE_EVENT_ID"})
        seen.add(event.event_id)
        if not event.evidence_refs:
            diagnostics.append({"event_id":event.event_id,"issue":"MISSING_EVIDENCE_REFERENCES"})
        if event.disputed:
            diagnostics.append({"event_id":event.event_id,"issue":"DISPUTED_INTERPRETATION"})
    return diagnostics
