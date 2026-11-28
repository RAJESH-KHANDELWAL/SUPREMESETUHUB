"""Dedicated job and work family registry for recruitment."""
CATEGORY_ID = "recruitment"
JOB_FAMILIES = [
    {
        "id": "talent_sourcing_roles",
        "name": "Talent Sourcing Roles",
        "roles": [
            "Talent sourcer",
            "researcher",
            "candidate engagement specialist"
        ]
    },
    {
        "id": "recruitment_delivery_roles",
        "name": "Recruitment Delivery Roles",
        "roles": [
            "Recruiter",
            "senior recruiter",
            "recruitment partner"
        ]
    },
    {
        "id": "executive_search_roles",
        "name": "Executive Search Roles",
        "roles": [
            "Executive search consultant",
            "research lead",
            "assessment adviser"
        ]
    },
    {
        "id": "technical_recruitment_roles",
        "name": "Technical Recruitment Roles",
        "roles": [
            "Technical recruiter",
            "engineering recruiter",
            "IT talent partner"
        ]
    }
]

def list_job_families():
    return [dict(item) for item in JOB_FAMILIES]
