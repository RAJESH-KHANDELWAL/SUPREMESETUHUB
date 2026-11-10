"""Validated request and response contracts for the cultural API."""
from __future__ import annotations
from pydantic import BaseModel, Field

class CulturalSearchRequest(BaseModel):
    query: str = Field(min_length=1, max_length=300)
    domain: str | None = Field(default=None, max_length=100)

class CulturalRecordWriteRequest(BaseModel):
    record_id: str = Field(min_length=3, max_length=160)
    domain_id: str = Field(min_length=2, max_length=100)
    title: str = Field(min_length=1, max_length=500)
    content: str = Field(min_length=1, max_length=100000)
    source_kind: str = Field(min_length=2, max_length=80)
    confidence: str = Field(min_length=2, max_length=40)
    source_url: str | None = Field(default=None, max_length=2000)
    publication_status: str = Field(default="DRAFT", max_length=30)
    metadata: dict = Field(default_factory=dict)
