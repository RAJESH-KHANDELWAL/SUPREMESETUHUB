<?php
/**
 * Plugin Name: SUPREME Owner Admin
 * Description: Owner-only WordPress admin landing page for the SUPREME platform.
 * Version: 1.0.2
 * Requires at least: 6.0
 * Requires PHP: 7.4
 * License: GPL-2.0-or-later
 */

defined( 'ABSPATH' ) || exit;

/**
 * Configure the owner's exact WordPress user ID in wp-config.php:
 * define( 'SUPREME_OWNER_WP_USER_ID', 123 );
 * Replace 123 with the intended owner's actual WordPress user ID.
 * Access fails closed if this constant is missing or invalid.
 */
final class Supreme_Owner_Admin_Plugin {
    private function is_authorized_owner() {
        return defined( 'SUPREME_OWNER_WP_USER_ID' )
            && is_numeric( SUPREME_OWNER_WP_USER_ID )
            && (int) SUPREME_OWNER_WP_USER_ID > 0
            && get_current_user_id() === (int) SUPREME_OWNER_WP_USER_ID
            && current_user_can( 'manage_options' );
    }

    public function __construct() {
        add_action( 'admin_menu', array( $this, 'register_menu' ) );
    }

    public function register_menu() {
        if ( ! $this->is_authorized_owner() ) {
            return;
        }
        add_menu_page(
            'SUPREME Owner Admin',
            'SUPREME Owner Admin',
            'manage_options',
            'supreme-owner-admin',
            array( $this, 'render_page' ),
            'dashicons-shield-alt',
            3
        );
    }

    public function render_page() {
        if ( ! $this->is_authorized_owner() ) {
            wp_die( esc_html__( 'Access denied. This control panel is restricted to the configured SUPREME owner account.', 'supreme-owner-admin' ), '', array( 'response' => 403 ) );
        }
        ?>
        <div class="wrap">
            <h1><?php echo esc_html__( 'SUPREME Owner Admin', 'supreme-owner-admin' ); ?></h1>
            <p><?php echo esc_html__( 'Private owner-only control-panel landing page for the SUPREME platform.', 'supreme-owner-admin' ); ?></p>
            <?php if ( ! defined( 'SUPREME_OWNER_WP_USER_ID' ) || ! is_numeric( SUPREME_OWNER_WP_USER_ID ) || (int) SUPREME_OWNER_WP_USER_ID < 1 ) : ?>
                <div class="notice notice-error"><p><?php echo esc_html__( 'Owner access is locked. Configure SUPREME_OWNER_WP_USER_ID in wp-config.php with the intended owner user ID.', 'supreme-owner-admin' ); ?></p></div>
            <?php else : ?>
                <div class="notice notice-success"><p><?php echo esc_html__( 'Owner account match verified for this WordPress session. Backend/API connectivity is not configured or verified by this plugin.', 'supreme-owner-admin' ); ?></p></div>
            <?php endif; ?>
            <div class="notice notice-info"><p><strong>🔐 Password Manager:</strong> <a href="https://rajesh-khandelwal.github.io/SUPREMESETUHUB/supreme/supreme-ecosystem/password-manager/index.html" target="_blank" rel="noopener noreferrer">Open encrypted SUPREME Owner Admin Password Manager</a>. CSV and vault data stay in your browser; never upload plaintext passwords to GitHub.</p></div>
            <h2><?php echo esc_html__( 'Control areas', 'supreme-owner-admin' ); ?></h2>
            <ul>
                <li><?php echo esc_html__( 'Platform identity and owner governance', 'supreme-owner-admin' ); ?></li>
                <li><?php echo esc_html__( 'Security, roles, and audit readiness', 'supreme-owner-admin' ); ?></li>
                <li><?php echo esc_html__( 'WordPress site registry and integration readiness', 'supreme-owner-admin' ); ?></li>
                <li><?php echo esc_html__( 'SUPREME ECOSYSTEM control-plane link readiness', 'supreme-owner-admin' ); ?></li>
            </ul>
            <p><strong><?php echo esc_html__( 'Status:', 'supreme-owner-admin' ); ?></strong> <?php echo esc_html__( 'Owner-only dashboard shell; live backend actions are not yet wired.', 'supreme-owner-admin' ); ?></p>
        </div>
        <?php
    }
}

new Supreme_Owner_Admin_Plugin();
