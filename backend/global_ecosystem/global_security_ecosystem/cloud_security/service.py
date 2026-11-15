"""Cloud security posture checklist helper."""
def assess_cloud_posture(*, mfa_enforced, public_storage_reviewed, audit_logging_enabled, backups_protected, workload_identity_used):
    controls={"mfa_not_enforced":mfa_enforced,"public_storage_review_missing":public_storage_reviewed,"audit_logging_disabled":audit_logging_enabled,"backup_protection_missing":backups_protected,"workload_identity_review_missing":workload_identity_used}
    return tuple(name for name, ok in controls.items() if not ok)
