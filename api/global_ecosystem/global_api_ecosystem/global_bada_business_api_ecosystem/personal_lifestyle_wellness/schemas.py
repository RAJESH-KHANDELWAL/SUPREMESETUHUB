from pydantic import BaseModel
class PersonalWellnessCategory(BaseModel):
 id:str
 name:str
 subcategories:list[str]
 access_class:str="general"
class PersonalWellnessListResponse(BaseModel):
 success:bool
 count:int
 categories:list[PersonalWellnessCategory]
class PersonalWellnessDetailResponse(BaseModel):
 success:bool
 category:PersonalWellnessCategory
