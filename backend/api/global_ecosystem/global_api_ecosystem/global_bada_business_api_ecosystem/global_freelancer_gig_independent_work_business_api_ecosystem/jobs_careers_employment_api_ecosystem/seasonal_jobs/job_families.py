"""Dedicated job and work family registry for seasonal_jobs."""
CATEGORY_ID = "seasonal_jobs"
JOB_FAMILIES = [
    {
        "id": "agriculture_seasonal_work",
        "name": "Agriculture Seasonal Work",
        "roles": [
            "Harvest worker",
            "sorting grader",
            "irrigation assistant"
        ]
    },
    {
        "id": "tourism_seasonal_work",
        "name": "Tourism Seasonal Work",
        "roles": [
            "Tour guide",
            "hotel associate",
            "travel desk executive"
        ]
    },
    {
        "id": "festival_retail_work",
        "name": "Festival and Retail Seasonal Work",
        "roles": [
            "Temporary sales associate",
            "stock handler",
            "cashier"
        ]
    },
    {
        "id": "logistics_peak_work",
        "name": "Logistics Peak Work",
        "roles": [
            "Warehouse picker",
            "sortation associate",
            "delivery helper"
        ]
    }
]

def list_job_families():
    return [dict(item) for item in JOB_FAMILIES]
