from pydantic import BaseModel
class ManufacturingCategory(BaseModel):
    id: str
    name: str
    subcategories: list[str]
class ManufacturingListResponse(BaseModel):
    success: bool
    count: int
    categories: list[ManufacturingCategory]
class ManufacturingDetailResponse(BaseModel):
    success: bool
    category: ManufacturingCategory
