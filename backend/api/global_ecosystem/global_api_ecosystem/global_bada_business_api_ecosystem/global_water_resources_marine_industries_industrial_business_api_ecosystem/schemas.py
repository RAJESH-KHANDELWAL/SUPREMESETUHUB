from pydantic import BaseModel
class WaterMarineCategory(BaseModel):
 id: str
 name: str
 subcategories: list[str]
class WaterMarineListResponse(BaseModel):
 success: bool
 count: int
 categories: list[WaterMarineCategory]
class WaterMarineDetailResponse(BaseModel):
 success: bool
 category: WaterMarineCategory
