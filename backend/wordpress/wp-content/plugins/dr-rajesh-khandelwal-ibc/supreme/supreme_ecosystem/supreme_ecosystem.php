<?php
/**
 * SUPREME ECOSYSTEM module.
 * Loaded by the parent SUPREME module; not a standalone WordPress plugin.
 */
if (!defined('ABSPATH')) { exit; }
if (!function_exists('supreme_ecosystem_manifest')) {
    function supreme_ecosystem_manifest() {
        return array(
            'name' => 'SUPREME ECOSYSTEM',
            'display_name' => 'SUPREME ECOSYSTEM by SUPREMESETUHUB',
            'parent_module' => 'SUPREME',
            'identity_folders' => array('dr_rajesh_khandelwal_ibc', 'dr_rajesh_khandelwal_ibc_official', 'rajesh_khandelwal', 'rajesh_khandelwal_official'),
        );
    }
}

 
// Load the four identity modules for SUPREME ECOSYSTEM.
foreach (array('dr_rajesh_khandelwal_ibc', 'dr_rajesh_khandelwal_ibc_official', 'rajesh_khandelwal', 'rajesh_khandelwal_official') as $identity) {
    $identity_file = __DIR__ . '/' . $identity . '/' . $identity . '.php';
    if (is_file($identity_file)) { require_once $identity_file; }
}


// Load the SUPREME Dashboard Ecosystem submodule.
require_once __DIR__ . '/supreme_dashboard_ecosystem/supreme_dashboard_ecosystem.php';
