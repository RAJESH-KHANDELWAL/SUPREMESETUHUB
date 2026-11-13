<?php
/**
 * SUPREMESETUHUB WordPress connector.
 * Registers a read-only status route and reports whether the two separate
 * companion WordPress plugins are active.
 */
if (!defined('ABSPATH')) { exit; }

if (!function_exists('supremesetuhub_wp_connector_status')) {
    function supremesetuhub_wp_connector_status() {
        $plugins = (array) get_option('active_plugins', array());
        $supreme_active = in_array('supreme/supreme.php', $plugins, true);
        $ecosystem_active = in_array('supreme-ecosystem/supreme-ecosystem.php', $plugins, true);

        return rest_ensure_response(array(
            'success' => true,
            'hub' => 'SUPREMESETUHUB',
            'brand' => '👑 DR RAJESH KHANDELWAL IBC 👑',
            'wordpress' => array(
                'runtime' => 'PHP',
                'connector' => 'registered',
            ),
            'companion_plugins' => array(
                'supreme' => array(
                    'brand' => 'SUPREME by SUPREMESETUHUB',
                    'active' => $supreme_active,
                ),
                'supreme_ecosystem' => array(
                    'brand' => 'SUPREME ECOSYSTEM by SUPREMESETUHUB',
                    'active' => $ecosystem_active,
                ),
            ),
        ));
    }
}

add_action('rest_api_init', function () {
    register_rest_route('supremesetuhub/v1', '/connector-status', array(
        'methods' => WP_REST_Server::READABLE,
        'callback' => 'supremesetuhub_wp_connector_status',
        'permission_callback' => '__return_true',
    ));
});
