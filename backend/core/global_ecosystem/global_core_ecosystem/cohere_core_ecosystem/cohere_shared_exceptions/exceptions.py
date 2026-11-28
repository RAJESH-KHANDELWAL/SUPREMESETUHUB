"""Provider-wide CORE exception taxonomy."""
class CohereCoreError(Exception):
    """Base error for Cohere CORE contract and policy failures."""
class CapabilityNotRegisteredError(CohereCoreError):
    pass
class CapabilityValidationError(CohereCoreError):
    pass
