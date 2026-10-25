from backend.businesses.service import BusinessService
from backend.schemas.business import BusinessCreateRequest


def test_enterprise_profile_fields_are_preserved():
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
    service = BusinessService()
    record = service.create_business(
        business_id="BUS-ENTERPRISE-1",
        owner_id="owner-1",
        name=request.name,
        legal_name=request.legal_name,
        business_type=request.business_type,
        industry=request.industry,
        employee_count=request.employee_count,
        headquarters=request.headquarters,
        parent_company_id=request.parent_company_id,
        annual_revenue_band=request.annual_revenue_band,
        operating_regions=request.operating_regions,
        departments=request.departments,
        tags=request.tags,
        compliance_status=request.compliance_status,
    )
    data = record.to_dict()
    assert data["business_type"] == "ENTERPRISE"
    assert data["employee_count"] == 12000
    assert data["operating_regions"] == ["India", "Europe"]
    assert data["departments"] == ["Engineering", "Finance"]
    assert data["compliance_status"] == "UNDER_REVIEW"


def test_old_business_requests_keep_compatible_defaults():
    request = BusinessCreateRequest(name="Legacy business")
    assert request.business_type == "SMALL_BUSINESS"
    assert request.employee_count is None
    assert request.departments == []


def test_unsupported_business_type_is_rejected():
    service = BusinessService()
    try:
        service.create_business(
            business_id="BUS-BAD",
            owner_id="owner-1",
            name="Bad type",
            business_type="NOT_A_REAL_TYPE",
        )
    except ValueError as error:
        assert "Unsupported business_type" in str(error)
    else:
        raise AssertionError("Unsupported business type should be rejected")
