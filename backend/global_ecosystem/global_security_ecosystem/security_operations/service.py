"""Security alert triage prioritization."""
def prioritize_alert(*, severity, confidence, asset_criticality, active_exploitation=False):
    if severity not in {"critical","high","medium","low"}: raise ValueError("invalid severity")
    if not 0 <= confidence <= 100: raise ValueError("confidence must be 0..100")
    if asset_criticality not in {"critical","high","medium","low"}: raise ValueError("invalid asset_criticality")
    score={"critical":8,"high":6,"medium":4,"low":2}[severity]
    score += 1 if confidence >= 80 else 0
    score += 1 if asset_criticality in {"critical","high"} else 0
    score += 2 if active_exploitation else 0
    return min(score, 10)
