<?php
/**
 * SUPREMESETUHUB WordPress connector — central hub runtime.
 * Separate companion plugins: SUPREME and SUPREME ECOSYSTEM.
 */
if (!defined('ABSPATH')) { exit; }

if (!function_exists('supremesetuhub_wordpress_connector_status')) {
    function supremesetuhub_wordpress_connector_status() {
        return rest_ensure_response(array(
            'success' => true,
            'hub' => 'SUPREMESETUHUB',
            'brand' => '👑 DR RAJESH KHANDELWAL IBC 👑',
            'connector' => 'WordPress',
            'runtime' => 'PHP',
            'companion_brands' => array(
                'SUPREME by SUPREMESETUHUB',
                'SUPREME ECOSYSTEM by SUPREMESETUHUB',
            ),
            'note' => 'Connector endpoint is registered; companion plugin runtime integration requires matching installed plugin basenames and end-to-end testing.',
        ));
    }
}

add_action('rest_api_init', function () {
    register_rest_route('supremesetuhub/v1', '/connector-status', array(
        'methods' => WP_REST_Server::READABLE,
        'callback' => 'supremesetuhub_wordpress_connector_status',
        'permission_callback' => '__return_true',
    ));
});
