"""Endpoint hardening baseline metadata."""
def assess_endpoint_baseline(*, disk_encryption, supported_os, endpoint_monitoring, patch_compliant, screen_lock):
    checks={"disk_encryption_missing":disk_encryption,"unsupported_os":supported_os,"endpoint_monitoring_missing":endpoint_monitoring,"patch_compliance_missing":patch_compliant,"screen_lock_missing":screen_lock}
    return tuple(name for name, ok in checks.items() if not ok)
