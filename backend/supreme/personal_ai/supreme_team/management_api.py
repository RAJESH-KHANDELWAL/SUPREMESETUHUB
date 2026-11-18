"""Authenticated HTTP API for SUPREME Team management."""
from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field

from .auth_adapter import get_team_actor
from .management import Actor, SupremeTeamManagement

router = APIRouter(
    prefix="/team-management",
    tags=["SUPREME TEAM MANAGEMENT"],
)
service = SupremeTeamManagement()


class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=240)
    description: str = Field(min_length=1, max_length=10000)
    department: str = Field(min_length=1, max_length=120)
    assigned_to: str = Field(min_length=1, max_length=160)
    assigned_role: str
    due_at: str | None = None


class TaskStatusUpdate(BaseModel):
    status: str
    evidence: list[str] = Field(default_factory=list)


class ProtectedChangeProposal(BaseModel):
    action: str
    resource: str = Field(min_length=1, max_length=1000)
    before_state: dict
    proposed_state: dict
    reason: str = Field(min_length=1, max_length=5000)
    impact: str = Field(min_length=1, max_length=5000)
    rollback_plan: str = Field(min_length=1, max_length=5000)


class OwnerDecision(BaseModel):
    approve: bool
    decision_note: str = Field(min_length=1, max_length=5000)


class ExecutionRecord(BaseModel):
    evidence: str = Field(min_length=1, max_length=5000)
    executed_resource_state: dict


class DailyReportSubmission(BaseModel):
    report_date: str
    department: str
    report: dict


def _run(call, *args, **kwargs):
    try:
        return call(*args, **kwargs)
    except PermissionError as exc:
        raise HTTPException(status_code=403, detail=str(exc)) from exc
    except LookupError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc


@router.get("/status")
def status(actor: Actor = Depends(get_team_actor)):
    return _run(service.management_status, actor)


@router.post("/tasks")
def create_task(payload: TaskCreate, actor: Actor = Depends(get_team_actor)):
    return _run(
        service.create_task, actor,
        title=payload.title, description=payload.description,
        department=payload.department, assigned_to=payload.assigned_to,
        assigned_role=payload.assigned_role, due_at=payload.due_at,
    )


@router.get("/tasks")
def list_tasks(status: str | None = None, department: str | None = None,
               actor: Actor = Depends(get_team_actor)):
    return _run(service.list_tasks, actor, status=status, department=department)


@router.get("/tasks/{task_id}")
def get_task(task_id: str, actor: Actor = Depends(get_team_actor)):
    return _run(service.get_task, actor, task_id)


@router.patch("/tasks/{task_id}/status")
def update_task(task_id: str, payload: TaskStatusUpdate,
                actor: Actor = Depends(get_team_actor)):
    return _run(
        service.update_task_status, actor, task_id,
        status=payload.status, evidence=payload.evidence,
    )


@router.post("/change-proposals")
def propose_change(payload: ProtectedChangeProposal,
                   actor: Actor = Depends(get_team_actor)):
    return _run(
        service.propose_protected_change, actor,
        action=payload.action, resource=payload.resource,
        before_state=payload.before_state,
        proposed_state=payload.proposed_state,
        reason=payload.reason, impact=payload.impact,
        rollback_plan=payload.rollback_plan,
    )


@router.get("/change-proposals/{proposal_id}")
def get_proposal(proposal_id: str, actor: Actor = Depends(get_team_actor)):
    return _run(service.get_proposal, actor, proposal_id)


@router.post("/change-proposals/{proposal_id}/owner-decision")
def decide_proposal(proposal_id: str, payload: OwnerDecision,
                    actor: Actor = Depends(get_team_actor)):
    return _run(
        service.decide_proposal, actor, proposal_id,
        approve=payload.approve, decision_note=payload.decision_note,
    )


@router.post("/change-proposals/{proposal_id}/execution-record")
def record_execution(proposal_id: str, payload: ExecutionRecord,
                     actor: Actor = Depends(get_team_actor)):
    return _run(
        service.record_execution, actor, proposal_id,
        evidence=payload.evidence,
        executed_resource_state=payload.executed_resource_state,
    )


@router.post("/daily-reports")
def submit_daily_report(payload: DailyReportSubmission,
                        actor: Actor = Depends(get_team_actor)):
    return _run(
        service.submit_daily_report, actor,
        report_date=payload.report_date, department=payload.department,
        report=payload.report,
    )


@router.get("/daily-reports")
def list_daily_reports(report_date: str | None = None,
                       actor: Actor = Depends(get_team_actor)):
    return _run(service.list_daily_reports, actor, report_date=report_date)


@router.get("/daily-reports/consolidated")
def consolidated_daily_report(report_date: str,
                              actor: Actor = Depends(get_team_actor)):
    return _run(service.consolidated_daily_report, actor, report_date=report_date)


@router.get("/audit")
def audit_log(resource_id: str | None = None,
              actor: Actor = Depends(get_team_actor)):
    return _run(service.audit_log, actor, resource_id=resource_id)
