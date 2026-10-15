<?php
/**
 * Plugin Name: 👑 DR RAJESH KHANDELWAL IBC 👑
 * Plugin URI: https://www.rajeshkhandelwal.com
 * Description: 👑 DR RAJESH KHANDELWAL IBC 👑 — Personal Supreme + WordPress Home integration.
 * Version: 1.3.0
 * Author: 👑 DR RAJESH KHANDELWAL IBC 👑
 * Author URI: https://www.rajeshkhandelwal.com
 * License: GPL-2.0-or-later
 * Text Domain: dr-rajesh-khandelwal-ibc
 */

if ( ! defined( 'ABSPATH' ) ) {
    exit;
}


/*
|--------------------------------------------------------------------------
| CONSTANTS
|--------------------------------------------------------------------------
*/

define(
    'DR_RAJESH_KHANDELWAL_IBC_VERSION',
    '1.3.0'
);

define(
    'DR_RAJESH_KHANDELWAL_IBC_FILE',
    __FILE__
);

define(
    'DR_RAJESH_KHANDELWAL_IBC_DIR',
    plugin_dir_path( __FILE__ )
);

define(
    'DR_RAJESH_KHANDELWAL_IBC_BACKEND_URL',
    'https://supremesetuhub-3v4e.onrender.com'
);

define(
    'DR_RAJESH_KHANDELWAL_IBC_HOME_URL',
    'https://supremesetuhub-3v4e.onrender.com/api/v1/frontend/supreme'
);


/*
|--------------------------------------------------------------------------
| ACTIVATION
|--------------------------------------------------------------------------
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


/*
|--------------------------------------------------------------------------
| DEACTIVATION
|--------------------------------------------------------------------------
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


/*
|--------------------------------------------------------------------------
| STATUS API
|--------------------------------------------------------------------------
*/

function dr_rajesh_khandelwal_ibc_status() {

    return array(

        'success'       => true,

        'plugin'        =>
            '👑 DR RAJESH KHANDELWAL IBC 👑',

        'version'       =>
            DR_RAJESH_KHANDELWAL_IBC_VERSION,

        'status'        =>
            'active',

        'wordpress'     =>
            true,

        'github_ready'  =>
            true,

        'backend_ready' =>
            true,

        'supreme_home'  =>
            true,

        'home_url'      =>
            DR_RAJESH_KHANDELWAL_IBC_HOME_URL,

    );
}


/*
|--------------------------------------------------------------------------
| SUPREME HOME SHORTCODE — DIRECT PAGE LINK
|--------------------------------------------------------------------------
|
| Use:
| [dr_rajesh_supreme_home]
|
| The Home page opens as a normal page so there is no nested scroll area.
|
*/

function dr_rajesh_khandelwal_ibc_supreme_home() {
    $home_url = esc_url(DR_RAJESH_KHANDELWAL_IBC_HOME_URL);
    $html  = '<section id="dr-rajesh-supreme-home" style="box-sizing:border-box;width:100%;max-width:100%;margin:0 auto;padding:clamp(24px,5vw,64px);background:#fff;color:#101828;border:1px solid #e5e7eb;border-radius:20px;text-align:center;">';
    $html .= '<div style="font-size:clamp(1.6rem,4vw,3rem);font-weight:900;line-height:1.2;">👑 DR RAJESH KHANDELWAL IBC 👑</div>';
    $html .= '<h1 style="font-size:clamp(1.3rem,3vw,2rem);margin:18px 0 10px;">SUPREME HOME</h1>';
    $html .= '<p style="max-width:720px;margin:0 auto 22px;line-height:1.7;">Open the live SUPREME Home page directly. It uses the full browser page instead of an embedded frame, avoiding a second internal scrollbar.</p>';
    $html .= '<a href="' . $home_url . '" style="display:inline-block;max-width:100%;box-sizing:border-box;padding:13px 20px;border-radius:12px;background:#0b5cff;color:#fff;text-decoration:none;font-weight:800;">🌍 OPEN SUPREME HOME</a>';
    $html .= '</section>';
    return $html;
}


add_shortcode(
    'dr_rajesh_supreme_home',
    'dr_rajesh_khandelwal_ibc_supreme_home'
);


/*
|--------------------------------------------------------------------------
| REST API
|--------------------------------------------------------------------------
*/

add_action(
    'rest_api_init',
    function () {

        register_rest_route(
            'dr-rajesh-khandelwal-ibc/v1',
            '/status',
            array(

                'methods' =>
                    'GET',

                'callback' =>
                    'dr_rajesh_khandelwal_ibc_status',

                'permission_callback' =>
                    '__return_true',

            )
        );

    }
);
