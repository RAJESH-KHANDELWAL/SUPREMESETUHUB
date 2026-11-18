"""Provider lifecycle metadata transitions for GOOGLE LANGUAGE."""
STATES = (
    "DISCOVERED", "CATALOGED", "ELIGIBILITY_REVIEW", "ADAPTER_PENDING",
    "CONNECTED", "SUSPENDED", "DEPRECATED", "DISCONTINUED",
)


def transition(current, target):
    if current not in STATES or target not in STATES:
        raise ValueError("UNKNOWN_PROVIDER_LIFECYCLE_STATE")
    return {
        "from": current,
        "to": target,
        "requires_external_verification": target == "CONNECTED",
    }
