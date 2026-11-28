"""Global Password Manager Ecosystem policy metadata.

This module never stores, reveals, guesses, or recovers raw passwords.
Use the authorized identity provider's password-reset flow instead.
"""

def status() -> dict:
    return {
        "service": "SUPREME_ECOSYSTEM_OWNER_ADMIN_PASSWORD_MANAGER",
        "status": "LOCAL_ENCRYPTED_BROWSER_VAULT_UI_AVAILABLE",
        "storage_boundary": "BROWSER_MEMORY_AND_USER_DOWNLOADED_ENCRYPTED_FILE",
        "owner_authorization_required": "VAULT_PASSPHRASE_REQUIRED_FOR_VAULT_DATA",
        "admin_actions_audited": False,
        "raw_password_storage": False,
        "server_side_credential_storage": False,
        "csv_import": True,
        "csv_duplicate_detection": True,
        "duplicate_key_fields": ["url", "username_or_email", "name"],
        "duplicate_key_normalization": ["unicode_nfkc", "trim", "casefold", "remove_url_query_fragment", "remove_trailing_path_slash"],
        "duplicate_detection_scope": "EXISTING_VAULT_AND_CURRENT_CSV_IMPORT",
        "clipboard_copy": True,
        "encrypted_export_import": True,
        "password_discovery": False,
        "recovery": "LOST_VAULT_PASSPHRASE_CANNOT_RECOVER_ENCRYPTED_EXPORT",
    }
