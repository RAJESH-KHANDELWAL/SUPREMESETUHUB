"""Dedicated job and work family registry for return_to_work."""
CATEGORY_ID = "return_to_work"
JOB_FAMILIES = [
    {
        "id": "returnship_programme_roles",
        "name": "Returnship Programme Roles",
        "roles": [
            "Returnship analyst",
            "returnship developer",
            "returnship associate"
        ]
    },
    {
        "id": "career_reentry_professional_roles",
        "name": "Career Re-entry Professional Roles",
        "roles": [
            "Re-entry accountant",
            "re-entry teacher",
            "re-entry project officer"
        ]
    },
    {
        "id": "flexible_reentry_roles",
        "name": "Flexible Re-entry Roles",
        "roles": [
            "Part-time analyst",
            "flexible administrator",
            "remote support specialist"
        ]
    },
    {
        "id": "refresher_training_pathways",
        "name": "Refresher Training Pathways",
        "roles": [
            "Refresher trainee",
            "bridge-course associate",
            "skills conversion trainee"
        ]
    }
]

def list_job_families():
    return [dict(item) for item in JOB_FAMILIES]
