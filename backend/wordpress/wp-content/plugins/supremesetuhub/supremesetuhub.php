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
        'data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Cpath fill='%23D4AF37' d='M5 17l14 12L31 6l13 23 15-12-6 34H11L5 17zm8 39h38v4H13z'/%3E%3C/svg%3E'
    );
});
