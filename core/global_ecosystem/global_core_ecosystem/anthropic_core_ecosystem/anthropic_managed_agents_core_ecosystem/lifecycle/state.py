"""Lifecycle metadata; CONNECTED requires external API-layer verification."""
STATES=("DISCOVERED","CATALOGED","ELIGIBILITY_REVIEW","ADAPTER_PENDING","CONNECTED","SUSPENDED","DEPRECATED","DISCONTINUED")

def transition(current: str, target: str, *, external_verification: bool = False) -> dict:
    if current not in STATES or target not in STATES:
        raise ValueError("unknown lifecycle state")
    if target == "CONNECTED" and not external_verification:
        raise ValueError("LIVE_CONNECTION_REQUIRES_EXTERNAL_VERIFICATION")
    return {"from":current,"to":target,"requires_external_verification":target=="CONNECTED"}
