from pydantic import BaseModel
class AviationAerospaceCategory(BaseModel):
 id:str
 name:str
 subcategories:list[str]
class AviationAerospaceListResponse(BaseModel):
 success:bool
 count:int
 categories:list[AviationAerospaceCategory]
class AviationAerospaceDetailResponse(BaseModel):
 success:bool
 category:AviationAerospaceCategory
