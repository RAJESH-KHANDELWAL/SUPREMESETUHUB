<?php
/**
 * Plugin Name: 👑 DR RAJESH KHANDELWAL IBC 👑
 * Plugin URI: https://www.rajeshkhandelwal.com
 * Description: 👑 DR RAJESH KHANDELWAL IBC 👑 — Private personal control and integration plugin.
 * Version: 1.0.0
 * Author: 👑 DR RAJESH KHANDELWAL IBC 👑
 * Author URI: https://www.rajeshkhandelwal.com
 * License: GPL-2.0-or-later
 * Text Domain: dr-rajesh-khandelwal-ibc
 */

if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

define( 'DR_RAJESH_KHANDELWAL_IBC_VERSION', '1.0.0' );
define( 'DR_RAJESH_KHANDELWAL_IBC_FILE', __FILE__ );
define( 'DR_RAJESH_KHANDELWAL_IBC_DIR', plugin_dir_path( __FILE__ ) );

/**
 * Plugin activation.
 */
function dr_rajesh_khandelwal_ibc_activate() {

    update_option(
        'dr_rajesh_khandelwal_ibc_status',
        'active'
    );

    update_option(
        'dr_rajesh_khandelwal_ibc_version',
        DR_RAJESH_KHANDELWAL_IBC_VERSION
    );
}

register_activation_hook(
    __FILE__,
    'dr_rajesh_khandelwal_ibc_activate'
);

/**
 * Plugin deactivation.
 */
function dr_rajesh_khandelwal_ibc_deactivate() {

    update_option(
        'dr_rajesh_khandelwal_ibc_status',
        'inactive'
    );
}

register_deactivation_hook(
    __FILE__,
    'dr_rajesh_khandelwal_ibc_deactivate'
);

/**
 * Basic REST API status endpoint.
 */
function dr_rajesh_khandelwal_ibc_status() {

    return array(
        'success'       => true,
        'plugin'        => 'DR RAJESH KHANDELWAL IBC',
        'version'       => DR_RAJESH_KHANDELWAL_IBC_VERSION,
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
            'dr-rajesh-khandelwal-ibc/v1',
            '/status',
            array(
                'methods'             => 'GET',
                'callback'            => 'dr_rajesh_khandelwal_ibc_status',
                'permission_callback' => '__return_true',
            )
        );

    }
);
