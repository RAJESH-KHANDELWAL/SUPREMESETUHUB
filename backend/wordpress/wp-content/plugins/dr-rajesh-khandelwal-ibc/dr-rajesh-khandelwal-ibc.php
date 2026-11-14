<?php
/**
 * Plugin Name: 👑 DR RAJESH KHANDELWAL IBC 👑
 * Description: Main brand plugin containing SUPREME, SUPREME Dashboard, and SUPREME ECOSYSTEM modules.
 * Version: 1.3.6
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
        '👑 DR RAJESH KHANDELWAL IBC 👑',
        '👑 DR RAJESH KHANDELWAL IBC 👑',
        'manage_options',
        'dr-rajesh-khandelwal-ibc-infrastructure',
        function () {
            if (!current_user_can('manage_options')) { return; }
            if (function_exists('supremesetuhub_render_control_plane_panel')) {
                supremesetuhub_render_control_plane_panel('👑 DR RAJESH KHANDELWAL IBC 👑 — Shared Database & FTP');
                return;
            }
            echo '<div class="wrap"><h1>👑 DR RAJESH KHANDELWAL IBC 👑 — Infrastructure</h1>';
            echo '<p>Activate the SUPREMESETUHUB hub plugin to load the shared, owner-authenticated Database & FTP control panel.</p></div>';
        },
        'data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%2064%2064%22%3E%3Cpath%20fill%3D%22%23D4AF37%22%20d%3D%22M5%2017l14%2012L31%206l13%2023%2015-12-6%2034H11L5%2017zm8%2039h38v4H13z%22%2F%3E%3C%2Fsvg%3E',
        58
    );
});

add_action('admin_menu', function () {
    add_submenu_page(
        'dr-rajesh-khandelwal-ibc-infrastructure',
        '👑 FOUR BRAND IDENTITIES 👑',
        '👑 FOUR BRAND IDENTITIES 👑',
        'manage_options',
        'dr-rajesh-khandelwal-ibc-identities',
        function () {
            if (!current_user_can('manage_options')) { return; }
            $identities = array(
                array('RAJESH KHANDELWAL', 'RAJESHKHANDELWAL'),
                array('RAJESH KHANDELWAL OFFICIAL', 'RAJESHKHANDELWALOFFICIAL'),
                array('DR RAJESH KHANDELWAL IBC', 'DRRAJESHKHANDELWALIBC'),
                array('DR RAJESH KHANDELWAL IBC OFFICIAL', 'DRRAJESHKHANDELWALIBCOFFICIAL'),
            );
            echo '<div class="wrap"><h1>👑 DR RAJESH KHANDELWAL IBC 👑</h1><h2>👑 FOUR BRAND IDENTITIES 👑</h2>';
            echo '<table class="widefat striped"><thead><tr><th>Brand Identity</th><th>Identity ID</th></tr></thead><tbody>';
            foreach ($identities as $identity) {
                echo '<tr><td>👑 ' . esc_html($identity[0]) . ' 👑</td><td><code>' . esc_html($identity[1]) . '</code></td></tr>';
            }
            echo '</tbody></table></div>';
        }
    );
    add_submenu_page(
        'dr-rajesh-khandelwal-ibc-infrastructure',
        '🧩 First-party Plugins',
        '🧩 Plugins',
        'manage_options',
        'dr-rajesh-khandelwal-ibc-plugins',
        function () {
            if (!current_user_can('manage_options')) { return; }
            if (!function_exists('get_plugins')) { require_once ABSPATH . 'wp-admin/includes/plugin.php'; }
            $plugins = get_plugins();
            $targets = array(
                'supremesetuhub/supremesetuhub.php' => 'SUPREMESETUHUB',
                'dr-rajesh-khandelwal-ibc/dr-rajesh-khandelwal-ibc.php' => 'DR RAJESH KHANDELWAL IBC',
            );
            $active = (array) get_option('active_plugins', array());
            $network = is_multisite() ? (array) get_site_option('active_sitewide_plugins', array()) : array();
            echo '<div class="wrap"><h1>👑 DR RAJESH KHANDELWAL IBC 👑</h1><h2>🧩 FIRST-PARTY PLUGINS</h2>';
            echo '<table class="widefat striped"><thead><tr><th>Plugin</th><th>Plugin file</th><th>Installation</th><th>Activation</th></tr></thead><tbody>';
            foreach ($targets as $file => $label) {
                $installed = isset($plugins[$file]);
                $enabled = in_array($file, $active, true) || isset($network[$file]);
                echo '<tr><td>' . esc_html($label) . '</td><td><code>' . esc_html($file) . '</code></td><td>' . ($installed ? 'Installed' : 'Not installed') . '</td><td>' . ($enabled ? 'Active' : 'Inactive') . '</td></tr>';
            }
            echo '</tbody></table></div>';
        }
    );
});


register_activation_hook(__FILE__, 'dr_rajesh_khandelwal_ibc_activate');
register_deactivation_hook(__FILE__, 'dr_rajesh_khandelwal_ibc_deactivate');
