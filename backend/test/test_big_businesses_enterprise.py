from backend.api.businesses import BusinessService
from backend.database.service import DatabaseService
from backend.schemas.business import BusinessCreateRequest


def test_enterprise_profile_fields_are_preserved(tmp_path):
    service = BusinessService(DatabaseService(str(tmp_path / "business.db")))
    request = BusinessCreateRequest(
        name="Global Example Ltd",
        legal_name="Global Example Limited",
        business_type="ENTERPRISE",
        industry="Technology",
        employee_count=12000,
        headquarters="Jaipur, India",
        parent_company_id="COMP-ROOT",
        annual_revenue_band="100M_PLUS",
        operating_regions=["India", "Europe"],
        departments=["Engineering", "Finance"],
        tags=["global", "b2b"],
        compliance_status="UNDER_REVIEW",
    )
    record = service.create_business(
        business_id="BUS-ENTERPRISE-1", owner_id="owner-1", name=request.name,
        legal_name=request.legal_name, business_type=request.business_type,
        industry=request.industry, employee_count=request.employee_count,
        headquarters=request.headquarters, parent_company_id=request.parent_company_id,
        annual_revenue_band=request.annual_revenue_band,
        operating_regions=request.operating_regions, departments=request.departments,
        tags=request.tags, compliance_status=request.compliance_status,
    )
    data = record.to_dict()
    assert data["business_type"] == "ENTERPRISE"
    assert data["employee_count"] == 12000
    assert data["operating_regions"] == ["India", "Europe"]
    assert data["departments"] == ["Engineering", "Finance"]
    assert data["compliance_status"] == "UNDER_REVIEW"
    service.repository.database.close()


def test_old_business_requests_keep_compatible_defaults():
    request = BusinessCreateRequest(name="Legacy business")
    assert request.business_type == "SMALL_BUSINESS"
    assert request.employee_count is None
    assert request.departments == []


def test_unsupported_business_type_is_rejected(tmp_path):
    service = BusinessService(DatabaseService(str(tmp_path / "invalid.db")))
    try:
        service.create_business(
            business_id="BUS-BAD", owner_id="owner-1", name="Bad type",
            business_type="NOT_A_REAL_TYPE",
        )
    except ValueError as error:
        assert "Unsupported business_type" in str(error)
    else:
        raise AssertionError("Unsupported business type should be rejected")
    finally:
        service.repository.database.close()


def test_business_records_survive_service_restart(tmp_path):
    database_path = str(tmp_path / "persistent-business.db")
    first_service = BusinessService(DatabaseService(database_path))
    first_service.create_business(
        business_id="BUS-PERSIST-1", owner_id="owner-7", name="Persistent Business",
        metadata={"source": "test"}, operating_regions=["India"],
    )
    first_service.repository.database.close()

    second_service = BusinessService(DatabaseService(database_path))
    restored = second_service.get_business("BUS-PERSIST-1")
    assert restored is not None
    assert restored.name == "Persistent Business"
    assert restored.metadata == {"source": "test"}
    assert restored.operating_regions == ["India"]
    second_service.repository.database.close()


def test_business_status_update_and_delete_are_persistent(tmp_path):
    database_path = str(tmp_path / "lifecycle.db")
    service = BusinessService(DatabaseService(database_path))
    service.create_business(
        business_id="BUS-LIFE-1", owner_id="owner-1", name="Lifecycle Business"
    )
    updated = service.update_status("BUS-LIFE-1", "inactive")
    assert updated is not None and updated.status == "INACTIVE"
    assert service.get_business("BUS-LIFE-1").status == "INACTIVE"
    assert service.delete_business("BUS-LIFE-1") is True
    assert service.get_business("BUS-LIFE-1") is None
    service.repository.database.close()


def test_business_service_rejects_missing_owner_and_blank_name(tmp_path):
    service = BusinessService(DatabaseService(str(tmp_path / "validation.db")))
    try:
        for values, expected in [
            ({"business_id": "BUS-1", "owner_id": "", "name": "Example"}, "owner_id is required"),
            ({"business_id": "BUS-2", "owner_id": "owner-1", "name": "  "}, "name is required"),
        ]:
            try:
                service.create_business(**values)
            except ValueError as error:
                assert expected in str(error)
            else:
                raise AssertionError("Invalid business record should be rejected")
    finally:
        service.repository.database.close()
