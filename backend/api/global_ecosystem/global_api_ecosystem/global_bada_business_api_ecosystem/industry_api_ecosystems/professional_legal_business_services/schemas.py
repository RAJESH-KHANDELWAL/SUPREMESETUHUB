"""Response schemas for Professional, Legal & Business Services."""
from pydantic import BaseModel

class ProfessionalServicesCategory(BaseModel):
    id: str
    name: str
    subcategories: list[str]

class ProfessionalServicesListResponse(BaseModel):
    success: bool
    count: int
    categories: list[ProfessionalServicesCategory]

class ProfessionalServicesDetailResponse(BaseModel):
    success: bool
    category: ProfessionalServicesCategory
