<?php
/** Registry connecting all four identity PHP modules to SUPREME ECOSYSTEM. */
return [
    'dr_rajesh_khandelwal_ibc' => require __DIR__ . '/dr_rajesh_khandelwal_ibc/identity.php',
    'dr_rajesh_khandelwal_ibc_official' => require __DIR__ . '/dr_rajesh_khandelwal_ibc_official/identity.php',
    'rajesh_khandelwal_official' => require __DIR__ . '/rajesh_khandelwal_official/identity.php',
    'rajesh_khandelwal_personal' => require __DIR__ . '/rajesh_khandelwal_personal/identity.php',
];
