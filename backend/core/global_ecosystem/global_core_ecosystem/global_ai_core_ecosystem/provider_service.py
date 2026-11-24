"""Legacy API alias facade."""
from .catalog import get_ai_provider
class AIProviderCoreFacade:
 PROVIDER_ID=""
 def __init__(self):
  self._provider=get_ai_provider(self.PROVIDER_ID)
  if self._provider is None:raise LookupError("AI_PROVIDER_NOT_REGISTERED: "+self.PROVIDER_ID)
 def status(self):return {**self._provider,"facade_layer":"GLOBAL_AI_CORE_COMPATIBILITY_ALIAS","live_connection_verified":False,"inference_performed":False}
 def execute(self,*args,**kwargs):raise RuntimeError("USE_INJECTED_GLOBAL_AI_ENGINE_EXECUTOR")
