from pydantic import BaseModel
class MediaCategory(BaseModel):
    id: str
    name: str
    subcategories: list[str]
class MediaListResponse(BaseModel):
    success: bool
    count: int
    categories: list[MediaCategory]
class MediaDetailResponse(BaseModel):
    success: bool
    category: MediaCategory
