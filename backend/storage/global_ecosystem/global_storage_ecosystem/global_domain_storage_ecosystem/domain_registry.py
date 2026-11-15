"""Thread-safe in-memory catalog; production persistence belongs in central DB."""
from threading import RLock
from dataclasses import asdict
from .domain_models import DomainRecord
class DomainRegistry:
 def __init__(self): self._records: dict[str, DomainRecord] = {}; self._lock = RLock()
 def register(self, record: DomainRecord) -> dict:
  with self._lock:
   if record.domain_id in self._records: raise ValueError("DUPLICATE_DOMAIN_ID")
   if any(x.domain_name == record.domain_name for x in self._records.values()): raise ValueError("DUPLICATE_DOMAIN_NAME")
   self._records[record.domain_id] = record
   return asdict(record)
 def get(self, domain_id: str) -> dict | None:
  with self._lock:
   item = self._records.get(domain_id)
   return asdict(item) if item else None
 def list(self) -> list[dict]:
  with self._lock: return [asdict(x) for x in self._records.values()]
