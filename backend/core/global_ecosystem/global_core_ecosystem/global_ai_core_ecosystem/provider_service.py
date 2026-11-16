"""Read-only facade over canonical provider CORE packages."""
from .catalog import get_ai_provider
class AIProviderCoreFacade:
 PROVIDER_ID=""
 def __init__(self):
  if not self.PROVIDER_ID: raise NotImplementedError("PROVIDER_ID_REQUIRED")
  self._provider=get_ai_provider(self.PROVIDER_ID)
  if self._provider is None: raise LookupError("AI_PROVIDER_NOT_REGISTERED")
 def status(self): return {**self._provider,"facade_layer":"GLOBAL_AI_CORE","provider_core_delegated":True,"live_connection_verified":False,"inference_performed":False}
 def execute(self,*args,**kwargs): raise RuntimeError("AI_EXECUTION_REQUIRES_INJECTED_GLOBAL_AI_EXECUTOR")
