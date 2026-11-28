"""Typed Company sector record."""
from dataclasses import dataclass
@dataclass(frozen=True,slots=True)
class SectorRecord:
 sector_id:str
 name:str
 description:str
 industry_ids:tuple[str,...]=()
 status:str="curated_taxonomy"
