"""Validated request schemas for registered organizations."""

from pydantic import BaseModel, Field, HttpUrl


class OrganizationCreateRequest(BaseModel):
    organization_name: str = Field(min_length=1, max_length=200)
    display_name: str = Field(min_length=1, max_length=200)
    organization_type: str = Field(default="BUSINESS", min_length=1, max_length=64)
    owner_id: str | None = Field(default=None, max_length=128)
    email: str | None = Field(default=None, max_length=254)
    phone: str | None = Field(default=None, max_length=32)
    website: str | None = Field(default=None, max_length=2048)
    status: str = Field(default="ACTIVE", max_length=32)


class OrganizationUpdateRequest(BaseModel):
    organization_name: str = Field(min_length=1, max_length=200)
    display_name: str = Field(min_length=1, max_length=200)
    organization_type: str = Field(min_length=1, max_length=64)
    owner_id: str | None = Field(default=None, max_length=128)
    email: str | None = Field(default=None, max_length=254)
    phone: str | None = Field(default=None, max_length=32)
    website: str | None = Field(default=None, max_length=2048)
    status: str = Field(min_length=1, max_length=32)
