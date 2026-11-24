from ..contracts import validate_request
class CoreService:
    def validate(self,payload): return validate_request(payload)
    def execute(self,*args,**kwargs): raise RuntimeError("LIVE_PROVIDER_CALLS_DISABLED")
