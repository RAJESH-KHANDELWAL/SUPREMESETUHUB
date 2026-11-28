"""Dedicated job and work family registry for part_time_jobs."""
CATEGORY_ID = "part_time_jobs"
JOB_FAMILIES = [
    {
        "id": "student_part_time_roles",
        "name": "Student Part-Time Roles",
        "roles": [
            "Tutor",
            "library assistant",
            "campus ambassador"
        ]
    },
    {
        "id": "weekend_part_time_roles",
        "name": "Weekend Part-Time Roles",
        "roles": [
            "Event staff",
            "retail associate",
            "hospitality assistant"
        ]
    },
    {
        "id": "evening_part_time_roles",
        "name": "Evening Part-Time Roles",
        "roles": [
            "Call centre agent",
            "online tutor",
            "restaurant service staff"
        ]
    },
    {
        "id": "professional_part_time_roles",
        "name": "Professional Part-Time Roles",
        "roles": [
            "Part-time accountant",
            "consultant",
            "therapist"
        ]
    }
]

def list_job_families():
    return [dict(item) for item in JOB_FAMILIES]
