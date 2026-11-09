"""Dedicated job and work family registry for full_time_jobs."""
CATEGORY_ID = "full_time_jobs"
JOB_FAMILIES = [
    {
        "id": "permanent_professional_roles",
        "name": "Permanent Professional Roles",
        "roles": [
            "Accountant",
            "software developer",
            "HR specialist"
        ]
    },
    {
        "id": "full_time_operations_roles",
        "name": "Full-Time Operations Roles",
        "roles": [
            "Production operator",
            "logistics coordinator",
            "facility supervisor"
        ]
    },
    {
        "id": "full_time_customer_roles",
        "name": "Full-Time Customer Roles",
        "roles": [
            "Customer success executive",
            "retail manager",
            "relationship officer"
        ]
    },
    {
        "id": "full_time_technical_roles",
        "name": "Full-Time Technical Roles",
        "roles": [
            "Maintenance engineer",
            "network engineer",
            "quality technician"
        ]
    }
]

def list_job_families():
    return [dict(item) for item in JOB_FAMILIES]
