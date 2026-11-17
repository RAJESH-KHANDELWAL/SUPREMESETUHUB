"""DeepSeek CORE router; validation only."""
from .deepseek_chat_completions_core_ecosystem.contracts import validate_request as validate_chat_completions
from .deepseek_responses_core_ecosystem.contracts import validate_request as validate_responses
from .deepseek_search_core_ecosystem.contracts import validate_request as validate_search
from .deepseek_fetch_core_ecosystem.contracts import validate_request as validate_fetch
_VALIDATORS={"chat_completions":validate_chat_completions,"responses":validate_responses,"search":validate_search,"fetch":validate_fetch}
class DeepSeekCoreService:
    live_provider_calls_enabled=False
    def validate(self,capability,payload):
        if capability not in _VALIDATORS: raise ValueError("unknown DeepSeek capability")
        return {"provider":"deepseek",**_VALIDATORS[capability](payload)}
    def execute(self,*args,**kwargs): raise RuntimeError("LIVE_PROVIDER_CALLS_DISABLED: use approved API/ENGINE adapter")
