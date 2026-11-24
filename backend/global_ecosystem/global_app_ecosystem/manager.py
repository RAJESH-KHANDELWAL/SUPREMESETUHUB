"""Management facade for the independent GLOBAL APP ecosystem."""
from .service import GlobalAppEcosystemService
class GlobalAppEcosystemManager:
    def __init__(self,service=None):self.service=service or GlobalAppEcosystemService()
    def register_component(self,component,*,replace=False):return self.service.register_component(component,replace=replace)
    def get_component(self,component_id):return self.service.get_component(component_id)
    def list_components(self,**kwargs):return self.service.list_components(**kwargs)
    def unregister_component(self,component_id):return self.service.unregister_component(component_id)
    def register_adapter(self,component_id,adapter,*,replace=False):return self.service.register_adapter(component_id,adapter,replace=replace)
    def invoke_adapter(self,component_id,*args,**kwargs):return self.service.invoke_adapter(component_id,*args,**kwargs)
    def transition(self,target):return self.service.transition(target)
    def health(self):return self.service.health()
    def describe(self):return self.service.describe()
__all__=["GlobalAppEcosystemManager"]
