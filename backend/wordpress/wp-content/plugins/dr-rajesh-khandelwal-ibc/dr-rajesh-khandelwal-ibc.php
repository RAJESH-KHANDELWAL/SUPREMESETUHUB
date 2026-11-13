<?php
/**
 * Plugin Name: 👑 DR RAJESH KHANDELWAL IBC 👑
 * Description: Main brand plugin containing SUPREME, SUPREME Dashboard, and SUPREME ECOSYSTEM modules.
 * Version: 1.3.3
 * Author: 👑 DR RAJESH KHANDELWAL IBC 👑
 * Text Domain: dr-rajesh-khandelwal-ibc
 */
if (!defined('ABSPATH')) { exit; }

if (!defined('DR_RAJESH_KHANDELWAL_IBC_ROOT_FILE')) {
    define('DR_RAJESH_KHANDELWAL_IBC_ROOT_FILE', __FILE__);
}
if (!defined('DR_RAJESH_KHANDELWAL_IBC_ROOT_DIR')) {
    define('DR_RAJESH_KHANDELWAL_IBC_ROOT_DIR', plugin_dir_path(__FILE__));
}

require_once __DIR__ . '/supreme/dr-rajesh-khandelwal-ibc.php';

register_activation_hook(__FILE__, 'dr_rajesh_khandelwal_ibc_activate');
register_deactivation_hook(__FILE__, 'dr_rajesh_khandelwal_ibc_deactivate');
