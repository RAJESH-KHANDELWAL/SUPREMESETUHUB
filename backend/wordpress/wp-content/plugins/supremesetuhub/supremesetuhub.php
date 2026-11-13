<?php
/**
 * Plugin Name: SUPREMESETUHUB
 * Description: Central WordPress connector for SUPREME by SUPREMESETUHUB and SUPREME ECOSYSTEM by SUPREMESETUHUB.
 * Version: 1.2.0
 * Author: 👑 DR RAJESH KHANDELWAL IBC 👑
 * Text Domain: supremesetuhub
 */
if (!defined('ABSPATH')) { exit; }

define('SUPREMESETUHUB_VERSION', '1.2.0');
define('SUPREMESETUHUB_DIR', plugin_dir_path(__FILE__));
define('SUPREMESETUHUB_URL', plugin_dir_url(__FILE__));

require_once SUPREMESETUHUB_DIR . 'wordpress_connector.php';

register_activation_hook(__FILE__, function () {
    update_option('supremesetuhub_plugin_version', SUPREMESETUHUB_VERSION);
});

add_action('admin_menu', function () {
    add_menu_page(
        'SUPREMESETUHUB',
        'SUPREMESETUHUB',
        'manage_options',
        'supremesetuhub',
        function () {
            if (!current_user_can('manage_options')) { return; }
            echo '<div class="wrap"><h1>SUPREMESETUHUB</h1>';
            echo '<h2>👑 DR RAJESH KHANDELWAL IBC 👑</h2>';
            echo '<p><strong>SUPREME by SUPREMESETUHUB</strong></p>';
            echo '<p><strong>SUPREME ECOSYSTEM by SUPREMESETUHUB</strong></p>';
            echo '<p>Central WordPress connector status: Registered</p></div>';
        },
        'dashicons-networking'
    );
});
