"""Platform-specific metadata model for MILLIONAIRE_TRACK."""
from dataclasses import dataclass,field
from typing import Any
@dataclass
class PlatformMetadata:
 record_id:str
 record_type:str
 metadata:dict[str,Any]=field(default_factory=dict)
 platform_id:str="MILLIONAIRE_TRACK"
 def __post_init__(self):
  if not self.record_id.strip() or not self.record_type.strip():raise ValueError("record_id and record_type required")
