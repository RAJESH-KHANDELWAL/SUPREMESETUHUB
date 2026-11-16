from dataclasses import dataclass
@dataclass(frozen=True)
class ProductDescriptor:
 product_id:str
 name:str
 category:str
 api_name:str|None
 availability:str
