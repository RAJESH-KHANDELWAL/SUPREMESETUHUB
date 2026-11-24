"""SUPREME Owner Admin Password Manager policy metadata.

This module never stores, reveals, guesses, or recovers raw passwords.
Use the authorized identity provider's password-reset flow instead.
"""

def status() -> dict:
    return {
        "service": "SUPREME_OWNER_ADMIN_PASSWORD_MANAGER",
        "status": "LOCAL_ENCRYPTED_BROWSER_VAULT_UI_AVAILABLE",
        "storage_boundary": "BROWSER_MEMORY_AND_USER_DOWNLOADED_ENCRYPTED_FILE",
        "owner_authorization_required": "VAULT_PASSPHRASE_REQUIRED_FOR_VAULT_DATA",
        "admin_actions_audited": False,
        "raw_password_storage": False,
        "server_side_credential_storage": False,
        "csv_import": True,
        "clipboard_copy": True,
        "encrypted_export_import": True,
        "password_discovery": False,
        "recovery": "LOST_VAULT_PASSPHRASE_CANNOT_RECOVER_ENCRYPTED_EXPORT",
    }
