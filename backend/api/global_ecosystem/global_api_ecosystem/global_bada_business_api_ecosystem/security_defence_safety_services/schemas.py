from pydantic import BaseModel
class SecurityDefenceCategory(BaseModel):
 id:str
 name:str
 subcategories:list[str]
class SecurityDefenceListResponse(BaseModel):
 success:bool
 count:int
 categories:list[SecurityDefenceCategory]
class SecurityDefenceDetailResponse(BaseModel):
 success:bool
 category:SecurityDefenceCategory
