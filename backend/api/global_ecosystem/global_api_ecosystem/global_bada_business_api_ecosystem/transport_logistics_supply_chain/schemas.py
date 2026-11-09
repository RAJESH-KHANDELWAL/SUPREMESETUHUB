from pydantic import BaseModel
class TransportCategory(BaseModel):
    id: str
    name: str
    subcategories: list[str]
class TransportListResponse(BaseModel):
    success: bool
    count: int
    categories: list[TransportCategory]
class TransportDetailResponse(BaseModel):
    success: bool
    category: TransportCategory
