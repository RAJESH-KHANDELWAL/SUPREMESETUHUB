<?php
/** SUPREME ECOSYSTEM Owner Admin Password Manager policy metadata only. */
declare(strict_types=1);

return [
    'service' => 'SUPREME_ECOSYSTEM_OWNER_ADMIN_PASSWORD_MANAGER',
    'status' => 'LOCAL_ENCRYPTED_BROWSER_VAULT_UI_AVAILABLE',
    'owner_authorization_required' => 'VAULT_PASSPHRASE_REQUIRED_FOR_VAULT_DATA',
    'admin_actions_audited' => false,
    'raw_password_storage' => false,
    'server_side_credential_storage' => false,
    'csv_import' => true,
    'clipboard_copy' => true,
    'encrypted_export_import' => true,
    'password_discovery' => false,
    'recovery' => 'LOST_VAULT_PASSPHRASE_CANNOT_RECOVER_ENCRYPTED_EXPORT',
];
