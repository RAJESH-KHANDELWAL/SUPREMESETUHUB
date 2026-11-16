"""AWS AI provider facade metadata."""
from ..catalog import get_ai_provider
PROVIDER_ID="aws"
PROVIDER=get_ai_provider(PROVIDER_ID)
