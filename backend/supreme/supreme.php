<?php
/**
 * Plugin Name: 👑 SUPREMESETUHUB 👑
 * Description: Real WordPress ↔ SUPREMESETUHUB integration layer.
 * Version: 1.0.0
 * Author: 👑 DR RAJESH KHANDELWAL IBC 👑
 */

if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

final class SupremeSetuHub {

    const VERSION = '1.0.0';

    public function __construct() {

        add_action(
            'rest_api_init',
            array( $this, 'register_rest_routes' )
        );

        add_action(
            'admin_menu',
            array( $this, 'register_admin_menu' )
        );
    }

    /**
     * SUPREME admin menu
     */
    public function register_admin_menu() {

        add_menu_page(
            '👑 SUPREMESETUHUB 👑',
            '👑 SUPREMESETUHUB 👑',
            'manage_options',
            'supreme-setuhub',
            array( $this, 'dashboard' ),
            'dashicons-admin-generic',
            2
        );
    }

    /**
     * REST API routes
     */
    public function register_rest_routes() {

        register_rest_route(
            'supreme/v1',
            '/status',
            array(
                'methods'  => WP_REST_Server::READABLE,
                'callback' => array( $this, 'status' ),
                'permission_callback' => array(
                    $this,
                    'permission'
                ),
            )
        );

        register_rest_route(
            'supreme/v1',
            '/plugins',
            array(
                'methods'  => WP_REST_Server::READABLE,
                'callback' => array( $this, 'plugins' ),
                'permission_callback' => array(
                    $this,
                    'permission'
                ),
            )
        );
    }

    /**
     * Permission check
     */
    public function permission() {

        return current_user_can( 'manage_options' );
    }

    /**
     * System status
     */
    public function status() {

        return rest_ensure_response(
            array(
                'success' => true,
                'system'  => 'SUPREMESETUHUB',
                'version' => self::VERSION,
                'wordpress' => get_bloginfo( 'version' ),
                'site' => home_url(),
                'connected' => true,
            )
        );
    }

    /**
     * REAL installed WordPress plugins
     */
    public function plugins() {

        if ( ! function_exists( 'get_plugins' ) ) {
            require_once ABSPATH . 'wp-admin/includes/plugin.php';
        }

        $all_plugins = get_plugins();
        $active      = (array) get_option(
            'active_plugins',
            array()
        );

        $plugins = array();

        foreach ( $all_plugins as $file => $plugin ) {

            $plugins[] = array(
                'file'       => $file,
                'name'       => $plugin['Name'],
                'version'    => $plugin['Version'],
                'author'     => wp_strip_all_tags(
                    $plugin['Author']
                ),
                'description'=> wp_strip_all_tags(
                    $plugin['Description']
                ),
                'active'     => in_array(
                    $file,
                    $active,
                    true
                ),
                'plugin_uri' => $plugin['PluginURI'],
            );
        }

        return rest_ensure_response(
            array(
                'success' => true,
                'count'   => count( $plugins ),
                'plugins' => $plugins,
            )
        );
    }

    /**
     * Supreme dashboard
     */
    public function dashboard() {

        if ( ! current_user_can( 'manage_options' ) ) {
            wp_die(
                esc_html__(
                    'You do not have permission to access SUPREMESETUHUB.'
                )
            );
        }

        ?>
        <div class="wrap">

            <h1 style="
                text-align:center;
                font-weight:800;
                margin:30px 0;
            ">
                👑 DR RAJESH KHANDELWAL IBC 👑
            </h1>

            <h2 style="
                text-align:center;
                font-weight:800;
                margin:20px 0 35px;
            ">
                👑 SUPREME DASHBOARD 👑
            </h2>

            <div style="
                max-width:1100px;
                margin:auto;
                display:grid;
                grid-template-columns:
                    repeat(auto-fit,minmax(220px,1fr));
                gap:20px;
            ">

                <div style="
                    padding:25px;
                    border:1px solid #ddd;
                    border-radius:12px;
                    background:#fff;
                ">
                    <h2>🧩 PLUGINS</h2>
                    <p>
                        Real WordPress installed plugins.
                    </p>

                    <a
                        class="button button-primary"
                        href="<?php
                            echo esc_url(
                                admin_url( 'plugins.php' )
                            );
                        ?>"
                    >
                        OPEN PLUGINS
                    </a>
                </div>

                <div style="
                    padding:25px;
                    border:1px solid #ddd;
                    border-radius:12px;
                    background:#fff;
                ">
                    <h2>➕ ADD PLUGINS</h2>
                    <p>
                        WordPress official plugin directory.
                    </p>

                    <a
                        class="button button-primary"
                        href="<?php
                            echo esc_url(
                                admin_url(
                                    'plugin-install.php'
                                )
                            );
                        ?>"
                    >
                        ADD PLUGINS
                    </a>
                </div>

                <div style="
                    padding:25px;
                    border:1px solid #ddd;
                    border-radius:12px;
                    background:#fff;
                ">
                    <h2>📝 PLUGIN EDITOR</h2>
                    <p>
                        Administrator-only plugin editor.
                    </p>

                    <a
                        class="button"
                        href="<?php
                            echo esc_url(
                                admin_url(
                                    'plugin-editor.php'
                                )
                            );
                        ?>"
                    >
                        OPEN EDITOR
                    </a>
                </div>

                <div style="
                    padding:25px;
                    border:1px solid #ddd;
                    border-radius:12px;
                    background:#fff;
                ">
                    <h2>🌐 GITHUB</h2>
                    <p>
                        SUPREMESETUHUB source repository.
                    </p>

                    <strong>
                        SOURCE CONNECTOR
                    </strong>
                </div>

            </div>

        </div>
        <?php
    }
}

new SupremeSetuHub();
