"""Security control evidence completeness helper."""
def evaluate_control_evidence(control_id, evidence_items, *, owner_assigned, review_date=None):
    findings=[]
    if not control_id.strip(): findings.append("control_id_required")
    if not evidence_items: findings.append("evidence_missing")
    if not owner_assigned: findings.append("control_owner_missing")
    if not review_date: findings.append("review_date_missing")
    return tuple(findings)
