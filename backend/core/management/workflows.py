"""
CORE Workflow Management

Defines how approved work moves through a controlled workflow.

CORE manages the workflow state.
Actual technical execution belongs to backend/engines.
"""

from typing import Any, Dict, List


class WorkflowManager:
    """
    Central workflow-management controller.
    """

    VALID_STATUSES = [
        "PENDING",
        "APPROVED",
        "QUEUED",
        "RUNNING",
        "PAUSED",
        "COMPLETED",
        "FAILED",
        "CANCELLED",
    ]

    def __init__(self) -> None:
        self.workflows: Dict[str, Dict[str, Any]] = {}

    def create_workflow(
        self,
        workflow_id: str,
        name: str,
        created_by: str = "SYSTEM",
        description: str = "",
    ) -> None:
        """Create a new workflow."""

        key = workflow_id.strip()

        if not key:
            raise ValueError("workflow_id cannot be empty")

        if not name.strip():
            raise ValueError("name cannot be empty")

        self.workflows[key] = {
            "workflow_id": key,
            "name": name.strip(),
            "description": description.strip(),
            "created_by": created_by.strip(),
            "status": "PENDING",
            "assigned_to": None,
            "engine": None,
            "steps": [],
        }

    def add_step(
        self,
        workflow_id: str,
        step_name: str,
        step_type: str = "TASK",
    ) -> bool:
        """Add a step to an existing workflow."""

        key = workflow_id.strip()

        if key not in self.workflows:
            return False

        if not step_name.strip():
            raise ValueError("step_name cannot be empty")

        self.workflows[key]["steps"].append(
            {
                "step_name": step_name.strip(),
                "step_type": step_type.strip().upper(),
                "status": "PENDING",
            }
        )

        return True

    def assign(
        self,
        workflow_id: str,
        assigned_to: str,
    ) -> bool:
        """Assign a workflow to an identity, team or role."""

        key = workflow_id.strip()

        if key not in self.workflows:
            return False

        if not assigned_to.strip():
            raise ValueError("assigned_to cannot be empty")

        self.workflows[key]["assigned_to"] = assigned_to.strip()
        return True

    def attach_engine(
        self,
        workflow_id: str,
        engine_name: str,
    ) -> bool:
        """
        Connect a workflow to an execution engine.

        This does not execute the engine.
        """

        key = workflow_id.strip()

        if key not in self.workflows:
            return False

        if not engine_name.strip():
            raise ValueError("engine_name cannot be empty")

        self.workflows[key]["engine"] = engine_name.strip()
        return True

    def update_status(
        self,
        workflow_id: str,
        status: str,
    ) -> bool:
        """Update workflow status."""

        key = workflow_id.strip()
        normalized_status = status.strip().upper()

        if key not in self.workflows:
            return False

        if normalized_status not in self.VALID_STATUSES:
            raise ValueError(
                f"Invalid workflow status: {status}"
            )

        self.workflows[key]["status"] = normalized_status
        return True

    def get_workflow(
        self,
        workflow_id: str,
    ) -> Dict[str, Any] | None:
        """Return a workflow."""

        return self.workflows.get(workflow_id.strip())

    def list_workflows(self) -> List[Dict[str, Any]]:
        """Return all workflows."""

        return list(self.workflows.values())

    def list_by_status(
        self,
        status: str,
    ) -> List[Dict[str, Any]]:
        """Return workflows filtered by status."""

        normalized_status = status.strip().upper()

        if normalized_status not in self.VALID_STATUSES:
            raise ValueError(
                f"Invalid workflow status: {status}"
            )

        return [
            workflow
            for workflow in self.workflows.values()
            if workflow["status"] == normalized_status
        ]

    def count(self) -> int:
        """Return total workflow count."""

        return len(self.workflows)
