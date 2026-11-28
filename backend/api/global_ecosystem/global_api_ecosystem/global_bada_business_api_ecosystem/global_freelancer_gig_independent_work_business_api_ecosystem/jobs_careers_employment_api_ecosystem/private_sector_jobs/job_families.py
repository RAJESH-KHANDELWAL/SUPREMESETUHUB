"""Dedicated job and work family registry for private_sector_jobs."""
CATEGORY_ID = "private_sector_jobs"
JOB_FAMILIES = [
    {
        "id": "private_company_functional_roles",
        "name": "Private Company Functional Roles",
        "roles": [
            "Finance executive",
            "HR officer",
            "operations analyst"
        ]
    },
    {
        "id": "startup_venture_roles",
        "name": "Startup and Venture Roles",
        "roles": [
            "Founder associate",
            "growth operator",
            "product generalist"
        ]
    },
    {
        "id": "small_business_jobs",
        "name": "Small Business Jobs",
        "roles": [
            "Office manager",
            "accounts assistant",
            "sales coordinator"
        ]
    },
    {
        "id": "private_professional_firm_roles",
        "name": "Private Professional Firm Roles",
        "roles": [
            "Audit associate",
            "legal associate",
            "tax consultant"
        ]
    }
]

def list_job_families():
    return [dict(item) for item in JOB_FAMILIES]
