<?php
/**
 * SUPREME Dashboard module.
 * Loaded by supreme.php; not a separate WordPress plugin.
 */
if (!defined('ABSPATH')) { exit; }

if (!function_exists('supreme_dashboard_manifest')) {
    function supreme_dashboard_manifest() {
        return array(
            'module' => 'SUPREME DASHBOARD',
            'parent' => 'SUPREME',
            'parent_brand' => 'DR RAJESH KHANDELWAL IBC',
        );
    }
}

add_action('admin_menu', function () {
    add_menu_page(
        'SUPREME Dashboard',
        'SUPREME Dashboard',
        'SUPREME Dashboard',
        'Dashboard',
        'manage_options',
        'supreme-dashboard',
        function () {
            if (!current_user_can('manage_options')) { return; }
            echo '<div class="wrap"><h1>SUPREME Dashboard</h1>';
            echo '<p>SUPREME module dashboard scaffold is loaded.</p></div>';
        }
    );
});
