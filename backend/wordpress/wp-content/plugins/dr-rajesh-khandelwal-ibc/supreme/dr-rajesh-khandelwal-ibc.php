<?php
/**
 * Brand implementation module loaded by the parent WordPress plugin.
 * This file intentionally has no Plugin Name header to prevent duplicate plugin registration.
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

define('DR_RAJESH_KHANDELWAL_IBC_DIR', dirname(plugin_dir_path(__FILE__)) . '/');

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
    'https://rajeshkhandelwalofficial.com/'
);


/*
|--------------------------------------------------------------------------
| ACTIVATION
|--------------------------------------------------------------------------
*/

function dr_rajesh_khandelwal_ibc_activate() {
    update_option('dr_rajesh_khandelwal_ibc_status', 'active');
    update_option('dr_rajesh_khandelwal_ibc_version', DR_RAJESH_KHANDELWAL_IBC_VERSION);
}


/*
|--------------------------------------------------------------------------
| DEACTIVATION
|--------------------------------------------------------------------------
*/

function dr_rajesh_khandelwal_ibc_deactivate() {
    update_option('dr_rajesh_khandelwal_ibc_status', 'inactive');
}


/*
|--------------------------------------------------------------------------
| TWO-PLUGIN INTEGRATION STATUS
|--------------------------------------------------------------------------
*/

function dr_rajesh_khandelwal_ibc_integration_status() {
    $active_plugins = (array) get_option('active_plugins', array());
    $network_active = (array) get_site_option('active_sitewide_plugins', array());
    $hub_basename = 'supremesetuhub/supremesetuhub.php';

    return array(
        'contract' => 'supremesetuhub-wordpress-v1',
        'hub_plugin' => array(
            'name' => 'SUPREMESETUHUB',
            'plugin_basename' => $hub_basename,
            'active' => in_array($hub_basename, $active_plugins, true) || isset($network_active[$hub_basename]),
        ),
        'brand_plugin' => array(
            'name' => 'DR RAJESH KHANDELWAL IBC',
            'plugin_basename' => 'dr-rajesh-khandelwal-ibc/dr-rajesh-khandelwal-ibc.php',
            'active' => true,
        ),
        'modules' => array(
            'supreme' => 'loaded-through-ibc-plugin',
            'supreme_ecosystem' => 'loaded-through-ibc-plugin',
        ),
    );
}


/*
|--------------------------------------------------------------------------
| STATUS API
|--------------------------------------------------------------------------
*/

function dr_rajesh_khandelwal_ibc_status() {
    return array(
        'success' => true,
        'plugin' => 'DR RAJESH KHANDELWAL IBC',
        'version' => DR_RAJESH_KHANDELWAL_IBC_VERSION,
        'status' => 'active',
        'wordpress' => true,
        'github_ready' => true,
        'backend_ready' => true,
        'supreme_home' => true,
        'home_url' => DR_RAJESH_KHANDELWAL_IBC_HOME_URL,
        'integration' => dr_rajesh_khandelwal_ibc_integration_status(),
    );
}


/*
|--------------------------------------------------------------------------
| SUPREME HOME SHORTCODE — RENDER GITHUB HTML INLINE
|--------------------------------------------------------------------------
*/

function dr_rajesh_khandelwal_ibc_supreme_home() {
    $html_response = wp_remote_get(DR_RAJESH_KHANDELWAL_IBC_BACKEND_URL, array('timeout' => 15, 'redirection' => 3));
    $css_response  = wp_remote_get(DR_RAJESH_KHANDELWAL_IBC_HOME_CSS_URL, array('timeout' => 15, 'redirection' => 3));
    $js_response   = wp_remote_get(DR_RAJESH_KHANDELWAL_IBC_HOME_JS_URL, array('timeout' => 15, 'redirection' => 3));

    if (is_wp_error($html_response) || wp_remote_retrieve_response_code($html_response) !== 200) {
        return '<section id="dr-rajesh-supreme-home-error"><p>SUPREME HOME GitHub source could not be loaded. Please try again shortly.</p></section>';
    }

    $home_html = wp_remote_retrieve_body($html_response);
    $home_css  = (!is_wp_error($css_response) && wp_remote_retrieve_response_code($css_response) === 200) ? wp_remote_retrieve_body($css_response) : '';
    $home_js   = (!is_wp_error($js_response) && wp_remote_retrieve_response_code($js_response) === 200) ? wp_remote_retrieve_body($js_response) : '';

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

add_shortcode('dr_rajesh_supreme_home', 'dr_rajesh_khandelwal_ibc_supreme_home');


/*
|--------------------------------------------------------------------------
| REST API
|--------------------------------------------------------------------------
*/

add_action('rest_api_init', function () {
    register_rest_route(
        'dr-rajesh-khandelwal-ibc/v1',
        '/status',
        array(
            'methods' => 'GET',
            'callback' => 'dr_rajesh_khandelwal_ibc_status',
            'permission_callback' => '__return_true',
        )
    );
});


// Load the SUPREME module and its ecosystem submodule through one parent plugin.
require_once __DIR__ . '/supreme.php';
