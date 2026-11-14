"""Canonical relationship vocabulary for infrastructure topology."""
RELATIONSHIP_TYPES = (
    "CONTAINS",
    "HOSTS",
    "RUNS_ON",
    "CONNECTED_TO",
    "USES",
    "DEPENDS_ON",
    "SERVES",
    "ROUTES_TO",
    "BACKS_UP",
    "PROTECTED_BY",
    "DELIVERED_BY",
    "REPLICATES_TO",
    "MONITORED_BY",
)

def list_relationship_types() -> tuple[str, ...]:
    return RELATIONSHIP_TYPES
