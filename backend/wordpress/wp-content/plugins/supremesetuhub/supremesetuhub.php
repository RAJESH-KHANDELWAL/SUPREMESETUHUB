<?php
/**
 * Plugin Name: SUPREMESETUHUB
 * Description: Central WordPress integration hub for SUPREME and the DR RAJESH KHANDELWAL IBC plugin.
 * Version: 1.3.1
 * Author: 👑 DR RAJESH KHANDELWAL IBC 👑
 * Text Domain: supremesetuhub
 */
if (!defined('ABSPATH')) { exit; }

define('SUPREMESETUHUB_VERSION', '1.3.1');
define('SUPREMESETUHUB_DIR', plugin_dir_path(__FILE__));
define('SUPREMESETUHUB_URL', plugin_dir_url(__FILE__));

if (!function_exists('supremesetuhub_core_manifest')) {
    function supremesetuhub_core_manifest() {
        return array(
            'hub' => 'SUPREMESETUHUB',
            'brand' => 'DR RAJESH KHANDELWAL IBC',
            'integration_contract' => 'supremesetuhub-wordpress-v1',
            'wordpress_plugins' => array(
                'supremesetuhub/supremesetuhub.php',
                'dr-rajesh-khandelwal-ibc/dr-rajesh-khandelwal-ibc.php',
            ),
            'modules' => array(
                'supreme' => 'SUPREME by SUPREMESETUHUB',
                'supreme_ecosystem' => 'SUPREME ECOSYSTEM by SUPREMESETUHUB',
            ),
        );
    }
}

require_once SUPREMESETUHUB_DIR . 'supremesetuhub_wordpress_connector.php';
require_once SUPREMESETUHUB_DIR . 'supremesetuhub_control_plane.php';

register_activation_hook(__FILE__, function () {
    update_option('supremesetuhub_plugin_version', SUPREMESETUHUB_VERSION);
});

add_action('admin_menu', function () {
    add_submenu_page(
        'supremesetuhub',
        '🧩 First-party Plugins',
        '🧩 Plugins',
        'manage_options',
        'supremesetuhub-plugins',
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
            echo '<div class="wrap"><h1>👑 SUPREMESETUHUB 👑</h1><h2>🧩 FIRST-PARTY PLUGINS</h2>';
            echo '<table class="widefat striped"><thead><tr><th>Plugin</th><th>Plugin file</th><th>Installation</th><th>Activation</th></tr></thead><tbody>';
            foreach ($targets as $file => $label) {
                $installed = isset($plugins[$file]);
                $enabled = in_array($file, $active, true) || isset($network[$file]);
                echo '<tr><td>👑 ' . esc_html($label) . ' 👑</td><td><code>' . esc_html($file) . '</code></td><td>' . ($installed ? 'Installed' : 'Not installed') . '</td><td>' . ($enabled ? 'Active' : 'Inactive') . '</td></tr>';
            }
            echo '</tbody></table></div>';
        }
    );
}, 99);

add_action('admin_menu', function () {
    add_menu_page(
        '👑 SUPREMESETUHUB 👑',
        '👑 SUPREMESETUHUB 👑',
        'manage_options',
        'supremesetuhub',
        function () {
            if (!current_user_can('manage_options')) { return; }

            $status = supremesetuhub_wordpress_connector_status();
            echo '<div class="wrap"><h1>👑 SUPREMESETUHUB 👑</h1>';
            echo '<h2>👑 DR RAJESH KHANDELWAL IBC 👑</h2>';
            echo '<p>Unified WordPress integration registry</p>';
            echo '<table class="widefat striped"><thead><tr><th>Plugin</th><th>Plugin path</th><th>Status</th></tr></thead><tbody>';

            foreach ($status['wordpress_plugins'] as $plugin) {
                echo '<tr><td>' . esc_html($plugin['name']) . '</td>';
                echo '<td><code>' . esc_html($plugin['plugin_basename']) . '</code></td>';
                echo '<td>' . esc_html($plugin['active'] ? 'Active' : 'Inactive') . '</td></tr>';
            }

            echo '</tbody></table>';
            echo '<p><strong>Integration contract:</strong> <code>supremesetuhub-wordpress-v1</code></p>';
            echo '<h2>👑 FOUR BRAND IDENTITIES 👑</h2>';
            echo '<table class="widefat striped"><thead><tr><th>Brand Identity</th><th>Identity ID</th><th>Type</th></tr></thead><tbody>';
            $identities = array(
                array('RAJESH KHANDELWAL', 'RAJESHKHANDELWAL', 'Primary brand identity'),
                array('RAJESH KHANDELWAL OFFICIAL', 'RAJESHKHANDELWALOFFICIAL', 'Official brand identity'),
                array('DR RAJESH KHANDELWAL IBC', 'DRRAJESHKHANDELWALIBC', 'IBC brand identity'),
                array('DR RAJESH KHANDELWAL IBC OFFICIAL', 'DRRAJESHKHANDELWALIBCOFFICIAL', 'Official IBC identity'),
            );
            foreach ($identities as $identity) {
                echo '<tr><td>👑 ' . esc_html($identity[0]) . ' 👑</td><td><code>' . esc_html($identity[1]) . '</code></td><td>' . esc_html($identity[2]) . '</td></tr>';
            }
            echo '</tbody></table>';
            echo '<p>SUPREME and SUPREME ECOSYSTEM remain modules inside the DR RAJESH KHANDELWAL IBC plugin.</p>';
            echo '<p>REST status: <code>/wp-json/supremesetuhub/v1/connector-status</code></p></div>';
        },
        'data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%2064%2064%22%3E%3Cpath%20fill%3D%22%23D4AF37%22%20d%3D%22M5%2017l14%2012L31%206l13%2023%2015-12-6%2034H11L5%2017zm8%2039h38v4H13z%22%2F%3E%3C%2Fsvg%3E'
    );
});
