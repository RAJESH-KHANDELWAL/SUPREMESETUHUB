from dataclasses import dataclass, field
from typing import Any
@dataclass(frozen=True)
class IndividualContext:
    actor_ref:str|None=None
    tenant_ref:str|None=None
    region:str|None=None
    consent_ref:str|None=None
@dataclass(frozen=True)
class CoreResult:
    status:str
    data:dict[str,Any]=field(default_factory=dict)
    warnings:tuple[str,...]=()
