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

register_activation_hook(__FILE__, function () {
    update_option('supremesetuhub_plugin_version', SUPREMESETUHUB_VERSION);
});

add_action('admin_menu', function () {
    add_menu_page(
        'SUPREMESETUHUB',
        'SUPREMESETUHUB',
        'manage_options',
        'supremesetuhub',
        function () {
            if (!current_user_can('manage_options')) { return; }

            $status = supremesetuhub_wordpress_connector_status();
            echo '<div class="wrap"><h1>SUPREMESETUHUB</h1>';
            echo '<h2>DR RAJESH KHANDELWAL IBC</h2>';
            echo '<p>Unified WordPress integration registry</p>';
            echo '<table class="widefat striped"><thead><tr><th>Plugin</th><th>Plugin path</th><th>Status</th></tr></thead><tbody>';

            foreach ($status['wordpress_plugins'] as $plugin) {
                echo '<tr><td>' . esc_html($plugin['name']) . '</td>';
                echo '<td><code>' . esc_html($plugin['plugin_basename']) . '</code></td>';
                echo '<td>' . esc_html($plugin['active'] ? 'Active' : 'Inactive') . '</td></tr>';
            }

            echo '</tbody></table>';
            echo '<p><strong>Integration contract:</strong> <code>supremesetuhub-wordpress-v1</code></p>';
            echo '<p>SUPREME and SUPREME ECOSYSTEM remain modules inside the DR RAJESH KHANDELWAL IBC plugin.</p>';
            echo '<p>REST status: <code>/wp-json/supremesetuhub/v1/connector-status</code></p></div>';
        },
        'dashicons-networking'
    );
});
