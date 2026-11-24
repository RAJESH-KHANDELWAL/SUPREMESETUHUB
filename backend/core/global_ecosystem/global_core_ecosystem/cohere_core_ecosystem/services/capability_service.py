from ..capabilities.catalog import CAPABILITIES
class CapabilityService:
    def get(self, name):
        return CAPABILITIES.get(name.strip().lower())
