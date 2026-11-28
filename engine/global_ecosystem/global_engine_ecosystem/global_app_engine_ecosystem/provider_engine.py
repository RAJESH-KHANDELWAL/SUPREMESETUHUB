"""Provider execution boundary for GLOBAL APP.

A handler must be explicitly injected by a provider integration. Catalog entries
alone never create network calls or imply that an app is connected.
"""
from typing import Any,Callable
class AppProviderEngine:
 def __init__(self,provider_id:str,handler:Callable[[str,dict[str,Any]],Any]|None=None):
  self.provider_id=str(provider_id or "").strip()
  if not self.provider_id: raise ValueError("provider_id is required")
  self._handler=handler
 def status(self):
  return {"layer":"ENGINE","provider_id":self.provider_id,"status":"CONFIGURED" if callable(self._handler) else "NOT_CONFIGURED","live_connection_verified":False,"execution":"EXPLICIT_HANDLER_ONLY"}
 def execute(self,operation:str,payload:dict[str,Any]|None=None):
  if not callable(self._handler): raise RuntimeError(f"APP provider handler is not configured: {self.provider_id}")
  if not str(operation or "").strip(): raise ValueError("operation is required")
  result=self._handler(operation,dict(payload or {}))
  return {"provider_id":self.provider_id,"operation":operation,"result":result}
