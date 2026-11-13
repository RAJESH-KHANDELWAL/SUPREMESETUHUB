<?php
/**
 * Plugin Name: SUPREMESETUHUB
 * Plugin URI: https://github.com/RAJESH-KHANDELWAL/SUPREMESETUHUB
 * Description: SUPREMESETUHUB — SUPREME system and SUPREME ECOSYSTEM WordPress connector.
 * Version: 1.1.0
 * Author: 👑 DR RAJESH KHANDELWAL IBC 👑
 * Author URI: https://rajeshkhandelwalofficial.com
 * License: GPL-2.0-or-later
 * Text Domain: supremesetuhub
 */
if (!defined('ABSPATH')) { exit; }

define('SUPREMESETUHUB_VERSION', '1.1.0');
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
            echo '<p>SUPREME system and SUPREME ECOSYSTEM WordPress connector.</p>';
            echo '<p>Connector status: <strong>Registered</strong></p></div>';
        },
        'dashicons-networking'
    );
});
