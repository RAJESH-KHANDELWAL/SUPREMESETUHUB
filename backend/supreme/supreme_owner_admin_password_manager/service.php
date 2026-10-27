<?php
/**
 * SUPREME Owner Admin Password Manager policy metadata.
 * Does not store, reveal, guess, or recover raw passwords.
 */
declare(strict_types=1);

return [
    'service' => 'SUPREME_OWNER_ADMIN_PASSWORD_MANAGER',
    'status' => 'LOCAL_ENCRYPTED_BROWSER_VAULT_UI_AVAILABLE',
    'owner_authorization_required' => true,
    'admin_actions_audited' => true,
    'raw_password_storage' => false,\n    'server_side_credential_storage' => false,\n    'csv_import' => true,\n    'clipboard_copy' => true,\n    'encrypted_export_import' => true,
    'password_discovery' => false,
    'recovery' => 'USE_IDENTITY_PROVIDER_RESET_FLOW',
];
