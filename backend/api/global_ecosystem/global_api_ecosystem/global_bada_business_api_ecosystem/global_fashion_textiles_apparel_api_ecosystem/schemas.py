from pydantic import BaseModel
class FashionTextilesCategory(BaseModel):
 id:str
 name:str
 subcategories:list[str]
class FashionTextilesListResponse(BaseModel):
 success:bool
 count:int
 categories:list[FashionTextilesCategory]
class FashionTextilesDetailResponse(BaseModel):
 success:bool
 category:FashionTextilesCategory
