from backend.core.global_ecosystem.global_core_ecosystem.catalog import get_catalog
from backend.database.freelancer_ecosystem import FreelancerEcosystemRepository
from backend.engines.freelancer_ecosystem.manager import FreelancerEcosystemEngine


def test_freelancer_records_persist_and_are_owner_scoped(tmp_path, monkeypatch):
    monkeypatch.setenv("SUPREME_DB_PATH", str(tmp_path / "central.db"))
    repository = FreelancerEcosystemRepository()

    created = repository.create(
        owner_id="user-1",
        record_type="PROFILE",
        title="Freelancer profile",
        payload={"skills": ["WordPress", "Copywriting"]},
    )

    assert created["record_id"].startswith("FRE-")
    assert created["status"] == "DRAFT"
    assert created["payload"]["skills"] == ["WordPress", "Copywriting"]
    assert len(repository.list_for_owner(owner_id="user-1")) == 1
    assert repository.list_for_owner(owner_id="user-2") == []
    assert repository.get(created["record_id"], owner_id="user-2") is None


def test_freelancer_repository_rejects_unknown_record_type(tmp_path, monkeypatch):
    monkeypatch.setenv("SUPREME_DB_PATH", str(tmp_path / "central.db"))
    repository = FreelancerEcosystemRepository()

    try:
        repository.create(
            owner_id="user-1",
            record_type="PAYMENT_SECRET",
            title="not allowed",
            payload={},
        )
    except ValueError as exc:
        assert str(exc) == "UNSUPPORTED_FREELANCER_RECORD_TYPE"
    else:
        raise AssertionError("Unsupported record type should be rejected")


def test_freelancer_ecosystem_is_registered_in_core_catalog():
    records = get_catalog()
    record = next(
        item for item in records
        if item["ecosystem_id"] == "GLOBAL-FREELANCER-ECOSYSTEM"
    )
    assert record["parent_id"] == "GLOBAL-BUSINESS-ECOSYSTEM"
    assert "PROJECT_BRIEFS" in record["capabilities"]


def test_freelancer_engine_does_not_claim_production_ready(tmp_path, monkeypatch):
    monkeypatch.setenv("SUPREME_DB_PATH", str(tmp_path / "central.db"))
    status = FreelancerEcosystemEngine().status()
    assert status["success"] is True
    assert status["production_ready"] is False
    assert status["provider_integrations"]["google_drive"] == "NOT_IMPLEMENTED"
