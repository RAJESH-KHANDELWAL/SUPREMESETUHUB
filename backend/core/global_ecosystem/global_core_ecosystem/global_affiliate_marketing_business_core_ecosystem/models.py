"""Immutable identity models for affiliate platform catalog entries."""
from __future__ import annotations

from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class AffiliatePlatformIdentity:
    platform_id: str
    name: str
    region_scope: str
    record_type: str
    catalog_status: str
    verification_status: str
    program_status: str
    terms_url: str | None = None

    @classmethod
    def from_record(cls, record: dict[str, object]) -> "AffiliatePlatformIdentity":
        return cls(
            platform_id=str(record["platform_id"]),
            name=str(record["name"]),
            region_scope=str(record["region_scope"]),
            record_type=str(record["record_type"]),
            catalog_status=str(record["catalog_status"]),
            verification_status=str(record["verification_status"]),
            program_status=str(record["program_status"]),
            terms_url=str(record["terms_url"]) if record.get("terms_url") else None,
        )

__all__ = ["AffiliatePlatformIdentity"]
