"""Data protection control checklist."""
def validate_data_handling(*, classification, encryption_at_rest, encryption_in_transit, retention_defined, backup_tested):
    issues=[]
    if classification not in {"public","internal","confidential","restricted"}: issues.append("classification_required")
    if not encryption_at_rest: issues.append("encryption_at_rest_required")
    if not encryption_in_transit: issues.append("encryption_in_transit_required")
    if not retention_defined: issues.append("retention_policy_required")
    if not backup_tested: issues.append("backup_restore_test_required")
    return tuple(issues)
