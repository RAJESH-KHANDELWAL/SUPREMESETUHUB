"""Static health/readiness checks for the provider catalog."""


def check_health():
    from .service import readiness
    state = readiness()
    return {"status": "catalog_ready", **state}
