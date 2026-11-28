"""APP-owned catalog of application composition component types."""
from dataclasses import dataclass
@dataclass(frozen=True)
class AppComponentType:
    type_id: str
    display_name: str
    responsibility: str
    execution_owner: str = "APP_COMPOSITION_ROOT"
_TYPES=(AppComponentType("api-router","API Router","Router registration metadata; implementation belongs to API."),AppComponentType("middleware","Middleware","Application-level middleware registration and ordering."),AppComponentType("exception-handler","Exception Handler","Application exception-handler registration metadata."),AppComponentType("startup-hook","Startup Hook","Explicit startup callback registration."),AppComponentType("shutdown-hook","Shutdown Hook","Explicit shutdown callback registration."),AppComponentType("background-worker","Background Worker","Worker lifecycle registration; execution belongs to its owner."),AppComponentType("extension","Application Extension","Optional application extension registration metadata."))
def list_component_types():
    return [{"type_id":x.type_id,"display_name":x.display_name,"responsibility":x.responsibility,"execution_owner":x.execution_owner} for x in _TYPES]
def get_component_type(type_id):
    key=str(type_id or "").strip().lower().replace("_","-").replace(" ","-")
    for x in _TYPES:
        if x.type_id==key:return {"type_id":x.type_id,"display_name":x.display_name,"responsibility":x.responsibility,"execution_owner":x.execution_owner}
    raise KeyError(f"Unknown APP component type: {type_id}")
__all__=["AppComponentType","list_component_types","get_component_type"]
