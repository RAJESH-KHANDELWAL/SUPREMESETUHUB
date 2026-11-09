<?php
/** Canonical registry for the four primary SUPREME owner identities.
 * The separate rajesh_khandelwal_personal variant is intentionally excluded.
 */
return [
    'rajesh_khandelwal' => require __DIR__ . '/../rajesh_khandelwal/identity.php',
    'rajesh_khandelwal_official' => require __DIR__ . '/rajesh_khandelwal_official/identity.php',
    'dr_rajesh_khandelwal_ibc' => require __DIR__ . '/dr_rajesh_khandelwal_ibc/identity.php',
    'dr_rajesh_khandelwal_ibc_official' => require __DIR__ . '/dr_rajesh_khandelwal_ibc_official/identity.php',
];
