from pydantic import BaseModel
class SupplyChainCategory(BaseModel):
    id: str
    name: str
    subcategories: list[str]
class SupplyChainListResponse(BaseModel):
    success: bool
    count: int
    categories: list[SupplyChainCategory]
class SupplyChainDetailResponse(BaseModel):
    success: bool
    category: SupplyChainCategory
