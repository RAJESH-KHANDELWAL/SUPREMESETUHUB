"""Stable response contract for canonical Work & Business source discovery."""
from __future__ import annotations
from dataclasses import dataclass
from typing import Any

@dataclass(frozen=True, slots=True)
class WorkBusinessSource:
    source_id: str
    source_name: str
    canonical_package: str
    classification_axis: str
    live_records: bool = False

    def as_dict(self) -> dict[str, Any]:
        return {"source_id": self.source_id, "source_name": self.source_name,
                "canonical_package": self.canonical_package,
                "classification_axis": self.classification_axis,
                "live_records": self.live_records}
