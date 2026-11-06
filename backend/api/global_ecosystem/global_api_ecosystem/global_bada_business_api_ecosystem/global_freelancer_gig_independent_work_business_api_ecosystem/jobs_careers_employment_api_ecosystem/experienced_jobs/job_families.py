"""Dedicated job and work family registry for experienced_jobs."""
CATEGORY_ID = "experienced_jobs"
JOB_FAMILIES = [
    {
        "id": "senior_functional_specialists",
        "name": "Senior Functional Specialists",
        "roles": [
            "Senior accountant",
            "senior analyst",
            "senior engineer"
        ]
    },
    {
        "id": "people_management_roles",
        "name": "People Management Roles",
        "roles": [
            "Team manager",
            "department manager",
            "regional manager"
        ]
    },
    {
        "id": "technical_architecture_roles",
        "name": "Technical Architecture Roles",
        "roles": [
            "Solution architect",
            "principal engineer",
            "enterprise architect"
        ]
    },
    {
        "id": "programme_delivery_roles",
        "name": "Programme Delivery Roles",
        "roles": [
            "Programme manager",
            "portfolio manager",
            "PMO lead"
        ]
    }
]

def list_job_families():
    return [dict(item) for item in JOB_FAMILIES]
