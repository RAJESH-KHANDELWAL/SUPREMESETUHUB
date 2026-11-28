"""Typed security governance models."""
from dataclasses import dataclass, field
@dataclass(frozen=True)
class SecurityAsset:
    asset_id: str
    name: str
    asset_type: str
    owner: str
    classification: str = "internal"
    region: str | None = None
    tags: tuple[str, ...] = field(default_factory=tuple)
    def __post_init__(self):
        if not all((self.asset_id.strip(), self.name.strip(), self.asset_type.strip(), self.owner.strip())):
            raise ValueError("asset_id, name, asset_type and owner are required")
        if self.classification not in {"public", "internal", "confidential", "restricted"}:
            raise ValueError("invalid asset classification")
