<?php
/**
 * Plugin Name: 👑 DR RAJESH KHANDELWAL IBC 👑
 * Plugin URI: https://www.rajeshkhandelwal.com
 * Plugin URI: https://www.rajeshkhandelwalofficial.com
 * Plugin URI: https://www.drrajeshkhandelwalibc.com
 * Plugin URI: https://www.drrajeshkhandelwalibcofficial.com
 * Description: 👑 DR RAJESH KHANDELWAL IBC 👑 — Personal Supreme + WordPress Home integration.
 * Version: 1.3.1
 * Author: 👑 DR RAJESH KHANDELWAL IBC 👑
 * Author URI: https://www.rajeshkhandelwal.com
 * Plugin URI: https://www.rajeshkhandelwalofficial.com
 * Plugin URI: https://www.drrajeshkhandelwalibc.com
 * Plugin URI: https://www.drrajeshkhandelwalibcofficial.com
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
    '1.3.1'
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
    'https://raw.githubusercontent.com/RAJESH-KHANDELWAL/SUPREMESETUHUB/main/frontend/supreme/supreme-ecosystem/home-html.html'
);

define(
    'DR_RAJESH_KHANDELWAL_IBC_HOME_CSS_URL',
    'https://raw.githubusercontent.com/RAJESH-KHANDELWAL/SUPREMESETUHUB/main/frontend/supreme/supreme-ecosystem/home-css.css'
);

define(
    'DR_RAJESH_KHANDELWAL_IBC_HOME_JS_URL',
    'https://raw.githubusercontent.com/RAJESH-KHANDELWAL/SUPREMESETUHUB/main/frontend/supreme/supreme-ecosystem/home-js.js'
);

define(
    'DR_RAJESH_KHANDELWAL_IBC_HOME_URL',
    'https://rajesh-khandelwal.github.io/SUPREMESETUHUB/supreme/home.html'
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
| SUPREME HOME SHORTCODE — RENDER GITHUB HTML INLINE
|--------------------------------------------------------------------------
|
| Use:
| [dr_rajesh_supreme_home]
|
| Loads home-html.html, home-css.css and home-js.js directly from GitHub into this WordPress page.
|
*/

function dr_rajesh_khandelwal_ibc_supreme_home() {
    /*
     * Render the actual HTML maintained in GitHub directly inside WordPress.
     * No Render URL, no GitHub blob viewer, and no iframe.
     */
    $html_response = wp_remote_get(DR_RAJESH_KHANDELWAL_IBC_BACKEND_URL, array('timeout' => 15, 'redirection' => 3));
    $css_response  = wp_remote_get(DR_RAJESH_KHANDELWAL_IBC_HOME_CSS_URL, array('timeout' => 15, 'redirection' => 3));
    $js_response   = wp_remote_get(DR_RAJESH_KHANDELWAL_IBC_HOME_JS_URL, array('timeout' => 15, 'redirection' => 3));

    if (is_wp_error($html_response) || wp_remote_retrieve_response_code($html_response) !== 200) {
        return '<section id="dr-rajesh-supreme-home-error"><p>SUPREME HOME GitHub source could not be loaded. Please try again shortly.</p></section>';
    }

    $home_html = wp_remote_retrieve_body($html_response);
    $home_css  = (!is_wp_error($css_response) && wp_remote_retrieve_response_code($css_response) === 200) ? wp_remote_retrieve_body($css_response) : '';
    $home_js   = (!is_wp_error($js_response) && wp_remote_retrieve_response_code($js_response) === 200) ? wp_remote_retrieve_body($js_response) : '';

    // Replace old Render API navigation links so the page never routes back to Render.
    $home_html = str_replace(
        array(
            'href="/api/v1/frontend/supreme"',
            'href="/api/v1/frontend/supreme/about"',
            'href="/api/v1/frontend/supreme/contact"'
        ),
        array(
            'href="https://rajeshkhandelwalofficial.com/"',
            'href="https://rajeshkhandelwalofficial.com/about/"',
            'href="https://rajeshkhandelwalofficial.com/contact/"'
        ),
        $home_html
    );

    $output  = '<div id="SUPREMESETUHUB-HOME" class="SUPREMESETUHUB-HOME" style="width:100%;max-width:100%;min-width:0;box-sizing:border-box;overflow-x:clip;">';
    if ($home_css !== '') {
        $output .= '<style id="dr-rajesh-supreme-home-css">' . $home_css . '</style>';
    }
    $output .= $home_html;
    if ($home_js !== '') {
        $output .= '<script id="dr-rajesh-supreme-home-js">' . $home_js . '</script>';
    }
    $output .= '</div>';

    return $output;
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
