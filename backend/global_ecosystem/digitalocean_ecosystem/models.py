"""Typed, dependency-free models for the DigitalOcean capability catalog."""
from dataclasses import dataclass, asdict
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
    resource_type: str = ""
    region: str = ""
    destructive: bool = False
    confirmation: bool = False
