"""In-memory read-only taxonomy registry with deterministic lookup."""
from __future__ import annotations
class EntityRelationshipRegistry:
    def __init__(self, records):
        self._records={}
        for record in records:
            key=record["ecosystem_id"]
            if key in self._records: raise ValueError(f"duplicate category id: {key}")
            self._records[key]=dict(record)
    def list(self): return [dict(v) for v in self._records.values()]
    def get(self, key): return dict(self._records[key]) if key in self._records else None
    def count(self): return len(self._records)
    def names(self): return [v["name"] for v in self._records.values()]
