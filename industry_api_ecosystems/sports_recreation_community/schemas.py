from pydantic import BaseModel
class SportsCommunityCategory(BaseModel):
 id:str
 name:str
 subcategories:list[str]
class SportsCommunityListResponse(BaseModel):
 success:bool
 count:int
 categories:list[SportsCommunityCategory]
class SportsCommunityDetailResponse(BaseModel):
 success:bool
 category:SportsCommunityCategory
