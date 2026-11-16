<?php
/**
 * Plugin Name: 👑 DR RAJESH KHANDELWAL IBC 👑
 * Description: Main brand plugin containing SUPREME, SUPREME Dashboard, and SUPREME ECOSYSTEM modules.
 * Version: 1.3.7
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
    // The brand plugin is the second independent top-level menu.
    // Its landing page opens the existing SUPREME Dashboard module.
    add_menu_page(
        '👑 DR RAJESH KHANDELWAL IBC 👑',
        '👑 DR RAJESH KHANDELWAL IBC 👑',
        'manage_options',
        'dr-rajesh-khandelwal-ibc-dashboard',
        function () {
            if (!current_user_can('manage_options')) { return; }
            if (function_exists('supreme_dashboard_render_page')) {
                supreme_dashboard_render_page();
                return;
            }
            echo '<div class="wrap"><h1>👑 DR RAJESH KHANDELWAL IBC 👑</h1><p>SUPREME Dashboard module is not loaded.</p></div>';
        },
        'data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2NCA2NCI+PHBhdGggZmlsbD0iI0Q0QUYzNyIgZD0iTTUgMTdsMTQgMTJMMzEgNmwxMyAyMyAxNS0xMi02IDM0SDExTDUgMTd6bTggMzloMzh2NEgxM3oiLz48L3N2Zz4=',
        58
    );

    // Keep infrastructure available as a child page instead of a separate dashboard.
    add_submenu_page(
        'dr-rajesh-khandelwal-ibc-dashboard',
        'Database & FTP Infrastructure',
        'Database & FTP',
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
        }
    );
}, 58);

add_action('admin_menu', function () {
    add_submenu_page(
        'dr-rajesh-khandelwal-ibc-dashboard',
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
        'dr-rajesh-khandelwal-ibc-dashboard',
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
}, 99);


register_activation_hook(__FILE__, 'dr_rajesh_khandelwal_ibc_activate');
register_deactivation_hook(__FILE__, 'dr_rajesh_khandelwal_ibc_deactivate');


/** Explicit Dashboard submenu for the IBC parent plugin. */
add_action('admin_menu', function () {
    add_submenu_page(
        'dr-rajesh-khandelwal-ibc-dashboard',
        '👑 DR RAJESH KHANDELWAL IBC DASHBOARD 👑',
        '👑 Dashboard 👑',
        'manage_options',
        'dr-rajesh-khandelwal-ibc-home-dashboard',
        function () {
            if (!current_user_can('manage_options')) { return; }
            if (function_exists('supreme_dashboard_render_page')) {
                supreme_dashboard_render_page();
                return;
            }
            echo '<div class="wrap"><h1>👑 DR RAJESH KHANDELWAL IBC DASHBOARD 👑</h1><p>SUPREME Dashboard module is not loaded. Check the parent plugin module loader.</p></div>';
        }
    );
}, 99);
