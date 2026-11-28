from dataclasses import dataclass,field
from typing import Any
@dataclass(frozen=True)
class EducationBusinessCapability:
 capability_id: str
 domain_id: str
 core_domain_id: str
 delivery_modes: tuple[str,...]=("ONLINE","OFFLINE","HYBRID")
 metadata: dict[str,Any]=field(default_factory=dict)
