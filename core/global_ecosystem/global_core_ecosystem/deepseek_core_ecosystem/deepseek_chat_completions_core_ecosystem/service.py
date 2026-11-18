"""Validation-only service facade."""
from .contracts import validate_request
class CoreService:
    live_calls_enabled=False
    endpoint="POST /chat/completions"
    def validate(self,payload): return validate_request(payload)
    def execute(self,*args,**kwargs): raise RuntimeError("LIVE_PROVIDER_CALLS_DISABLED")
