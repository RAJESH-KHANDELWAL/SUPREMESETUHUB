"""Dedicated job and work family registry for government_jobs."""
CATEGORY_ID = "government_jobs"
JOB_FAMILIES = [
    {
        "id": "central_administrative_posts",
        "name": "Central Administrative Posts",
        "roles": [
            "Section officer",
            "assistant section officer",
            "under secretary"
        ]
    },
    {
        "id": "central_technical_posts",
        "name": "Central Technical Posts",
        "roles": [
            "Scientific assistant",
            "junior engineer",
            "technical officer"
        ]
    },
    {
        "id": "railway_operational_posts",
        "name": "Railway Operational Posts",
        "roles": [
            "Station master",
            "loco pilot",
            "train manager"
        ]
    },
    {
        "id": "government_teaching_posts",
        "name": "Government Teaching Posts",
        "roles": [
            "Primary teacher",
            "trained graduate teacher",
            "assistant professor"
        ]
    },
    {
        "id": "government_health_posts",
        "name": "Government Health Posts",
        "roles": [
            "Medical officer",
            "staff nurse",
            "pharmacist"
        ]
    },
    {
        "id": "police_and_security_posts",
        "name": "Police and Security Posts",
        "roles": [
            "Constable",
            "sub inspector",
            "assistant commissioner"
        ]
    },
    {
        "id": "defence_uniformed_posts",
        "name": "Defence Uniformed Posts",
        "roles": [
            "Soldier",
            "sailor",
            "airman"
        ]
    },
    {
        "id": "government_finance_posts",
        "name": "Government Finance Posts",
        "roles": [
            "Auditor",
            "tax assistant",
            "accounts officer"
        ]
    },
    {
        "id": "government_legal_posts",
        "name": "Government Legal Posts",
        "roles": [
            "Public prosecutor",
            "legal assistant",
            "civil judge"
        ]
    },
    {
        "id": "government_agriculture_posts",
        "name": "Government Agriculture Posts",
        "roles": [
            "Agriculture officer",
            "forest guard",
            "rural development officer"
        ]
    }
]

def list_job_families():
    return [dict(item) for item in JOB_FAMILIES]
