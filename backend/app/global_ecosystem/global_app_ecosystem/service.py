"""Independent GLOBAL APP service; owns composition metadata and lifecycle only."""
from .catalog import list_component_types,get_component_type
from .registry import AppComponentRegistry
from .component_registry import AppAdapterRegistry
from .lifecycle import AppLifecycle
from .runtime import runtime_status
class GlobalAppEcosystemService:
    domain="APP";ecosystem="GLOBAL_APP_ECOSYSTEM"
    def __init__(self,component_registry=None,adapter_registry=None,lifecycle=None,application_id="supremesetuhub"):
        self.registry=component_registry or AppComponentRegistry();self.adapters=adapter_registry or AppAdapterRegistry();self.lifecycle=lifecycle or AppLifecycle();self.application_id=str(application_id or "").strip()
        if not self.application_id:raise ValueError("application_id is required")
    def register_component(self,component,*,replace=False):return self.registry.register(component,replace=replace)
    def get_component(self,component_id):return self.registry.get(component_id)
    def list_components(self,*,component_type=None,enabled_only=False):return self.registry.list(component_type=component_type,enabled_only=enabled_only)
    def unregister_component(self,component_id):return self.registry.unregister(component_id)
    def register_adapter(self,component_id,adapter,*,replace=False):return self.adapters.register(component_id,adapter,replace=replace)
    def invoke_adapter(self,component_id,*args,**kwargs):
        adapter=self.adapters.get(component_id);component=self.registry.get(component_id)
        if adapter is None:raise RuntimeError(f"APP adapter is not configured: {component_id}")
        if component is None or not component.enabled:raise RuntimeError(f"APP component is missing or disabled: {component_id}")
        return adapter.invoke(*args,**kwargs)
    def transition(self,target):return self.lifecycle.transition(target)
    def health(self):
        components=self.registry.status();ids=self.adapters.list_ids()
        return {"domain":self.domain,"ecosystem":self.ecosystem,"status":"CONFIGURED" if components["registered_components"] else "NOT_CONFIGURED","application_id":self.application_id,"lifecycle":self.lifecycle.snapshot(),"components":components,"adapters":{"registered_adapter_count":len(ids),"adapter_ids":list(ids),"execution":"EXPLICIT_ONLY"},"runtime":runtime_status()}
    def describe(self):return {"domain":self.domain,"ecosystem":self.ecosystem,"application_id":self.application_id,"component_types":list_component_types(),"component_count":self.registry.count(),"framework_dependency":None,"automatic_startup":False,"automatic_component_loading":False,"lifecycle_state":self.lifecycle.state}
    def list_component_types(self):return list_component_types()
    def get_component_type(self,type_id):return get_component_type(type_id)
EcosystemService=GlobalAppEcosystemService
__all__=["GlobalAppEcosystemService","EcosystemService"]
