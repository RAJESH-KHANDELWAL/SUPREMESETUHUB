<?php
/**
 * Plugin Name: SUPREMESETUHUB
 * Plugin URI: https://www.supremesetuhub.com
 * Description: SUPREMESETUHUB — WordPress integration and backend connectivity.
 * Version: 1.0.0
 * Author: 👑 DR RAJESH KHANDELWAL IBC 👑
 * Author URI: https://www.rajeshkhandelwal.com
 * License: GPL-2.0-or-later
 * Text Domain: supremesetuhub
 */

if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

define( 'SUPREMESETUHUB_VERSION', '1.0.0' );
define( 'SUPREMESETUHUB_FILE', __FILE__ );
define( 'SUPREMESETUHUB_DIR', plugin_dir_path( __FILE__ ) );

/**
 * Plugin activation.
 */
function supremesetuhub_activate() {
    update_option( 'supremesetuhub_status', 'active' );
    update_option( 'supremesetuhub_version', SUPREMESETUHUB_VERSION );
}

register_activation_hook( __FILE__, 'supremesetuhub_activate' );

/**
 * Plugin deactivation.
 */
function supremesetuhub_deactivate() {
    update_option( 'supremesetuhub_status', 'inactive' );
}

register_deactivation_hook( __FILE__, 'supremesetuhub_deactivate' );

/**
 * Basic REST API status endpoint.
 */
function supremesetuhub_status() {
    return array(
        'success'       => true,
        'plugin'        => 'SUPREMESETUHUB',
        'version'       => SUPREMESETUHUB_VERSION,
        'status'        => 'active',
        'wordpress'     => true,
        'github_ready'  => true,
        'backend_ready' => true,
    );
}

add_action(
    'rest_api_init',
    function () {
        register_rest_route(
            'supremesetuhub/v1',
            '/status',
            array(
                'methods'             => 'GET',
                'callback'            => 'supremesetuhub_status',
                'permission_callback' => '__return_true',
            )
        );
    }
);
