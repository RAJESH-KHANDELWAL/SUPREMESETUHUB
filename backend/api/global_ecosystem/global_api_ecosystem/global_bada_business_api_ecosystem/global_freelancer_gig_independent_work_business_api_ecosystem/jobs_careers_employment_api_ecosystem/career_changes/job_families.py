"""Dedicated job and work family registry for career_changes."""
CATEGORY_ID = "career_changes"
JOB_FAMILIES = [
    {
        "id": "industry_switch_roles",
        "name": "Industry Switch Roles",
        "roles": [
            "Operations-to-project coordinator",
            "accounts-to-finance analyst",
            "retail-to-customer success"
        ]
    },
    {
        "id": "career_reentry_roles",
        "name": "Career Re-entry Roles",
        "roles": [
            "Returnship associate",
            "refresher trainee",
            "re-entry analyst"
        ]
    },
    {
        "id": "occupation_pivot_roles",
        "name": "Occupation Pivot Roles",
        "roles": [
            "Support-to-business analyst",
            "sales-to-marketing executive",
            "technician-to-quality inspector"
        ]
    },
    {
        "id": "reskilling_transition_roles",
        "name": "Reskilling Transition Roles",
        "roles": [
            "Cloud support trainee",
            "data operations associate",
            "junior cyber analyst"
        ]
    }
]

def list_job_families():
    return [dict(item) for item in JOB_FAMILIES]
