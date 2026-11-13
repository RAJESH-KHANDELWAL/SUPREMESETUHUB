<?php
/**
 * SUPREMESETUHUB WordPress connector PHP runtime.
 */
if (!defined('ABSPATH')) { exit; }

if (!function_exists('supremesetuhub_wordpress_connector_status')) {
    function supremesetuhub_wordpress_connector_status() {
        return rest_ensure_response(array(
            'success' => true,
            'system' => 'SUPREMESETUHUB',
            'connector' => 'WordPress',
            'brand' => '👑 DR RAJESH KHANDELWAL IBC 👑',
            'modules' => array('SUPREME', 'SUPREME ECOSYSTEM'),
            'runtime' => 'PHP',
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
