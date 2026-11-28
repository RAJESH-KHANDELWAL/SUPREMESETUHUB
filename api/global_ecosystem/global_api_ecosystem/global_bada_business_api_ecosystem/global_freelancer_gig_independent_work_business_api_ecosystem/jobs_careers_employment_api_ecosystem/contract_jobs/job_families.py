"""Dedicated job and work family registry for contract_jobs."""
CATEGORY_ID = "contract_jobs"
JOB_FAMILIES = [
    {
        "id": "fixed_term_project_roles",
        "name": "Fixed-Term Project Roles",
        "roles": [
            "Project coordinator",
            "implementation specialist",
            "site supervisor"
        ]
    },
    {
        "id": "independent_professional_contracts",
        "name": "Independent Professional Contracts",
        "roles": [
            "Independent accountant",
            "design consultant",
            "IT consultant"
        ]
    },
    {
        "id": "agency_supplied_contract_roles",
        "name": "Agency-Supplied Contract Roles",
        "roles": [
            "Warehouse associate",
            "office administrator",
            "production operator"
        ]
    },
    {
        "id": "consulting_advisory_contracts",
        "name": "Consulting Advisory Contracts",
        "roles": [
            "Management consultant",
            "HR consultant",
            "technology adviser"
        ]
    }
]

def list_job_families():
    return [dict(item) for item in JOB_FAMILIES]
