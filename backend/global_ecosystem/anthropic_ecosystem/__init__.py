"""Anthropic global ecosystem domain package.

Owns provider metadata, capability discovery, request planning, and domain-level
validation. API transport, CORE, ENGINE, DATABASE, credentials and authorization
enforcement remain in their separately owned architecture layers.
"""
from .catalog import ANTHROPIC_PROVIDER, ANTHROPIC_CAPABILITIES, get_capability
from .models import AnthropicCapability, AnthropicRequestPlan
from .service import AnthropicEcosystemService

__all__ = ["ANTHROPIC_PROVIDER", "ANTHROPIC_CAPABILITIES", "AnthropicCapability",
           "AnthropicRequestPlan", "AnthropicEcosystemService", "get_capability"]
