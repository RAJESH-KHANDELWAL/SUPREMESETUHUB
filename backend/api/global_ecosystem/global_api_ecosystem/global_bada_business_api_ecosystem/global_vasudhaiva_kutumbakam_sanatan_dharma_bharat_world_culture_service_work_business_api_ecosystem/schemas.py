"""Validated API contracts for cultural service, work and business records."""
from __future__ import annotations

from typing import Any
from pydantic import BaseModel, ConfigDict, Field, HttpUrl, field_validator


# Keep request validation aligned with CORE governance.ALLOWED_STATUSES.
ALLOWED_RECORD_STATUSES = frozenset(
    {"DRAFT", "SUBMITTED", "REVIEWED", "APPROVED", "REJECTED", "ARCHIVED"}
)


class CultureServiceWorkBusinessRecordRequest(BaseModel):
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)

    record_id: str = Field(min_length=3, max_length=160)
    capability_id: str = Field(min_length=2, max_length=100)
    record_type: str = Field(min_length=2, max_length=40)
    title: str = Field(min_length=1, max_length=300)
    description: str = Field(min_length=1, max_length=10000)
    organization_name: str | None = Field(default=None, max_length=250)
    location: str | None = Field(default=None, max_length=250)
    website_url: str | None = Field(default=None, max_length=2000)
    source_url: str | None = Field(default=None, max_length=2000)
    status: str = Field(default="DRAFT", min_length=3, max_length=30)
    metadata: dict[str, Any] = Field(default_factory=dict)

    @field_validator("status")
    @classmethod
    def normalize_status(cls, value: str) -> str:
        normalized = value.upper()
        if normalized not in ALLOWED_RECORD_STATUSES:
            raise ValueError("INVALID_RECORD_STATUS")
        return normalized

    @field_validator("website_url", "source_url")
    @classmethod
    def validate_optional_urls(cls, value: str | None) -> str | None:
        if value is None:
            return None
        from pydantic import TypeAdapter, ValidationError

        try:
            TypeAdapter(HttpUrl).validate_python(value)
        except ValidationError as exc:
            raise ValueError("INVALID_URL") from exc
        return value


class CultureServiceWorkBusinessAIRequest(BaseModel):
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)

    question: str = Field(min_length=1, max_length=500)
    domain: str | None = Field(default=None, max_length=20)

    @field_validator("domain")
    @classmethod
    def normalize_domain(cls, value: str | None) -> str | None:
        return value.upper() if value else None
