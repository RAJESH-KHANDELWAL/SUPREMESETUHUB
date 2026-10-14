"""Validated request schemas for business resources."""

from typing import Any
from pydantic import BaseModel, Field, HttpUrl


class BusinessCreateRequest(BaseModel):
    name: str = Field(min_length=1, max_length=200)
    category: str = Field(default="", max_length=100)
    location: str = Field(default="", max_length=300)
    website: str = Field(default="", max_length=2048)
    public_contact: str = Field(default="", max_length=300)
    source: str = Field(default="", max_length=100)
    metadata: dict[str, Any] = Field(default_factory=dict)


class BusinessStatusRequest(BaseModel):
    status: str = Field(min_length=1, max_length=32)
