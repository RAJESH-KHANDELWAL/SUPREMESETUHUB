"""Dedicated job and work family registry for public_sector_jobs."""
CATEGORY_ID = "public_sector_jobs"
JOB_FAMILIES = [
    {
        "id": "public_enterprise_roles",
        "name": "Public Enterprise Roles",
        "roles": [
            "Management trainee",
            "engineer",
            "finance officer"
        ]
    },
    {
        "id": "public_banking_roles",
        "name": "Public Banking Roles",
        "roles": [
            "Probationary officer",
            "clerk",
            "specialist officer"
        ]
    },
    {
        "id": "public_education_roles",
        "name": "Public Education Roles",
        "roles": [
            "Teacher",
            "librarian",
            "research assistant"
        ]
    },
    {
        "id": "public_healthcare_roles",
        "name": "Public Healthcare Roles",
        "roles": [
            "Nurse",
            "lab technician",
            "medical officer"
        ]
    },
    {
        "id": "public_utility_roles",
        "name": "Public Utility Roles",
        "roles": [
            "Line worker",
            "plant operator",
            "junior engineer"
        ]
    }
]

def list_job_families():
    return [dict(item) for item in JOB_FAMILIES]
