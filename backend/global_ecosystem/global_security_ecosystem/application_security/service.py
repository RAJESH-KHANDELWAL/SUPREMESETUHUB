"""Application security release-gate metadata checks."""
def validate_application_release(*, code_reviewed, dependencies_scanned, secrets_scanned, input_validation_reviewed, security_tests_passed):
    checks={"code_review_required":code_reviewed,"dependency_scan_required":dependencies_scanned,"secret_scan_required":secrets_scanned,"input_validation_review_required":input_validation_reviewed,"security_tests_required":security_tests_passed}
    return tuple(name for name, ok in checks.items() if not ok)
