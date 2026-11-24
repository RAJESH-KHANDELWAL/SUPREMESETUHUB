"""Dedicated job and work family registry for remote_jobs."""
CATEGORY_ID = "remote_jobs"
JOB_FAMILIES = [
    {
        "id": "fully_remote_professional_roles",
        "name": "Fully Remote Professional Roles",
        "roles": [
            "Software engineer",
            "accountant",
            "content strategist"
        ]
    },
    {
        "id": "remote_customer_operations",
        "name": "Remote Customer Operations",
        "roles": [
            "Customer support agent",
            "technical support analyst",
            "claims processor"
        ]
    },
    {
        "id": "remote_digital_delivery",
        "name": "Remote Digital Delivery",
        "roles": [
            "Web developer",
            "UI designer",
            "SEO specialist"
        ]
    },
    {
        "id": "distributed_team_roles",
        "name": "Distributed Team Roles",
        "roles": [
            "Product manager",
            "data analyst",
            "project coordinator"
        ]
    }
]

def list_job_families():
    return [dict(item) for item in JOB_FAMILIES]
