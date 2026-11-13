<?php
if (!defined('ABSPATH')) { exit; }
/** SUPREMESETUHUB WordPress connector — PHP runtime entry point. */
function supremesetuhub_wp_connector_status() {
    return array(
        'success' => true,
        'system' => 'SUPREMESETUHUB',
        'brand' => '👑 DR RAJESH KHANDELWAL IBC 👑',
        'wordpress' => true,
        'modules' => array('SUPREME', 'SUPREME ECOSYSTEM'),
    );
}
add_action('rest_api_init', function () {
    register_rest_route('supremesetuhub/v1', '/connector-status', array(
        'methods' => 'GET',
        'callback' => 'supremesetuhub_wp_connector_status',
        'permission_callback' => '__return_true',
    ));
});
