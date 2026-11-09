from pydantic import BaseModel
class FoodHospitalityCategory(BaseModel):
 id:str
 name:str
 subcategories:list[str]
class FoodHospitalityListResponse(BaseModel):
 success:bool
 count:int
 categories:list[FoodHospitalityCategory]
class FoodHospitalityDetailResponse(BaseModel):
 success:bool
 category:FoodHospitalityCategory
