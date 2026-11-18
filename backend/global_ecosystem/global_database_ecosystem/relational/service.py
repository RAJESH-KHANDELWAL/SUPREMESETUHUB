"""Relational SQL platform descriptors and workload checks."""
from typing import Any
PLATFORMS = ("postgresql", "mysql", "mariadb", "sqlite", "microsoft_sql_server", "oracle_database")
def describe_relational_domain() -> dict[str, Any]:
    return {"domain":"relational_sql","platforms":list(PLATFORMS),"capabilities":["schemas","tables","views","constraints","indexes","transactions","joins"],"integration_status":"catalog_only"}
def validate_relational_workload(*, requires_transactions: bool, requires_relational_integrity: bool) -> tuple[str, ...]:
    if not requires_transactions and not requires_relational_integrity:
        return ("Confirm whether a specialized database model is a better fit.",)
    return ()
