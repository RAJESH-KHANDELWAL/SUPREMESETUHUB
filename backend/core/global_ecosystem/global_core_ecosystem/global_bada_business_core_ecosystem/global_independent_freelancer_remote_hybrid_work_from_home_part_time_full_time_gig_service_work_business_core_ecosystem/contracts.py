"""Stable discovery contracts."""
from dataclasses import dataclass,field
from typing import Any
@dataclass(frozen=True)
class WorkQuery:
 domain_id:str|None=None
 keyword:str|None=None
 work_mode:str|None=None
 region_id:str|None=None
@dataclass(frozen=True)
class WorkResult:
 status:str
 data:dict[str,Any]=field(default_factory=dict)
 warnings:tuple[str,...]=()
