from pydantic import BaseModel
class TechnologyCategory(BaseModel):
    id: str
    name: str
    subcategories: list[str]
class TechnologyListResponse(BaseModel):
    success: bool
    count: int
    categories: list[TechnologyCategory]
class TechnologyDetailResponse(BaseModel):
    success: bool
    category: TechnologyCategory
