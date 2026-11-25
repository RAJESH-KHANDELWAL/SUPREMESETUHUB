from dataclasses import dataclass, field
from typing import Any
@dataclass(frozen=True)
class EducationQuery:
 domain_id: str|None=None
 keyword: str|None=None
@dataclass(frozen=True)
class EducationResult:
 status: str
 data: dict[str,Any]=field(default_factory=dict)
 warnings: tuple[str,...]=()
