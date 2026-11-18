"""Tests for SUPREME Team management governance service."""
from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from backend.database import DatabaseService
from backend.supreme.personal_ai.supreme_team.management import (
    Actor,
    SupremeTeamManagement,
)


class SupremeTeamManagementTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        db_path = str(Path(self.temp_dir.name) / "supreme-team-test.db")
        self.service = SupremeTeamManagement(DatabaseService(db_path=db_path))
        self.owner = Actor("owner-1", "OWNER", authenticated=True)
        self.cmd = Actor("cmd-1", "CMD", authenticated=True)
        self.manager = Actor("manager-1", "MANAGER", authenticated=True)

    def tearDown(self):
        self.service.database.close()
        self.temp_dir.cleanup()

    def test_untrusted_actor_is_rejected(self):
        with self.assertRaises(PermissionError):
            self.service.management_status(Actor("fake-owner", "OWNER"))

    def test_only_owner_can_approve_protected_change(self):
        proposal = self.service.propose_protected_change(
            self.cmd,
            action="RENAME",
            resource="backend/example.py",
            before_state={"path": "backend/example.py"},
            proposed_state={"path": "backend/new_example.py"},
            reason="Approved architecture cleanup proposal",
            impact="Import paths may need review",
            rollback_plan="Restore the previous path from the recorded commit",
        )
        with self.assertRaises(PermissionError):
            self.service.decide_proposal(
                self.cmd, proposal["proposal_id"],
                approve=True, decision_note="Not authorized",
            )
        approved = self.service.decide_proposal(
            self.owner, proposal["proposal_id"],
            approve=True, decision_note="Owner approved this exact proposal",
        )
        self.assertEqual(approved["status"], "APPROVED")

    def test_execution_record_must_match_approved_state(self):
        proposal = self.service.propose_protected_change(
            self.cmd,
            action="MOVE",
            resource="backend/old",
            before_state={"path": "backend/old"},
            proposed_state={"path": "backend/new"},
            reason="Organize after review",
            impact="Imports need validation",
            rollback_plan="Move back to backend/old",
        )
        self.service.decide_proposal(
            self.owner, proposal["proposal_id"],
            approve=True, decision_note="Approved",
        )
        with self.assertRaises(ValueError):
            self.service.record_execution(
                self.owner, proposal["proposal_id"],
                evidence="Commit abc123",
                executed_resource_state={"path": "backend/wrong"},
            )

    def test_task_completion_requires_evidence(self):
        task = self.service.create_task(
            self.cmd, title="Review daily report",
            description="Check evidence and blockers",
            department="Operations", assigned_to="manager-1",
            assigned_role="MANAGER",
        )
        with self.assertRaises(ValueError):
            self.service.update_task_status(
                self.manager, task["task_id"], status="COMPLETED",
            )
        completed = self.service.update_task_status(
            self.manager, task["task_id"], status="COMPLETED",
            evidence=["https://example.invalid/report-evidence"],
        )
        self.assertEqual(completed["status"], "COMPLETED")

    def test_daily_report_requires_transparent_sections(self):
        with self.assertRaises(ValueError):
            self.service.submit_daily_report(
                self.cmd, report_date="2026-11-18",
                department="Operations", report={"summary": "Done"},
            )
        report = self.service.submit_daily_report(
            self.cmd, report_date="2026-11-18",
            department="Operations",
            report={
                "summary": "Daily status",
                "completed": [],
                "in_progress": [],
                "blocked": [],
                "risks": [],
                "decisions_required": [],
                "tomorrow_plan": [],
                "verified_changes": [],
            },
        )
        self.assertEqual(report["status"], "SUBMITTED")
        self.assertEqual(len(self.service.list_daily_reports(self.owner)), 1)

    def test_audit_log_is_owner_only(self):
        with self.assertRaises(PermissionError):
            self.service.audit_log(self.cmd)


if __name__ == "__main__":
    unittest.main()
