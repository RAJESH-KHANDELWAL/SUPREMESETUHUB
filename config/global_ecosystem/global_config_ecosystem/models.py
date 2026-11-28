"""Small immutable models shared by configuration services."""

from dataclasses import dataclass, field
from typing import Any, Mapping


@dataclass(frozen=True)
class ConfigSnapshot:
    namespace: str
    values: Mapping[str, Any] = field(default_factory=dict)
    source: str = "defaults"
    valid: bool = True
    errors: tuple = ()

    def as_dict(self):
        return {
            "namespace": self.namespace,
            "values": dict(self.values),
            "source": self.source,
            "valid": self.valid,
            "errors": list(self.errors),
        }
