"""Network security policy metadata validation."""
def validate_network_policy(*, environment, tls_required, segmentation_defined, ingress_reviewed, egress_reviewed):
    issues=[]
    if environment not in {"development", "staging", "production"}: issues.append("invalid_environment")
    if not tls_required: issues.append("tls_required")
    if not segmentation_defined: issues.append("network_segmentation_review_required")
    if not ingress_reviewed: issues.append("ingress_review_required")
    if not egress_reviewed: issues.append("egress_review_required")
    return tuple(issues)
