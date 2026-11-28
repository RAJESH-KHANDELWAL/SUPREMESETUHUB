"""Dedicated job and work family registry for hybrid_jobs."""
CATEGORY_ID = "hybrid_jobs"
JOB_FAMILIES = [
    {
        "id": "office_remote_hybrid_roles",
        "name": "Office and Remote Hybrid Roles",
        "roles": [
            "Hybrid analyst",
            "hybrid HR specialist",
            "hybrid software engineer"
        ]
    },
    {
        "id": "field_office_hybrid_roles",
        "name": "Field and Office Hybrid Roles",
        "roles": [
            "Field sales officer",
            "service engineer",
            "project inspector"
        ]
    },
    {
        "id": "client_site_hybrid_roles",
        "name": "Client-Site Hybrid Roles",
        "roles": [
            "Implementation consultant",
            "account manager",
            "IT support specialist"
        ]
    },
    {
        "id": "flexible_schedule_hybrid_roles",
        "name": "Flexible Schedule Hybrid Roles",
        "roles": [
            "Research analyst",
            "content strategist",
            "product designer"
        ]
    }
]

def list_job_families():
    return [dict(item) for item in JOB_FAMILIES]
