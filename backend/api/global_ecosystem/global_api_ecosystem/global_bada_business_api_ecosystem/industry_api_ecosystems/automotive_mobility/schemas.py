from pydantic import BaseModel
class AutomotiveMobilityCategory(BaseModel):
 id:str
 name:str
 subcategories:list[str]
class AutomotiveMobilityListResponse(BaseModel):
 success:bool
 count:int
 categories:list[AutomotiveMobilityCategory]
class AutomotiveMobilityDetailResponse(BaseModel):
 success:bool
 category:AutomotiveMobilityCategory
