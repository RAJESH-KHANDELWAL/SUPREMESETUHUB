"""Response schemas for Energy, Utilities & Environment."""
from pydantic import BaseModel

class EnergyEnvironmentCategory(BaseModel):
    id: str
    name: str
    subcategories: list[str]

class EnergyEnvironmentListResponse(BaseModel):
    success: bool
    count: int
    categories: list[EnergyEnvironmentCategory]

class EnergyEnvironmentDetailResponse(BaseModel):
    success: bool
    category: EnergyEnvironmentCategory
