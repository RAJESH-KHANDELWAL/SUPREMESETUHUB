from pydantic import BaseModel, Field

class HomeServicesCategory(BaseModel):
 id: str
 name: str
 channels: list[str] = Field(default_factory=list)
 subcategories: list[str]
class HomeServicesListResponse(BaseModel):
 success: bool
 count: int
 categories: list[HomeServicesCategory]
class HomeServicesDetailResponse(BaseModel):
 success: bool
 category: HomeServicesCategory
