"""Dedicated job and work family registry for staffing."""
CATEGORY_ID = "staffing"
JOB_FAMILIES = [
    {
        "id": "permanent_staffing_services",
        "name": "Permanent Staffing Services",
        "roles": [
            "Permanent recruiter",
            "account manager",
            "talent researcher"
        ]
    },
    {
        "id": "temporary_staffing_services",
        "name": "Temporary Staffing Services",
        "roles": [
            "Temporary staffing coordinator",
            "site supervisor",
            "payroll associate"
        ]
    },
    {
        "id": "contract_workforce_management",
        "name": "Contract Workforce Management",
        "roles": [
            "Workforce coordinator",
            "vendor manager",
            "compliance executive"
        ]
    },
    {
        "id": "employer_of_record_services",
        "name": "Employer of Record Services",
        "roles": [
            "EOR specialist",
            "global mobility coordinator",
            "payroll compliance analyst"
        ]
    }
]

def list_job_families():
    return [dict(item) for item in JOB_FAMILIES]
