"""APP-owned framework-neutral value objects."""
from dataclasses import dataclass,field
from typing import Any
@dataclass(frozen=True)
class AppComponent:
    component_id:str
    name:str
    component_type:str
    enabled:bool=True
    version:str="1.0.0"
    metadata:dict[str,Any]=field(default_factory=dict)
    def __post_init__(self):
        for key in ("component_id","name","component_type","version"):
            value=str(getattr(self,key) or "").strip()
            if not value:raise ValueError(f"{key} is required")
            object.__setattr__(self,key,value)
        object.__setattr__(self,"component_type",self.component_type.lower().replace("_","-"))
        if not isinstance(self.enabled,bool):raise TypeError("enabled must be a boolean")
        if not isinstance(self.metadata,dict):raise TypeError("metadata must be a dictionary")
        object.__setattr__(self,"metadata",dict(self.metadata))
__all__=["AppComponent"]
