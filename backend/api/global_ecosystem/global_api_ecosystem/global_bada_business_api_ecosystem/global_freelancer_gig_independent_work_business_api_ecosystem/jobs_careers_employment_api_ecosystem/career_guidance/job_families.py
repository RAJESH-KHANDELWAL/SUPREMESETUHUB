"""Dedicated job and work family registry for career_guidance."""
CATEGORY_ID = "career_guidance"
JOB_FAMILIES = [
    {
        "id": "career_assessment_services",
        "name": "Career Assessment Services",
        "roles": [
            "Aptitude assessor",
            "skills assessor",
            "psychometric practitioner"
        ]
    },
    {
        "id": "career_counselling_roles",
        "name": "Career Counselling Roles",
        "roles": [
            "Career counsellor",
            "student counsellor",
            "transition counsellor"
        ]
    },
    {
        "id": "career_coaching_roles",
        "name": "Career Coaching Roles",
        "roles": [
            "Career coach",
            "executive coach",
            "job-search coach"
        ]
    },
    {
        "id": "career_mentoring_roles",
        "name": "Career Mentoring Roles",
        "roles": [
            "Industry mentor",
            "technical mentor",
            "founder mentor"
        ]
    }
]

def list_job_families():
    return [dict(item) for item in JOB_FAMILIES]
