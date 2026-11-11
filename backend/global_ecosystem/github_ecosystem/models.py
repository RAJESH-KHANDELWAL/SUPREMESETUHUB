"""Typed models for GitHub provider capabilities."""
from dataclasses import asdict, dataclass
from typing import Tuple

@dataclass(frozen=True)
class Capability:
    id: str
    name: str
    category: str
    description: str
    resource_types: Tuple[str, ...] = ()
    requires_credentials: bool = True
    destructive: bool = False
    def to_dict(self):
        value = asdict(self)
        value["resource_types"] = list(self.resource_types)
        return value

@dataclass(frozen=True)
class OperationRequest:
    capability_id: str
    action: str
    owner: str = ""
    repository: str = ""
    resource_type: str = ""
    confirmation: bool = False
