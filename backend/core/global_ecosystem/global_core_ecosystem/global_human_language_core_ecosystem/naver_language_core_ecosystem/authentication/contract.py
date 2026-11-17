"""Authentication boundary contract; credentials are owned by the API layer."""
def valid_tenant_context(context):
    return (
        isinstance(context, dict)
        and isinstance(context.get("tenant_id"), str)
        and bool(context["tenant_id"].strip())
        and isinstance(context.get("actor_id"), str)
        and bool(context["actor_id"].strip())
    )


def credentials_in_core_enabled():
    return False
