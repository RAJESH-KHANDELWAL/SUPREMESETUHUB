from pydantic import BaseModel
class DigitalInfrastructureCategory(BaseModel):
 id:str
 name:str
 subcategories:list[str]
class DigitalInfrastructureListResponse(BaseModel):
 success:bool
 count:int
 categories:list[DigitalInfrastructureCategory]
class DigitalInfrastructureDetailResponse(BaseModel):
 success:bool
 category:DigitalInfrastructureCategory
