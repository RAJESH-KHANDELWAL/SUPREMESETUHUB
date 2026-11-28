"""App-specific metadata record for YOUTAG_RECHARGES_APP."""
from dataclasses import dataclass,field
from typing import Any
@dataclass
class AppMetadataRecord:
 record_id:str
 record_type:str
 metadata:dict[str,Any]=field(default_factory=dict)
 app_id:str="YOUTAG_RECHARGES_APP"
 def __post_init__(self):
  if not self.record_id.strip() or not self.record_type.strip():raise ValueError("record_id and record_type required")
