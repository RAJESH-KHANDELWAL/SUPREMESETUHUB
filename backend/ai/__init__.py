"""AI domain layer for SUPREMESETUHUB.

Provider execution and dispatch are owned by backend.engine.ai.
"""

from backend.ai.capabilities import AICapability
from backend.ai.contracts import AIRequest, AIResult

__all__ = ["AICapability", "AIRequest", "AIResult"]
