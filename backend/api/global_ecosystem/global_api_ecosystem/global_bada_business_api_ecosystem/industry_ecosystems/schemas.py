"""Pydantic response models for the Industry Ecosystems API."""
from pydantic import BaseModel


class IndustryEcosystem(BaseModel):
    id: str
    name: str
    package: str
    coverage: list[str]
    channels: list[str]
    status: str


class IndustryEcosystemListResponse(BaseModel):
    success: bool
    count: int
    industries: list[IndustryEcosystem]


class IndustryEcosystemDetailResponse(BaseModel):
    success: bool
    industry: IndustryEcosystem
