from .catalog import get_module
from .policy import redact_metadata
class IndividualModuleService:
    def get(self,module_id):
        item=get_module(module_id)
        return redact_metadata(item) if item else None
