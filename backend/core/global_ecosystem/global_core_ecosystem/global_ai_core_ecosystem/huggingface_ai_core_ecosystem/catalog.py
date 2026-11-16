"""Hugging Face provider facade metadata."""
from ..catalog import get_ai_provider
PROVIDER_ID="huggingface"
PROVIDER=get_ai_provider(PROVIDER_ID)
