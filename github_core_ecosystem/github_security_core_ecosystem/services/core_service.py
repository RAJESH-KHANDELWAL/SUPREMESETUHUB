from ..contracts import validate_request
class CoreService:
 live_calls_enabled=False
 def validate(self,payload): return validate_request(payload)
 def execute(self,*args,**kwargs): raise RuntimeError("LIVE_PROVIDER_CALLS_DISABLED: delegate to API/ENGINE layers")
