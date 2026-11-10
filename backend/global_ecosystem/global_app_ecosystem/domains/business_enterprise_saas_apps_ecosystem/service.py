"""Executable workflow service for this application domain."""
from ..domain_runtime import create_domain_service

DOMAIN_ID = __name__.rsplit(".", 2)[-2].removesuffix("_ecosystem")
service = create_domain_service(DOMAIN_ID)

def inspect():
    """Return domain metadata and supported actions."""
    return service.inspect()

def validate(payload):
    """Validate a workflow without external side effects."""
    return service.validate(payload)

def plan(payload):
    """Create a validated implementation plan; no provider is called."""
    return service.plan(payload)

__all__ = ["DOMAIN_ID", "service", "inspect", "validate", "plan"]
