"""Ministry and department taxonomy for central recruitment."""
DEPARTMENT_TYPES = ("ministry", "department", "attached_office", "subordinate_office", "field_formation")
EMPLOYMENT_DOMAINS = ("administration", "finance_and_accounts", "engineering", "science_and_research", "law_and_compliance", "operations", "clerical_and_support")

def get_department_taxonomy() -> dict:
    return {"track_id": "central_government_recruitment", "domain_id": "ministries_and_departments", "department_types": DEPARTMENT_TYPES, "employment_domains": EMPLOYMENT_DOMAINS, "required_context": ("parent_ministry", "jurisdiction", "recruiting_authority")}
