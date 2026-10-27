<?php
/**
 * Plugin Name: SUPREME Owner Admin
 * Description: A private WordPress admin landing page for the SUPREME platform owner.
 * Version: 1.0.0
 * Requires at least: 6.0
 * Requires PHP: 7.4
 * License: GPL-2.0-or-later
 */

defined( 'ABSPATH' ) || exit;

final class Supreme_Owner_Admin_Plugin {
    public function __construct() {
        add_action( 'admin_menu', array( $this, 'register_menu' ) );
    }

    public function register_menu() {
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
        if ( ! current_user_can( 'manage_options' ) ) {
            wp_die( esc_html__( 'You are not allowed to access this page.', 'supreme-owner-admin' ) );
        }
        ?>
        <div class="wrap">
            <h1><?php echo esc_html__( 'SUPREME Owner Admin', 'supreme-owner-admin' ); ?></h1>
            <p><?php echo esc_html__( 'Private WordPress control-panel landing page for the SUPREME platform owner.', 'supreme-owner-admin' ); ?></p>
            <div class="notice notice-info"><p><?php echo esc_html__( 'WordPress administrator access is checked locally. Backend/API connectivity is not configured or verified by this plugin.', 'supreme-owner-admin' ); ?></p></div>
            <h2><?php echo esc_html__( 'Control areas', 'supreme-owner-admin' ); ?></h2>
            <ul>
                <li><?php echo esc_html__( 'Platform identity and owner governance', 'supreme-owner-admin' ); ?></li>
                <li><?php echo esc_html__( 'Security, roles, and audit readiness', 'supreme-owner-admin' ); ?></li>
                <li><?php echo esc_html__( 'WordPress site registry and integration readiness', 'supreme-owner-admin' ); ?></li>
                <li><?php echo esc_html__( 'SUPREME ECOSYSTEM control-plane link readiness', 'supreme-owner-admin' ); ?></li>
            </ul>
            <p><strong><?php echo esc_html__( 'Status:', 'supreme-owner-admin' ); ?></strong> <?php echo esc_html__( 'Dashboard shell installed; live backend actions are not yet wired.', 'supreme-owner-admin' ); ?></p>
        </div>
        <?php
    }
}

new Supreme_Owner_Admin_Plugin();
