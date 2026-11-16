from dataclasses import dataclass
from typing import Mapping, Any
@dataclass(frozen=True)
class CoreEvent:
    name: str
    payload: Mapping[str, Any]
