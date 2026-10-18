from datetime import datetime, timezone

import pytest

from backend.crm.repository import CRMRepository
from backend.crm.service import CRMService
from backend.database.service import DatabaseService


@pytest.fixture
def crm(tmp_path):
    database = DatabaseService(db_path=str(tmp_path / "crm-test.db"))
    service = CRMService(CRMRepository(database))
    yield service
    database.close()


def test_contact_storage_is_scoped_to_user(crm):
    first = crm.create_contact("user-1", "user-1", {"full_name": "Asha", "email": "asha@example.com"})
    assert crm.get_contact("user-1", first["contact_id"])["full_name"] == "Asha"
    assert crm.get_contact("user-2", first["contact_id"]) is None
    assert crm.list_contacts("user-2") == []


def test_duplicate_suggestions_do_not_merge_records(crm):
    crm.create_contact("u", "u", {"full_name": "Asha", "email": "ASHA@example.com"})
    crm.create_contact("u", "u", {"full_name": "Asha K", "email": "asha@example.com"})
    matches = crm.duplicate_candidates("u")
    assert len(matches) == 1
    assert matches[0]["match_reason"] == "EMAIL"
    assert matches[0]["auto_merged"] is False


def test_category_suggestions_require_human_approval(crm):
    record = crm.create_contact("u", "u", {"full_name": "Ravi", "notes": "affiliate partner"})
    suggestion = crm.suggest_category(record)
    assert suggestion["suggested_category"] == "PARTNER"
    assert suggestion["requires_human_approval"] is True
    assert suggestion["applied"] is False


def test_do_not_contact_never_gets_outreach_draft(crm):
    record = crm.create_contact("u", "u", {
        "full_name": "Do Not Contact", "contact_status": "DO_NOT_CONTACT",
        "consent_to_contact": False,
    })
    with pytest.raises(PermissionError, match="EXPLICIT_CONTACT_CONSENT_REQUIRED"):
        crm.draft_message("u", record["contact_id"], "an offer")


def test_draft_is_never_sent(crm):
    record = crm.create_contact("u", "u", {
        "full_name": "Asha", "consent_to_contact": True,
    })
    draft = crm.draft_message("u", record["contact_id"], "the requested service")
    assert draft["sent"] is False
    assert draft["human_approval_required"] is True


def test_report_counts_only_current_users_records(crm):
    crm.create_contact("u1", "u1", {"full_name": "A"})
    crm.create_contact("u2", "u2", {"full_name": "B"})
    assert crm.report("u1")["report"]["total_contacts"] == 1


def test_invalid_do_not_contact_consent_combination_is_rejected(crm):
    record = crm.create_contact("u", "u", {"full_name": "A"})
    with pytest.raises(ValueError, match="DO_NOT_CONTACT"):
        crm.update_contact("u", "u", record["contact_id"], {
            "contact_status": "DO_NOT_CONTACT", "consent_to_contact": True,
        })


def test_import_preview_does_not_write_and_commit_requires_confirmation(crm):
    rows = [{"Name": "Imported Person", "Email": "imported@example.com"}]
    preview = crm.preview_import("u", "GOOGLE_SHEETS", rows)
    assert preview["ready_count"] == 1
    assert preview["records_written"] == 0
    assert preview["no_data_written"] is True
    assert crm.repository.counts("u")["total_contacts"] == 0
    with pytest.raises(PermissionError, match="HUMAN_IMPORT_CONFIRMATION_REQUIRED"):
        crm.commit_import("u", "u", "GOOGLE_SHEETS", rows, confirm_import=False)
    result = crm.commit_import("u", "u", "GOOGLE_SHEETS", rows, confirm_import=True)
    assert result["records_imported"] == 1
    assert crm.repository.counts("u")["total_contacts"] == 1


def test_import_preview_flags_existing_duplicate_for_human_review(crm):
    crm.create_contact("u", "u", {"full_name": "Existing", "email": "same@example.com"})
    preview = crm.preview_import("u", "GOOGLE_SHEETS", [
        {"Name": "Incoming", "Email": "same@example.com"}
    ])
    assert preview["duplicate_review_count"] == 1
    assert preview["records_written"] == 0


def test_quality_checker_flags_bad_and_missing_contact_fields(crm):
    from backend.crm.quality import assess_contact_quality

    result = assess_contact_quality({
        "full_name": "Test", "phone": "12345", "email": "bad-email",
        "whatsapp_phone": "", "organization": "", "address": "", "city": "",
        "verification_status": "UNVERIFIED",
    })
    codes = {flag["code"] for flag in result["flags"]}
    assert result["quality_label"] == "REVIEW_REQUIRED"
    assert "PHONE_FORMAT_INVALID" in codes
    assert "EMAIL_FORMAT_INVALID" in codes
    assert "WHATSAPP_NOT_PROVIDED" in codes
    assert result["claims_real_world_validity"] is False


def test_contact_profile_saves_whatsapp_address_and_verification(crm):
    record = crm.create_contact("u", "u", {
        "full_name": "Asha", "phone": "9876543210",
        "whatsapp_phone": "9876543210", "address": "Main Road",
        "city": "Jaipur", "pincode": "302001", "designation": "Agent",
        "verification_status": "VERIFIED",
    })
    assert record["whatsapp_phone"] == "9876543210"
    assert record["address"] == "Main Road"
    assert record["verification_status"] == "VERIFIED"
    assessment = crm.assess_contact("u", record["contact_id"])
    assert assessment["claims_real_world_validity"] is True


def test_daily_work_items_are_user_scoped_and_audited(crm):
    item = crm.create_daily_item("u1", "u1", {
        "title": "Call lead", "item_type": "CALL", "due_at": "2026-10-19T10:00:00"
    })
    assert item["status"] == "OPEN"
    assert crm.repository.get_daily_item("u2", item["item_id"]) is None
    updated = crm.update_daily_item("u1", "u1", item["item_id"], "DONE")
    assert updated["status"] == "DONE"
    assert crm.daily_briefing("u1")["summary"]["done"] == 1
    assert any(event["action"] == "DAILY_ITEM_STATUS_CHANGED"
               for event in crm.repository.list_audit_events("u1"))


def test_contact_activity_timeline_is_user_scoped_and_audited(crm):
    contact = crm.create_contact("u1", "u1", {"full_name": "Asha", "phone": "9876543210"})
    activity = crm.log_activity("u1", "u1", {
        "contact_id": contact["contact_id"], "activity_type": "CALL",
        "summary": "Discussed requested service", "outcome": "Asked for proposal",
        "next_follow_up_at": "2026-10-19T11:00:00",
    })
    assert activity["activity_type"] == "CALL"
    assert crm.contact_timeline("u1", contact["contact_id"])[0]["activity_id"] == activity["activity_id"]
    assert crm.contact_timeline("u2", contact["contact_id"]) is None
    assert any(event["action"] == "CONTACT_ACTIVITY_LOGGED"
               for event in crm.repository.list_audit_events("u1"))
