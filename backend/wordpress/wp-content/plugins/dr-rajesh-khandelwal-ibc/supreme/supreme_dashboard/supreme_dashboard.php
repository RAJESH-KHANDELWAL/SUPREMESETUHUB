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
        '👑 SUPREME DASHBOARD 👑',
        '👑 SUPREME DASHBOARD 👑',
        'manage_options',
        'supreme-dashboard',
        function () {
            if (!current_user_can('manage_options')) { return; }
            echo '<div class="wrap"><h1>👑 SUPREME DASHBOARD 👑</h1>';
            echo '<p>SUPREME Dashboard module is loaded under DR RAJESH KHANDELWAL IBC.</p></div>';
        },
        'data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%2064%2064%22%3E%3Cpath%20fill%3D%22%23D4AF37%22%20d%3D%22M5%2017l14%2012L31%206l13%2023%2015-12-6%2034H11L5%2017zm8%2039h38v4H13z%22%2F%3E%3C%2Fsvg%3E',
        59
    );
});
