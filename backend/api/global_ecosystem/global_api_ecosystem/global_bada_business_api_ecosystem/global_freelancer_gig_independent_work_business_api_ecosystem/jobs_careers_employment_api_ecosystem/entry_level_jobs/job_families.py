"""Dedicated job and work family registry for entry_level_jobs."""
CATEGORY_ID = "entry_level_jobs"
JOB_FAMILIES = [
    {
        "id": "fresher_office_roles",
        "name": "Fresher Office Roles",
        "roles": [
            "Office assistant",
            "data entry operator",
            "front desk associate"
        ]
    },
    {
        "id": "graduate_trainee_roles",
        "name": "Graduate Trainee Roles",
        "roles": [
            "Management trainee",
            "graduate engineer trainee",
            "finance trainee"
        ]
    },
    {
        "id": "apprentice_trade_roles",
        "name": "Apprentice Trade Roles",
        "roles": [
            "Electrician apprentice",
            "fitter apprentice",
            "welder apprentice"
        ]
    },
    {
        "id": "internship_roles",
        "name": "Internship Roles",
        "roles": [
            "Software intern",
            "marketing intern",
            "research intern"
        ]
    }
]

def list_job_families():
    return [dict(item) for item in JOB_FAMILIES]
