"""SUPREME Team management domain service.

This service persists tasks, approval requests, audit events and daily reports.
It deliberately does not execute GitHub/file-system mutations. Protected changes
must be carried out by a separately authenticated executor after Owner approval.
Callers must pass an actor identity established by the authentication layer;
never construct Actor from an untrusted request-body role field.
"""
from __future__ import annotations

import hashlib
import json
import uuid
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any

from backend.database import DatabaseService


OWNER = "OWNER"
ROLE_ORDER = {
    "OWNER": 0,
    "CMD": 1,
    "MD": 2,
    "DIRECTOR": 3,
    "DEPARTMENT_HEAD": 4,
    "EXECUTIVE": 5,
    "MANAGER": 6,
    "TEAM_LEADER": 7,
    "TEAM_MEMBER": 8,
}
PROTECTED_ACTIONS = {
    "RENAME", "MOVE", "DELETE", "OVERWRITE", "MERGE",
    "DEPLOY", "DATABASE_MIGRATION", "ACCESS_CHANGE",
    "ROLE_CHANGE", "FINANCIAL_COMMITMENT", "CREDENTIAL_CHANGE",
}


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


@dataclass(frozen=True)
class Actor:
    """Authenticated principal supplied by a trusted authentication adapter."""

    actor_id: str
    role: str
    authenticated: bool = False

    def validate(self) -> None:
        if not self.authenticated:
            raise PermissionError("AUTHENTICATED_ACTOR_REQUIRED")
        if not self.actor_id or not self.actor_id.strip():
            raise ValueError("ACTOR_ID_REQUIRED")
        if self.role not in ROLE_ORDER:
            raise PermissionError("UNKNOWN_SUPREME_TEAM_ROLE")


class SupremeTeamManagement:
    """Persistent task, approval, audit and daily-report coordinator."""

    def __init__(self, database: DatabaseService | None = None) -> None:
        self.database = database or DatabaseService()
        self._initialize_schema()

    def _initialize_schema(self) -> None:
        statements = (
            """CREATE TABLE IF NOT EXISTS supreme_team_tasks (
                task_id TEXT PRIMARY KEY, title TEXT NOT NULL,
                description TEXT NOT NULL, department TEXT NOT NULL,
                assigned_to TEXT NOT NULL, assigned_role TEXT NOT NULL,
                created_by TEXT NOT NULL, status TEXT NOT NULL,
                due_at TEXT, evidence TEXT NOT NULL DEFAULT '[]',
                created_at TEXT NOT NULL, updated_at TEXT NOT NULL
            )""",
            """CREATE TABLE IF NOT EXISTS supreme_team_change_proposals (
                proposal_id TEXT PRIMARY KEY, action TEXT NOT NULL,
                resource TEXT NOT NULL, before_state TEXT NOT NULL,
                proposed_state TEXT NOT NULL, reason TEXT NOT NULL,
                impact TEXT NOT NULL, rollback_plan TEXT NOT NULL,
                requested_by TEXT NOT NULL, status TEXT NOT NULL,
                proposal_hash TEXT NOT NULL, approved_by TEXT,
                approved_at TEXT, execution_evidence TEXT,
                created_at TEXT NOT NULL, updated_at TEXT NOT NULL
            )""",
            """CREATE TABLE IF NOT EXISTS supreme_team_audit_events (
                event_id TEXT PRIMARY KEY, actor_id TEXT NOT NULL,
                actor_role TEXT NOT NULL, event_type TEXT NOT NULL,
                resource_type TEXT NOT NULL, resource_id TEXT NOT NULL,
                details TEXT NOT NULL, created_at TEXT NOT NULL
            )""",
            """CREATE TABLE IF NOT EXISTS supreme_team_daily_reports (
                report_id TEXT PRIMARY KEY, report_date TEXT NOT NULL,
                submitted_by TEXT NOT NULL, submitted_role TEXT NOT NULL,
                department TEXT NOT NULL, report TEXT NOT NULL,
                status TEXT NOT NULL, created_at TEXT NOT NULL
            )""",
        )
        for statement in statements:
            self.database.execute(statement)

    def _actor(self, actor: Actor) -> None:
        if not isinstance(actor, Actor):
            raise PermissionError("TRUSTED_ACTOR_CONTEXT_REQUIRED")
        actor.validate()

    def _audit(
        self, actor: Actor, event_type: str, resource_type: str,
        resource_id: str, details: dict[str, Any],
    ) -> None:
        self.database.execute(
            """INSERT INTO supreme_team_audit_events
            (event_id, actor_id, actor_role, event_type, resource_type,
             resource_id, details, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
            (str(uuid.uuid4()), actor.actor_id, actor.role, event_type,
             resource_type, resource_id, _json(details), _now()),
        )

    def create_task(
        self, actor: Actor, *, title: str, description: str,
        department: str, assigned_to: str, assigned_role: str,
        due_at: str | None = None,
    ) -> dict[str, Any]:
        self._actor(actor)
        if not all(isinstance(v, str) and v.strip() for v in
                   (title, description, department, assigned_to, assigned_role)):
            raise ValueError("TASK_REQUIRED_FIELDS_MISSING")
        if assigned_role not in ROLE_ORDER:
            raise ValueError("UNKNOWN_ASSIGNED_ROLE")
        if ROLE_ORDER[assigned_role] < ROLE_ORDER[actor.role] and actor.role != OWNER:
            raise PermissionError("CANNOT_ASSIGN_ABOVE_OWN_ROLE")
        task_id, now = str(uuid.uuid4()), _now()
        self.database.execute(
            """INSERT INTO supreme_team_tasks
            (task_id,title,description,department,assigned_to,assigned_role,
             created_by,status,due_at,evidence,created_at,updated_at)
            VALUES (?,?,?,?,?,?,?,'OPEN',?,'[]',?,?)""",
            (task_id,title.strip(),description.strip(),department.strip(),
             assigned_to.strip(),assigned_role,actor.actor_id,due_at,now,now),
        )
        self._audit(actor,"TASK_CREATED","TASK",task_id,{"title":title,"department":department})
        return self.get_task(actor, task_id)

    def list_tasks(
        self, actor: Actor, *, status: str | None = None,
        department: str | None = None,
    ) -> list[dict[str, Any]]:
        self._actor(actor)
        query = "SELECT * FROM supreme_team_tasks"
        clauses: list[str] = []
        parameters: list[Any] = []
        if actor.role not in {OWNER, "CMD"}:
            clauses.append("(assigned_to = ? OR created_by = ?)")
            parameters.extend([actor.actor_id, actor.actor_id])
        if status:
            clauses.append("status = ?")
            parameters.append(status)
        if department:
            clauses.append("department = ?")
            parameters.append(department)
        if clauses:
            query += " WHERE " + " AND ".join(clauses)
        query += " ORDER BY created_at DESC"
        rows = self.database.fetchall(query, parameters)
        result = []
        for row in rows:
            item = dict(row)
            item["evidence"] = json.loads(item["evidence"])
            result.append(item)
        return result

    def get_task(self, actor: Actor, task_id: str) -> dict[str, Any]:
        self._actor(actor)
        row = self.database.fetchone(
            "SELECT * FROM supreme_team_tasks WHERE task_id = ?", (task_id,)
        )
        if row is None:
            raise LookupError("TASK_NOT_FOUND")
        if actor.role != OWNER and actor.role != "CMD" and row["assigned_to"] != actor.actor_id and row["created_by"] != actor.actor_id:
            raise PermissionError("TASK_ACCESS_DENIED")
        result = dict(row)
        result["evidence"] = json.loads(result["evidence"])
        return result

    def update_task_status(
        self, actor: Actor, task_id: str, *, status: str,
        evidence: list[str] | None = None,
    ) -> dict[str, Any]:
        self._actor(actor)
        allowed = {"OPEN", "IN_PROGRESS", "BLOCKED", "COMPLETED", "CANCELLED"}
        if status not in allowed:
            raise ValueError("INVALID_TASK_STATUS")
        task = self.get_task(actor, task_id)
        if actor.role not in {OWNER, "CMD"} and task["assigned_to"] != actor.actor_id:
            raise PermissionError("TASK_UPDATE_DENIED")
        if status == "COMPLETED" and not evidence:
            raise ValueError("COMPLETION_EVIDENCE_REQUIRED")
        evidence = evidence or []
        if not all(isinstance(item, str) and item.strip() for item in evidence):
            raise ValueError("INVALID_TASK_EVIDENCE")
        self.database.execute(
            "UPDATE supreme_team_tasks SET status=?, evidence=?, updated_at=? WHERE task_id=?",
            (status,_json(evidence),_now(),task_id),
        )
        self._audit(actor,"TASK_STATUS_UPDATED","TASK",task_id,{"status":status,"evidence":evidence})
        return self.get_task(actor, task_id)

    def propose_protected_change(
        self, actor: Actor, *, action: str, resource: str,
        before_state: Any, proposed_state: Any, reason: str,
        impact: str, rollback_plan: str,
    ) -> dict[str, Any]:
        self._actor(actor)
        action = action.strip().upper()
        if action not in PROTECTED_ACTIONS:
            raise ValueError("ACTION_NOT_IN_PROTECTED_CHANGE_CATALOG")
        if not all(isinstance(v, str) and v.strip() for v in
                   (resource, reason, impact, rollback_plan)):
            raise ValueError("CHANGE_PROPOSAL_DETAILS_REQUIRED")
        payload = {
            "action": action, "resource": resource,
            "before_state": before_state, "proposed_state": proposed_state,
            "reason": reason, "impact": impact, "rollback_plan": rollback_plan,
        }
        digest = hashlib.sha256(_json(payload).encode("utf-8")).hexdigest()
        proposal_id, now = str(uuid.uuid4()), _now()
        self.database.execute(
            """INSERT INTO supreme_team_change_proposals
            (proposal_id,action,resource,before_state,proposed_state,reason,
             impact,rollback_plan,requested_by,status,proposal_hash,created_at,updated_at)
            VALUES (?,?,?,?,?,?,?,?,?,'PENDING_OWNER_APPROVAL',?,?,?)""",
            (proposal_id,action,resource,_json(before_state),_json(proposed_state),
             reason,impact,rollback_plan,actor.actor_id,digest,now,now),
        )
        self._audit(actor,"PROTECTED_CHANGE_PROPOSED","CHANGE_PROPOSAL",proposal_id,payload)
        return self.get_proposal(actor, proposal_id)

    def get_proposal(self, actor: Actor, proposal_id: str) -> dict[str, Any]:
        self._actor(actor)
        row = self.database.fetchone(
            "SELECT * FROM supreme_team_change_proposals WHERE proposal_id = ?",
            (proposal_id,),
        )
        if row is None:
            raise LookupError("CHANGE_PROPOSAL_NOT_FOUND")
        if actor.role != OWNER and actor.role != "CMD" and row["requested_by"] != actor.actor_id:
            raise PermissionError("CHANGE_PROPOSAL_ACCESS_DENIED")
        result = dict(row)
        for key in ("before_state", "proposed_state"):
            result[key] = json.loads(result[key])
        return result

    def decide_proposal(
        self, actor: Actor, proposal_id: str, *, approve: bool,
        decision_note: str,
    ) -> dict[str, Any]:
        self._actor(actor)
        if actor.role != OWNER:
            raise PermissionError("SUPREME_OWNER_APPROVAL_REQUIRED")
        if not isinstance(approve, bool) or not decision_note.strip():
            raise ValueError("EXPLICIT_OWNER_DECISION_AND_NOTE_REQUIRED")
        proposal = self.get_proposal(actor, proposal_id)
        if proposal["status"] != "PENDING_OWNER_APPROVAL":
            raise ValueError("PROPOSAL_NOT_PENDING")
        status = "APPROVED" if approve else "REJECTED"
        now = _now()
        self.database.execute(
            """UPDATE supreme_team_change_proposals
            SET status=?, approved_by=?, approved_at=?, updated_at=?
            WHERE proposal_id=? AND status='PENDING_OWNER_APPROVAL'""",
            (status,actor.actor_id,now,now,proposal_id),
        )
        self._audit(actor,"OWNER_"+status,"CHANGE_PROPOSAL",proposal_id,
                    {"decision_note":decision_note,"proposal_hash":proposal["proposal_hash"]})
        return self.get_proposal(actor, proposal_id)

    def record_execution(
        self, actor: Actor, proposal_id: str, *, evidence: str,
        executed_resource_state: Any,
    ) -> dict[str, Any]:
        """Record an externally executed change; this method does not execute it."""
        self._actor(actor)
        if actor.role not in {OWNER, "CMD"}:
            raise PermissionError("CMD_OR_OWNER_EXECUTION_RECORDING_REQUIRED")
        if not evidence.strip():
            raise ValueError("EXECUTION_EVIDENCE_REQUIRED")
        proposal = self.get_proposal(actor, proposal_id)
        if proposal["status"] != "APPROVED":
            raise PermissionError("OWNER_APPROVED_PROPOSAL_REQUIRED")
        if _json(executed_resource_state) != _json(proposal["proposed_state"]):
            raise ValueError("EXECUTED_STATE_DOES_NOT_MATCH_APPROVED_PROPOSAL")
        now = _now()
        self.database.execute(
            """UPDATE supreme_team_change_proposals
            SET status='EXECUTED_RECORDED', execution_evidence=?, updated_at=?
            WHERE proposal_id=? AND status='APPROVED'""",
            (evidence,now,proposal_id),
        )
        self._audit(actor,"PROTECTED_CHANGE_EXECUTION_RECORDED","CHANGE_PROPOSAL",
                    proposal_id,{"evidence":evidence,"state":executed_resource_state})
        return self.get_proposal(actor, proposal_id)

    def submit_daily_report(
        self, actor: Actor, *, report_date: str, department: str,
        report: dict[str, Any],
    ) -> dict[str, Any]:
        self._actor(actor)
        if not report_date.strip() or not department.strip() or not isinstance(report, dict):
            raise ValueError("DAILY_REPORT_FIELDS_REQUIRED")
        required = {"summary","completed","in_progress","blocked","risks",
                    "decisions_required","tomorrow_plan","verified_changes"}
        missing = sorted(required - set(report))
        if missing:
            raise ValueError("DAILY_REPORT_SECTIONS_MISSING:" + ",".join(missing))
        report_id, now = str(uuid.uuid4()), _now()
        self.database.execute(
            """INSERT INTO supreme_team_daily_reports
            (report_id,report_date,submitted_by,submitted_role,department,report,status,created_at)
            VALUES (?,?,?,?,?,?,'SUBMITTED',?)""",
            (report_id,report_date,actor.actor_id,actor.role,department,_json(report),now),
        )
        self._audit(actor,"DAILY_REPORT_SUBMITTED","DAILY_REPORT",report_id,
                    {"report_date":report_date,"department":department})
        return {"report_id":report_id,"report_date":report_date,
                "submitted_by":actor.actor_id,"role":actor.role,
                "department":department,"status":"SUBMITTED","created_at":now}

    def list_daily_reports(
        self, actor: Actor, *, report_date: str | None = None,
    ) -> list[dict[str, Any]]:
        self._actor(actor)
        if actor.role not in {OWNER, "CMD"}:
            raise PermissionError("CMD_OR_OWNER_REPORT_ACCESS_REQUIRED")
        if report_date:
            rows = self.database.fetchall(
                "SELECT * FROM supreme_team_daily_reports WHERE report_date=? ORDER BY created_at",
                (report_date,),
            )
        else:
            rows = self.database.fetchall(
                "SELECT * FROM supreme_team_daily_reports ORDER BY created_at DESC"
            )
        reports = []
        for row in rows:
            item = dict(row)
            item["report"] = json.loads(item["report"])
            reports.append(item)
        return reports

    def consolidated_daily_report(
        self, actor: Actor, *, report_date: str,
    ) -> dict[str, Any]:
        """Consolidate department submissions without inventing missing data."""
        self._actor(actor)
        if actor.role not in {OWNER, "CMD"}:
            raise PermissionError("CMD_OR_OWNER_REPORT_ACCESS_REQUIRED")
        if not report_date or not report_date.strip():
            raise ValueError("REPORT_DATE_REQUIRED")
        rows = self.database.fetchall(
            """SELECT * FROM supreme_team_daily_reports
            WHERE report_date = ? ORDER BY department, created_at""",
            (report_date,),
        )
        submissions = []
        for row in rows:
            item = dict(row)
            item["report"] = json.loads(item["report"])
            submissions.append(item)
        changes = []
        blockers = []
        risks = []
        decisions = []
        completed = []
        in_progress = []
        for item in submissions:
            report = item["report"]
            for key, target in (
                ("verified_changes", changes),
                ("blocked", blockers),
                ("risks", risks),
                ("decisions_required", decisions),
                ("completed", completed),
                ("in_progress", in_progress),
            ):
                values = report.get(key, [])
                if isinstance(values, list):
                    target.extend({
                        "department": item["department"],
                        "submitted_by": item["submitted_by"],
                        "item": value,
                    } for value in values)
        return {
            "report_date": report_date,
            "status": "CONSOLIDATED" if submissions else "NO_SUBMISSIONS",
            "submission_count": len(submissions),
            "departments_submitted": sorted({item["department"] for item in submissions}),
            "submissions": submissions,
            "completed": completed,
            "in_progress": in_progress,
            "blockers": blockers,
            "risks": risks,
            "owner_decisions_required": decisions,
            "verified_changes": changes,
            "missing_data_policy": "No department submission or evidence is fabricated; missing sections remain visible in source submissions.",
        }

    def audit_log(
        self, actor: Actor, *, resource_id: str | None = None,
    ) -> list[dict[str, Any]]:
        self._actor(actor)
        if actor.role != OWNER:
            raise PermissionError("SUPREME_OWNER_AUDIT_ACCESS_REQUIRED")
        if resource_id:
            rows = self.database.fetchall(
                "SELECT * FROM supreme_team_audit_events WHERE resource_id=? ORDER BY created_at",
                (resource_id,),
            )
        else:
            rows = self.database.fetchall(
                "SELECT * FROM supreme_team_audit_events ORDER BY created_at DESC"
            )
        result = []
        for row in rows:
            item = dict(row)
            item["details"] = json.loads(item["details"])
            result.append(item)
        return result

    def management_status(self, actor: Actor) -> dict[str, Any]:
        self._actor(actor)
        if actor.role not in {OWNER, "CMD"}:
            raise PermissionError("CMD_OR_OWNER_STATUS_ACCESS_REQUIRED")
        counts = {}
        for table, key in (
            ("supreme_team_tasks","tasks"),
            ("supreme_team_change_proposals","change_proposals"),
            ("supreme_team_daily_reports","daily_reports"),
            ("supreme_team_audit_events","audit_events"),
        ):
            row = self.database.fetchone(f"SELECT COUNT(*) AS total FROM {table}")
            counts[key] = int(row["total"])
        return {
            "success": True, "system": "SUPREME_TEAM_MANAGEMENT",
            "status": "INITIALIZED", "counts": counts,
            "protected_actions_require_owner_approval": True,
            "automatic_repository_mutations_enabled": False,
        }
