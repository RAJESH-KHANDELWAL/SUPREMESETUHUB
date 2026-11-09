from pydantic import BaseModel
class ScienceResearchCategory(BaseModel):
 id:str
 name:str
 subcategories:list[str]
class ScienceResearchListResponse(BaseModel):
 success:bool
 count:int
 categories:list[ScienceResearchCategory]
class ScienceResearchDetailResponse(BaseModel):
 success:bool
 category:ScienceResearchCategory
