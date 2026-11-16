"""Provider execution boundary for AWS CLOUDFORMATION; no API/CORE dependency."""
from typing import Any
class ProviderEngine:
    provider="AWS CLOUDFORMATION"
    layer="ENGINE"
    def __init__(self,handler=None): self._handler=handler
    def health(self): return {"provider":self.provider,"layer":self.layer,"status":"READY" if callable(self._handler) else "NOT_CONFIGURED"}
    def execute(self,operation:str,payload:dict[str,Any]|None=None):
        if not callable(self._handler): raise NotImplementedError(self.provider+" engine handler is not configured")
        return self._handler(operation,dict(payload or {}))
