"""Database security control catalog; policy execution belongs to SECURITY layer."""
def describe_database_security_domain():
    return {"domain":"database_security","controls":["least_privilege","role_based_access","attribute_based_access","encryption_at_rest","encryption_in_transit","key_rotation","secret_management","audit_logging","tenant_isolation","sensitive_field_protection","anomaly_detection"],"integration_status":"catalog_only","runtime_owner":"canonical SECURITY and IDENTITY layers"}
