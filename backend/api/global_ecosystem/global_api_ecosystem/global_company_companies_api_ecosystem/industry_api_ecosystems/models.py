"""Typed industry taxonomy records."""
from dataclasses import dataclass
@dataclass(frozen=True,slots=True)
class IndustryRecord:
 industry_id:str
 name:str
 classification_status:str="curated_taxonomy"
