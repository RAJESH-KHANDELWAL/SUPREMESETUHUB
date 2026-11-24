"""Dedicated job and work family registry for placements."""
CATEGORY_ID = "placements"
JOB_FAMILIES = [
    {
        "id": "campus_recruitment_placements",
        "name": "Campus Recruitment Placements",
        "roles": [
            "Graduate engineer trainee",
            "management trainee",
            "analyst trainee"
        ]
    },
    {
        "id": "apprenticeship_placements",
        "name": "Apprenticeship Placements",
        "roles": [
            "ITI apprentice",
            "degree apprentice",
            "technician apprentice"
        ]
    },
    {
        "id": "returnship_placements",
        "name": "Returnship Placements",
        "roles": [
            "Returnship analyst",
            "returnship engineer",
            "returnship manager"
        ]
    },
    {
        "id": "vocational_placement_services",
        "name": "Vocational Placement Services",
        "roles": [
            "Electrician trainee",
            "healthcare assistant",
            "machine operator"
        ]
    }
]

def list_job_families():
    return [dict(item) for item in JOB_FAMILIES]
