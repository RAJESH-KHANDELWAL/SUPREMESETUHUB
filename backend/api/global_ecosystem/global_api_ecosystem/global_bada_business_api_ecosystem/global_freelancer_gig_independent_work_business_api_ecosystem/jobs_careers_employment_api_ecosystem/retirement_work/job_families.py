"""Dedicated job and work family registry for retirement_work."""
CATEGORY_ID = "retirement_work"
JOB_FAMILIES = [
    {
        "id": "phased_retirement_roles",
        "name": "Phased Retirement Roles",
        "roles": [
            "Senior adviser",
            "part-time manager",
            "technical mentor"
        ]
    },
    {
        "id": "retired_consultant_roles",
        "name": "Retired Consultant Roles",
        "roles": [
            "Industry consultant",
            "finance adviser",
            "engineering consultant"
        ]
    },
    {
        "id": "mentor_knowledge_transfer_roles",
        "name": "Mentor and Knowledge Transfer Roles",
        "roles": [
            "Workplace mentor",
            "trainer",
            "succession adviser"
        ]
    },
    {
        "id": "part_time_senior_roles",
        "name": "Part-Time Senior Roles",
        "roles": [
            "Senior accountant",
            "quality adviser",
            "project reviewer"
        ]
    }
]

def list_job_families():
    return [dict(item) for item in JOB_FAMILIES]
