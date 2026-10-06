<?php
/**
 * Plugin Name: 👑 DR RAJESH KHANDELWAL IBC 👑
 * Plugin URI: https://www.rajeshkhandelwal.com
 * Description: 👑 DR RAJESH KHANDELWAL IBC 👑 — Personal Supreme + WordPress Home integration.
 * Version: 1.1.0
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
    '1.1.0'
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
| SUPREME HOME SHORTCODE
|--------------------------------------------------------------------------
|
| Use:
|
| [dr_rajesh_supreme_home]
|
| This displays the actual SUPREME Home Page inside WordPress.
|
*/

function dr_rajesh_khandelwal_ibc_supreme_home() {

    $home_url =
        esc_url(
            DR_RAJESH_KHANDELWAL_IBC_HOME_URL
        );


    ob_start();

    ?>

    <div
        id="dr-rajesh-supreme-home"
        style="
            width:100%;
            max-width:100%;
            margin:0 auto;
            padding:0;
            overflow:hidden;
            background:#ffffff;
        "
    >

        <iframe
            id="dr-rajesh-supreme-home-frame"
            src="<?php echo $home_url; ?>"
            title="👑 DR RAJESH KHANDELWAL IBC 👑 SUPREME HOME"
            loading="eager"
            style="
                display:block;
                width:100%;
                min-height:100vh;
                height:100vh;
                border:0;
                margin:0;
                padding:0;
                background:#ffffff;
            "
        ></iframe>

    </div>

    <script>

    (function(){

        const frame =
            document.getElementById(
                'dr-rajesh-supreme-home-frame'
            );

        if (!frame) {
            return;
        }

        function resizeFrame() {

            try {

                if (
                    frame.contentWindow &&
                    frame.contentDocument
                ) {

                    const body =
                        frame.contentDocument.body;

                    const html =
                        frame.contentDocument.documentElement;

                    const height =
                        Math.max(
                            body
                                ? body.scrollHeight
                                : 0,

                            body
                                ? body.offsetHeight
                                : 0,

                            html
                                ? html.clientHeight
                                : 0,

                            html
                                ? html.scrollHeight
                                : 0,

                            html
                                ? html.offsetHeight
                                : 0
                        );

                    if (height > 0) {

                        frame.style.height =
                            height + 'px';

                    }

                }

            }
            catch (error) {

                /*
                 * Cross-origin protection may prevent
                 * reading iframe height.
                 *
                 * The fixed 100vh height remains active.
                 */

            }

        }

        frame.addEventListener(
            'load',
            function(){

                resizeFrame();

                setTimeout(
                    resizeFrame,
                    1000
                );

                setTimeout(
                    resizeFrame,
                    3000
                );

            }
        );

        window.addEventListener(
            'resize',
            resizeFrame
        );

    })();

    </script>

    <?php

    return ob_get_clean();
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
