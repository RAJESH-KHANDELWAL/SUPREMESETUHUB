<?php
/**
 * SUPREME module bootstrap — loaded by the parent brand plugin.
 */
if (!defined('ABSPATH')) { exit; }
if (!defined('SUPREME_MODULE_VERSION')) {
    define('SUPREME_MODULE_VERSION', '1.0.0');
}
if (!function_exists('supreme_module_manifest')) {
    function supreme_module_manifest() {
        return array(
            'name' => 'SUPREME',
            'display_name' => 'SUPREME by SUPREMESETUHUB',
            'parent_plugin' => 'DR RAJESH KHANDELWAL IBC',
            'identity_folders' => array('dr_rajesh_khandelwal_ibc', 'dr_rajesh_khandelwal_ibc_official', 'rajesh_khandelwal', 'rajesh_khandelwal_official'),
        );
    }
}

 
// Load the four SUPREME identity modules.
foreach (array('dr_rajesh_khandelwal_ibc', 'dr_rajesh_khandelwal_ibc_official', 'rajesh_khandelwal', 'rajesh_khandelwal_official') as $identity) {
    $identity_file = __DIR__ . '/' . $identity . '/' . $identity . '.php';
    if (is_file($identity_file)) { require_once $identity_file; }
}

// Load SUPREME ECOSYSTEM as a child module of SUPREME.
require_once __DIR__ . '/supreme_ecosystem/supreme_ecosystem.php';
