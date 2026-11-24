"""Dedicated job and work family registry for shift_work."""
CATEGORY_ID = "shift_work"
JOB_FAMILIES = [
    {
        "id": "day_shift_occupations",
        "name": "Day Shift Occupations",
        "roles": [
            "Office operator",
            "day nurse",
            "production technician"
        ]
    },
    {
        "id": "evening_shift_occupations",
        "name": "Evening Shift Occupations",
        "roles": [
            "Evening support agent",
            "retail associate",
            "hotel receptionist"
        ]
    },
    {
        "id": "night_shift_occupations",
        "name": "Night Shift Occupations",
        "roles": [
            "Night auditor",
            "security operator",
            "overnight nurse"
        ]
    },
    {
        "id": "rotational_shift_occupations",
        "name": "Rotational Shift Occupations",
        "roles": [
            "Plant operator",
            "control room operator",
            "rail operations staff"
        ]
    }
]

def list_job_families():
    return [dict(item) for item in JOB_FAMILIES]
