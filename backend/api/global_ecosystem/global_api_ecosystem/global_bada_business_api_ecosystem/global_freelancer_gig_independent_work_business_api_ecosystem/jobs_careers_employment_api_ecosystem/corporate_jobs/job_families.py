"""Dedicated job and work family registry for corporate_jobs."""
CATEGORY_ID = "corporate_jobs"
JOB_FAMILIES = [
    {
        "id": "corporate_finance_roles",
        "name": "Corporate Finance Roles",
        "roles": [
            "Financial analyst",
            "treasury analyst",
            "cost controller"
        ]
    },
    {
        "id": "corporate_people_roles",
        "name": "Corporate People Roles",
        "roles": [
            "HR business partner",
            "talent acquisition specialist",
            "payroll manager"
        ]
    },
    {
        "id": "corporate_operations_roles",
        "name": "Corporate Operations Roles",
        "roles": [
            "Operations manager",
            "procurement specialist",
            "business operations analyst"
        ]
    },
    {
        "id": "corporate_technology_roles",
        "name": "Corporate Technology Roles",
        "roles": [
            "Enterprise architect",
            "cloud engineer",
            "IT service manager"
        ]
    }
]

def list_job_families():
    return [dict(item) for item in JOB_FAMILIES]
