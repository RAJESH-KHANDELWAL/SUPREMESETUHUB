<?php
/**
 * SUPREMESETUHUB WordPress REST connector.
 * Reports whether the two separate companion plugins are active.
 */
if (!defined('ABSPATH')) { exit; }

if (!function_exists('supremesetuhub_wordpress_connector_status')) {
    function supremesetuhub_wordpress_connector_status() {
        $active_plugins = (array) get_option('active_plugins', array());

        // These basenames are placeholders until confirmed against each
        // companion plugin's actual directory and main PHP filename.
        $supreme_basename = apply_filters('supremesetuhub_supreme_plugin_basename', 'supreme/supreme.php');
        $ecosystem_basename = apply_filters('supremesetuhub_ecosystem_plugin_basename', 'supreme-ecosystem/supreme-ecosystem.php');

        return rest_ensure_response(array(
            'success' => true,
            'hub' => 'SUPREMESETUHUB',
            'brand' => '👑 DR RAJESH KHANDELWAL IBC 👑',
            'connector' => 'WordPress',
            'companion_plugins' => array(
                'supreme' => array(
                    'brand' => 'SUPREME by SUPREMESETUHUB',
                    'active' => in_array($supreme_basename, $active_plugins, true),
                    'plugin_basename' => $supreme_basename,
                ),
                'supreme_ecosystem' => array(
                    'brand' => 'SUPREME ECOSYSTEM by SUPREMESETUHUB',
                    'active' => in_array($ecosystem_basename, $active_plugins, true),
                    'plugin_basename' => $ecosystem_basename,
                ),
            ),
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
