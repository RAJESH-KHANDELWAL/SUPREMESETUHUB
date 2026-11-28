"""DeepSeek chat_completions CORE package."""
from .contracts import validate_request
from .service import CoreService
__all__=["validate_request","CoreService"]
