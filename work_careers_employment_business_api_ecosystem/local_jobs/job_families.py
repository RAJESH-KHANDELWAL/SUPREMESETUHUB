"""Dedicated job and work family registry for local_jobs."""
CATEGORY_ID = "local_jobs"
JOB_FAMILIES = [
    {
        "id": "neighborhood_service_jobs",
        "name": "Neighborhood Service Jobs",
        "roles": [
            "Shop assistant",
            "home tutor",
            "repair technician"
        ]
    },
    {
        "id": "city_commercial_jobs",
        "name": "City Commercial Jobs",
        "roles": [
            "Sales executive",
            "store manager",
            "delivery coordinator"
        ]
    },
    {
        "id": "district_administration_jobs",
        "name": "District Administration Jobs",
        "roles": [
            "District coordinator",
            "block programme assistant",
            "office clerk"
        ]
    },
    {
        "id": "rural_village_jobs",
        "name": "Rural and Village Jobs",
        "roles": [
            "Community mobilizer",
            "rural technician",
            "agri-input adviser"
        ]
    }
]

def list_job_families():
    return [dict(item) for item in JOB_FAMILIES]
