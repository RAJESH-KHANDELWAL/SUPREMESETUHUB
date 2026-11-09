"""Dedicated job and work family registry for executive_jobs."""
CATEGORY_ID = "executive_jobs"
JOB_FAMILIES = [
    {
        "id": "chief_executive_roles",
        "name": "Chief Executive Roles",
        "roles": [
            "Chief executive officer",
            "chief operating officer",
            "chief transformation officer"
        ]
    },
    {
        "id": "finance_executive_roles",
        "name": "Finance Executive Roles",
        "roles": [
            "Chief financial officer",
            "chief accounting officer",
            "chief investment officer"
        ]
    },
    {
        "id": "technology_executive_roles",
        "name": "Technology Executive Roles",
        "roles": [
            "Chief information officer",
            "chief technology officer",
            "chief information security officer"
        ]
    },
    {
        "id": "board_governance_roles",
        "name": "Board and Governance Roles",
        "roles": [
            "Independent director",
            "non-executive director",
            "audit committee member"
        ]
    }
]

def list_job_families():
    return [dict(item) for item in JOB_FAMILIES]
