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

/**
 * Shared infrastructure panel for the four IBC identity gates.
 * Connection settings are centrally managed by the SUPREMESETUHUB plugin.
 */
add_action('admin_menu', function () {
    add_menu_page(
        'IBC Database & FTP',
        'IBC Infrastructure',
        'manage_options',
        'dr-rajesh-khandelwal-ibc-infrastructure',
        function () {
            if (!current_user_can('manage_options')) { return; }
            if (function_exists('supremesetuhub_render_control_plane_panel')) {
                supremesetuhub_render_control_plane_panel('DR RAJESH KHANDELWAL IBC — Shared Database & FTP');
                return;
            }
            echo '<div class="wrap"><h1>DR RAJESH KHANDELWAL IBC — Infrastructure</h1>';
            echo '<p>Activate the SUPREMESETUHUB hub plugin to load the shared, owner-authenticated Database & FTP control panel.</p></div>';
        },
        'dashicons-database',
        58
    );
});


register_activation_hook(__FILE__, 'dr_rajesh_khandelwal_ibc_activate');
register_deactivation_hook(__FILE__, 'dr_rajesh_khandelwal_ibc_deactivate');
