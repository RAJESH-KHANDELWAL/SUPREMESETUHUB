"""Shared provider adapter contracts and factory."""
from .contracts import ChatMessage, ChatRequest, ChatResponse, ProviderAdapter
from .factory import create_chat_adapter, list_chat_adapter_provider_ids

__all__ = [
    "ChatMessage", "ChatRequest", "ChatResponse", "ProviderAdapter",
    "create_chat_adapter", "list_chat_adapter_provider_ids",
]
