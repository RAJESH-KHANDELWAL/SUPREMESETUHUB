<?php
/**
 * Plugin Name: SUPREMESETUHUB Domain & Hosting
 * Description: Displays the public SUPREMESETUHUB domain and hosting service catalog from the FastAPI backend.
 * Version: 1.0.0
 * Requires at least: 6.2
 * Requires PHP: 7.4
 * Author: DR RAJESH KHANDELWAL IBC
 * License: GPL-2.0-or-later
 * Text Domain: supremesetuhub-domain-hosting
 */

if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

final class SUPREMESETUHUB_Domain_Hosting {
    const OPTION = 'supremesetuhub_domain_hosting_options';
    const CATALOG_PATH = '/api/v1/domain-hosting/public/catalog';

    public static function init() {
        add_action( 'admin_menu', array( __CLASS__, 'add_settings_page' ) );
        add_action( 'admin_init', array( __CLASS__, 'register_settings' ) );
        add_shortcode( 'supremesetuhub_domain_hosting', array( __CLASS__, 'render_catalog' ) );
    }

    private static function options() {
        $options = get_option( self::OPTION, array() );
        return is_array( $options ) ? $options : array();
    }

    public static function add_settings_page() {
        add_options_page(
            __( 'SUPREMESETUHUB Domain & Hosting', 'supremesetuhub-domain-hosting' ),
            __( 'SUPREMESETUHUB Domain & Hosting', 'supremesetuhub-domain-hosting' ),
            'manage_options',
            'supremesetuhub-domain-hosting',
            array( __CLASS__, 'render_settings_page' )
        );
    }

    public static function register_settings() {
        register_setting(
            'supremesetuhub_domain_hosting_settings',
            self::OPTION,
            array( 'sanitize_callback' => array( __CLASS__, 'sanitize_options' ) )
        );
    }

    public static function sanitize_options( $input ) {
        if ( ! current_user_can( 'manage_options' ) ) {
            return self::options();
        }

        $url = isset( $input['api_base'] ) ? trim( (string) $input['api_base'] ) : '';
        if ( $url === '' ) {
            return array( 'api_base' => '' );
        }

        $url = esc_url_raw( $url, array( 'https' ) );
        if ( ! $url || strpos( $url, 'https://' ) !== 0 || ! wp_http_validate_url( $url ) ) {
            add_settings_error(
                self::OPTION,
                'invalid_api_base',
                __( 'Enter a valid HTTPS backend base URL.', 'supremesetuhub-domain-hosting' )
            );
            return self::options();
        }

        return array( 'api_base' => untrailingslashit( $url ) );
    }

    public static function render_settings_page() {
        if ( ! current_user_can( 'manage_options' ) ) {
            return;
        }
        $options = self::options();
        $api_base = isset( $options['api_base'] ) ? $options['api_base'] : '';
        ?>
        <div class="wrap">
            <h1><?php esc_html_e( 'SUPREMESETUHUB Domain & Hosting', 'supremesetuhub-domain-hosting' ); ?></h1>
            <p><?php esc_html_e( 'Connect this WordPress site to the public, read-only service catalog. Use HTTPS and do not enter provider passwords or API keys here.', 'supremesetuhub-domain-hosting' ); ?></p>
            <?php settings_errors( self::OPTION ); ?>
            <form method="post" action="options.php">
                <?php settings_fields( 'supremesetuhub_domain_hosting_settings' ); ?>
                <table class="form-table" role="presentation">
                    <tr>
                        <th scope="row"><label for="suph-dh-api-base"><?php esc_html_e( 'Backend HTTPS base URL', 'supremesetuhub-domain-hosting' ); ?></label></th>
                        <td>
                            <input id="suph-dh-api-base" class="regular-text" type="url" name="<?php echo esc_attr( self::OPTION ); ?>[api_base]" value="<?php echo esc_attr( $api_base ); ?>" placeholder="https://your-api.example.com" required />
                            <p class="description"><?php esc_html_e( 'No trailing slash and no endpoint path.', 'supremesetuhub-domain-hosting' ); ?></p>
                        </td>
                    </tr>
                </table>
                <?php submit_button(); ?>
            </form>
            <p><code>[supremesetuhub_domain_hosting]</code></p>
        </div>
        <?php
    }

    private static function get_catalog() {
        $options = self::options();
        $base = isset( $options['api_base'] ) ? trim( $options['api_base'] ) : '';

        if ( ! $base || strpos( $base, 'https://' ) !== 0 || ! wp_http_validate_url( $base ) ) {
            return new WP_Error(
                'suph_dh_not_configured',
                __( 'The domain and hosting catalog is not configured yet. Please contact the site administrator.', 'supremesetuhub-domain-hosting' )
            );
        }

        $response = wp_safe_remote_get(
            $base . self::CATALOG_PATH,
            array(
                'timeout'             => 8,
                'redirection'         => 0,
                'limit_response_size'  => 131072,
                'headers'             => array( 'Accept' => 'application/json' ),
            )
        );

        if ( is_wp_error( $response ) ) {
            return new WP_Error(
                'suph_dh_backend_unavailable',
                __( 'The domain and hosting catalog is temporarily unavailable.', 'supremesetuhub-domain-hosting' )
            );
        }

        $status = (int) wp_remote_retrieve_response_code( $response );
        if ( $status !== 200 ) {
            return new WP_Error(
                'suph_dh_backend_http_error',
                __( 'The domain and hosting catalog is temporarily unavailable.', 'supremesetuhub-domain-hosting' )
            );
        }

        $body = wp_remote_retrieve_body( $response );
        $data = json_decode( $body, true );
        if ( ! is_array( $data ) || empty( $data['success'] ) || ! isset( $data['services'] ) || ! is_array( $data['services'] ) ) {
            return new WP_Error(
                'suph_dh_invalid_response',
                __( 'The catalog returned an invalid response.', 'supremesetuhub-domain-hosting' )
            );
        }

        return $data;
    }

    public static function render_catalog() {
        $catalog = self::get_catalog();
        if ( is_wp_error( $catalog ) ) {
            return '<p class="suph-dh-notice">' . esc_html( $catalog->get_error_message() ) . '</p>';
        }

        $services = $catalog['services'];
        $notice = isset( $catalog['notice'] ) ? (string) $catalog['notice'] : '';
        $html = '<section class="suph-dh-catalog" aria-label="' . esc_attr__( 'Domain and hosting services', 'supremesetuhub-domain-hosting' ) . '">';
        $html .= '<style>.suph-dh-catalog{color:#101828}.suph-dh-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,230px),1fr));gap:16px}.suph-dh-card{border:1px solid #d8e2f0;border-radius:14px;padding:20px;background:#fff}.suph-dh-card h3{margin-top:0}.suph-dh-status{display:inline-block;border-radius:999px;padding:4px 9px;background:#fff4d6;color:#714d00;font-size:.8rem;font-weight:700}.suph-dh-notice{margin-top:18px;padding:14px;border-radius:10px;background:#f2f6ff;color:#344054;font-size:.92rem}</style>';
        $html .= '<div class="suph-dh-grid">';

        foreach ( $services as $service ) {
            if ( ! is_array( $service ) ) {
                continue;
            }
            $name = isset( $service['name'] ) ? sanitize_text_field( (string) $service['name'] ) : '';
            $description = isset( $service['description'] ) ? sanitize_text_field( (string) $service['description'] ) : '';
            $availability = isset( $service['availability'] ) ? sanitize_key( (string) $service['availability'] ) : 'inquiry_only';
            if ( $name === '' ) {
                continue;
            }
            $html .= '<article class="suph-dh-card"><h3>' . esc_html( $name ) . '</h3>';
            $html .= '<p>' . esc_html( $description ) . '</p>';
            $html .= '<p><span class="suph-dh-status">' . esc_html( $availability === 'inquiry_only' ? __( 'Request a quote', 'supremesetuhub-domain-hosting' ) : __( 'Check availability', 'supremesetuhub-domain-hosting' ) ) . '</span></p>';
            $html .= '<p><a href="' . esc_url( home_url( '/contact/' ) ) . '">' . esc_html__( 'Contact us', 'supremesetuhub-domain-hosting' ) . ' →</a></p></article>';
        }

        $html .= '</div>';
        if ( $notice !== '' ) {
            $html .= '<p class="suph-dh-notice">' . esc_html( $notice ) . '</p>';
        }
        $html .= '</section>';
        return $html;
    }
}

SUPREMESETUHUB_Domain_Hosting::init();
