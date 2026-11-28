"""Planner and Tasks service-family metadata; catalog scaffold, not a live connector."""
from __future__ import annotations

SERVICE_ECOSYSTEM = {
    "provider_id": "microsoft",
    "service_id": "microsoft_planner_tasks_api",
    "name": "PLANNER AND TASKS API ECOSYSTEM",
    "scope": "Planner plans, buckets, tasks, assignments, and task details.",
    "authentication_setup": "Graph Tasks.* permissions and tenant licensing/availability.",
    "documentation_required": True,
    "adapter_implemented": False,
    "live_connection_verified": False,
    "credential_persistence_implemented": False,
}

__all__ = ["SERVICE_ECOSYSTEM"]
