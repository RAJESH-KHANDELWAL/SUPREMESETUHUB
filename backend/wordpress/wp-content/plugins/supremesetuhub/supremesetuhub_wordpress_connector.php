<?php
/**
 * SUPREMESETUHUB WordPress integration registry.
 * Detects the two separately installed first-party plugins without coupling their load order.
 */
if (!defined('ABSPATH')) { exit; }

if (!function_exists('supremesetuhub_wordpress_connector_status')) {
    function supremesetuhub_wordpress_connector_status() {
        $active_plugins = (array) get_option('active_plugins', array());
        $network_active = (array) get_site_option('active_sitewide_plugins', array());

        $plugin_registry = array(
            'supremesetuhub_core' => array(
                'name' => 'SUPREMESETUHUB',
                'plugin_basename' => 'supremesetuhub/supremesetuhub.php',
            ),
            'dr_rajesh_khandelwal_ibc' => array(
                'name' => 'DR RAJESH KHANDELWAL IBC',
                'plugin_basename' => 'dr-rajesh-khandelwal-ibc/dr-rajesh-khandelwal-ibc.php',
            ),
        );

        foreach ($plugin_registry as $key => $plugin) {
            $basename = $plugin['plugin_basename'];
            $plugin_registry[$key]['active'] = in_array($basename, $active_plugins, true)
                || isset($network_active[$basename]);
        }

        // Retain the legacy module map for clients that already consume this endpoint.
        $ibc_active = $plugin_registry['dr_rajesh_khandelwal_ibc']['active'];

        return array(
            'success' => true,
            'hub' => 'SUPREMESETUHUB',
            'brand' => 'DR RAJESH KHANDELWAL IBC',
            'connector' => 'WordPress',
            'integration_contract' => 'supremesetuhub-wordpress-v1',
            'wordpress_plugins' => $plugin_registry,
            'companion_plugins' => array(
                'supreme' => array(
                    'brand' => 'SUPREME by SUPREMESETUHUB',
                    'active' => $ibc_active,
                    'plugin_basename' => 'dr-rajesh-khandelwal-ibc/dr-rajesh-khandelwal-ibc.php',
                    'note' => 'SUPREME is a module inside the IBC plugin, not a separate WordPress plugin.',
                ),
                'supreme_ecosystem' => array(
                    'brand' => 'SUPREME ECOSYSTEM by SUPREMESETUHUB',
                    'active' => $ibc_active,
                    'plugin_basename' => 'dr-rajesh-khandelwal-ibc/dr-rajesh-khandelwal-ibc.php',
                    'note' => 'SUPREME ECOSYSTEM is a module inside the IBC plugin, not a separate WordPress plugin.',
                ),
            ),
        );
    }
}

add_action('rest_api_init', function () {
    register_rest_route('supremesetuhub/v1', '/connector-status', array(
        'methods' => WP_REST_Server::READABLE,
        'callback' => function () {
            return rest_ensure_response(supremesetuhub_wordpress_connector_status());
        },
        'permission_callback' => '__return_true',
    ));
});
