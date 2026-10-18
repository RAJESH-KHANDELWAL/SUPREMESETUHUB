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
