from dataclasses import dataclass
@dataclass(frozen=True)
class IndividualModule:
    module_id:str
    directory:str
    name:str
    status:str="CORE_CATALOG_ONLY"
    connected:bool=False
