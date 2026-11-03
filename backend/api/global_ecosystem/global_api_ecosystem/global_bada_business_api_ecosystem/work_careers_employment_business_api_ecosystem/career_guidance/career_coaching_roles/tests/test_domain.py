from ..services import get_job_family, validate_job_work_record

def test_job_family_has_distinct_roles_and_fields():
    family = get_job_family()
    assert family["category_id"] == "career_guidance"
    assert family["job_family_id"] == "career_coaching_roles"
    assert len(family["role_examples"]) >= 3
    assert len(family["required_domain_fields"]) >= 3

def test_empty_domain_record_is_rejected():
    result = validate_job_work_record({"domain_details": {}})
    assert result["valid"] is False
    assert result["errors"]
