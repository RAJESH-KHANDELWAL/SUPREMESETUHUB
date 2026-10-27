<?php
/**
 * SUPREME Owner Admin Password Manager policy metadata.
 * Does not store, reveal, guess, or recover raw passwords.
 */
declare(strict_types=1);

return [
    'service' => 'SUPREME_OWNER_ADMIN_PASSWORD_MANAGER',
    'status' => 'POLICY_METADATA_ONLY',
    'owner_authorization_required' => true,
    'admin_actions_audited' => true,
    'raw_password_storage' => false,
    'password_discovery' => false,
    'recovery' => 'USE_IDENTITY_PROVIDER_RESET_FLOW',
];
