from pydantic import BaseModel
class MiningMetalsCategory(BaseModel):
 id:str
 name:str
 subcategories:list[str]
class MiningMetalsListResponse(BaseModel):
 success:bool
 count:int
 categories:list[MiningMetalsCategory]
class MiningMetalsDetailResponse(BaseModel):
 success:bool
 category:MiningMetalsCategory
