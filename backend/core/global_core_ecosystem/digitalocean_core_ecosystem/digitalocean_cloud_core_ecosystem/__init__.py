"""DigitalOcean Cloud CORE contract package."""
from .contracts import validate_request
from .service import CoreService
__all__=["validate_request","CoreService"]
