"""Technology-neutral web application blueprint."""
def get_web_stack_blueprint() -> dict:
    return {
        "layers": ["experience", "frontend", "backend", "integration", "data_contracts", "operations"],
        "capabilities": ["responsive_web", "accessibility", "localisation", "seo", "testing", "observability"],
        "runtime_owner": "API/CORE/ENGINE/DATABASE/SECURITY",
        "status": "REFERENCE_BLUEPRINT",
    }
__all__ = ["get_web_stack_blueprint"]
