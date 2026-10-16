from fastapi import HTTPException

from backend.api import people as people_api
from backend.core.global_ecosystem.global_core_ecosystem.referral_service import (
    SupremeReferralService,
)
from backend.database.referral_repository import ReferralRepository
from backend.database.service import DatabaseService
from backend.storage.referral_store import ReferralStore


def _service(tmp_path):
    database = DatabaseService(db_path=str(tmp_path / "people-api.db"))
    repository = ReferralRepository(database=database)
    return SupremeReferralService(store=ReferralStore(repository=repository)), database


def test_people_api_persists_private_contact_with_consent_off_by_default(tmp_path, monkeypatch):
    service, database = _service(tmp_path)
    monkeypatch.setattr(people_api, "service", service)

    request = people_api.PersonCreateRequest(
        display_name="Test Lead",
        source_platform="WEBSITE",
        need_category="WEBSITE_SERVICE",
        whatsapp_contact="+910000000000",
    )
    created = people_api.create_person(request)
    person_id = created["data"]["person_id"]

    assert created["success"] is True
    assert created["data"]["contact_consent"] == 0
    assert people_api.get_person(person_id)["data"]["person_id"] == person_id
    assert people_api.people_summary()["consented_to_contact_count"] == 0

    database.close()


def test_people_api_stage_can_disable_contact_consent(tmp_path, monkeypatch):
    service, database = _service(tmp_path)
    monkeypatch.setattr(people_api, "service", service)
    created = people_api.create_person(
        people_api.PersonCreateRequest(
            display_name="Test Lead",
            source_platform="WEBSITE",
            need_category="CONSULTING",
            contact_consent=True,
        )
    )
    person_id = created["data"]["person_id"]

    updated = people_api.update_person_stage(
        person_id,
        people_api.PersonStageRequest(response_stage="DO_NOT_CONTACT"),
    )

    assert updated["data"]["response_stage"] == "DO_NOT_CONTACT"
    assert updated["data"]["contact_consent"] == 0
    database.close()


def test_people_api_rejects_non_https_referral_links(tmp_path, monkeypatch):
    service, database = _service(tmp_path)
    monkeypatch.setattr(people_api, "service", service)

    request = people_api.ReferralLinkCreateRequest(
        platform="AFFILIATE",
        program_name="Test Program",
        referral_url="http://example.com/ref",
    )

    try:
        people_api.create_referral_link(request)
    except HTTPException as exc:
        assert exc.status_code == 422
    else:
        raise AssertionError("Non-HTTPS referral URL must be rejected")
    database.close()


def test_people_api_router_requires_admin_dependency():
    assert people_api.router.dependencies
    assert all(
        dependency.dependency.__name__ == "require_admin"
        for dependency in people_api.router.dependencies
    )
