"""
CORE Management Layer

Central management package for:
- Management
- Decisions
- Workflows

Management defines how approved work is organized and controlled.
Technical execution belongs to backend/engines.
"""

from .management import Management
from .decisions import DecisionManager
from .workflows import WorkflowManager

__all__ = [
    "Management",
    "DecisionManager",
    "WorkflowManager",
]
