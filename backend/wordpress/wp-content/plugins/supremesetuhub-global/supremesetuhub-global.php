<?php
/**
 * Plugin Name: 👑 SUPREMESETUHUB 👑
 * Plugin URI: https://www.supremesetuhub.com
 * Description: 👑 SUPREMESETUHUB 👑 — Global WordPress integration and backend connectivity plugin.
 * Version: 1.0.0
 * Author: 👑 DR RAJESH KHANDELWAL IBC 👑
 * Author URI: https://www.rajeshkhandelwal.com
 * License: GPL-2.0-or-later
 * Text Domain: supremesetuhub-global
 */

if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

define( 'SUPREMESETUHUB_GLOBAL_VERSION', '1.0.0' );
define( 'SUPREMESETUHUB_GLOBAL_FILE', __FILE__ );
define( 'SUPREMESETUHUB_GLOBAL_DIR', plugin_dir_path( __FILE__ ) );

/**
 * Plugin activation.
 */
function supremesetuhub_global_activate() {

    update_option(
        'supremesetuhub_global_status',
        'active'
    );

    update_option(
        'supremesetuhub_global_version',
        SUPREMESETUHUB_GLOBAL_VERSION
    );
}

register_activation_hook(
    __FILE__,
    'supremesetuhub_global_activate'
);

/**
 * Plugin deactivation.
 */
function supremesetuhub_global_deactivate() {

    update_option(
        'supremesetuhub_global_status',
        'inactive'
    );
}

register_deactivation_hook(
    __FILE__,
    'supremesetuhub_global_deactivate'
);

/**
 * Basic REST API status endpoint.
 */
function supremesetuhub_global_status() {

    return array(
        'success'       => true,
        'plugin'        => 'SUPREMESETUHUB',
        'version'       => SUPREMESETUHUB_GLOBAL_VERSION,
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
                'callback'            => 'supremesetuhub_global_status',
                'permission_callback' => '__return_true',
            )
        );

    }
);
