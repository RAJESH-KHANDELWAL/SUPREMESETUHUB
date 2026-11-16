"""Dedicated job and work family registry for temporary_jobs."""
CATEGORY_ID = "temporary_jobs"
JOB_FAMILIES = [
    {
        "id": "short_term_assignment_roles",
        "name": "Short-Term Assignment Roles",
        "roles": [
            "Inventory counter",
            "document digitizer",
            "survey enumerator"
        ]
    },
    {
        "id": "temporary_replacement_roles",
        "name": "Temporary Replacement Roles",
        "roles": [
            "Temporary receptionist",
            "acting clerk",
            "cover teacher"
        ]
    },
    {
        "id": "event_temporary_roles",
        "name": "Event Temporary Roles",
        "roles": [
            "Registration assistant",
            "usher",
            "event setup worker"
        ]
    },
    {
        "id": "temporary_admin_operations",
        "name": "Temporary Admin and Operations Roles",
        "roles": [
            "Temporary data entry clerk",
            "office assistant",
            "dispatch coordinator"
        ]
    }
]

def list_job_families():
    return [dict(item) for item in JOB_FAMILIES]
