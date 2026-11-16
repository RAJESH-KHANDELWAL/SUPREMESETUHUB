"""Dedicated job and work family registry for international_jobs."""
CATEGORY_ID = "international_jobs"
JOB_FAMILIES = [
    {
        "id": "overseas_skilled_employment",
        "name": "Overseas Skilled Employment",
        "roles": [
            "Registered nurse",
            "civil engineer",
            "electrician"
        ]
    },
    {
        "id": "international_remote_employment",
        "name": "International Remote Employment",
        "roles": [
            "Remote developer",
            "designer",
            "customer success specialist"
        ]
    },
    {
        "id": "expatriate_assignments",
        "name": "Expatriate Assignments",
        "roles": [
            "Country manager",
            "project director",
            "technical secondee"
        ]
    },
    {
        "id": "international_organization_roles",
        "name": "International Organization Roles",
        "roles": [
            "Programme officer",
            "policy analyst",
            "field coordinator"
        ]
    }
]

def list_job_families():
    return [dict(item) for item in JOB_FAMILIES]
