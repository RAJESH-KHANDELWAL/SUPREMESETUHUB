"""Secret inventory metadata checks. Never store secret values here."""
def validate_secret_metadata(*, secret_id, owner, purpose, rotation_days, stored_in_approved_vault):
    findings=[]
    if not secret_id.strip(): findings.append("secret_id_required")
    if not owner.strip(): findings.append("owner_required")
    if not purpose.strip(): findings.append("purpose_required")
    if rotation_days < 1: findings.append("rotation_period_required")
    if not stored_in_approved_vault: findings.append("approved_vault_required")
    return tuple(findings)
