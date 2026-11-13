<?php
/**
 * Plugin Name: SUPREME by SUPREMESETUHUB
 * Description: SUPREME plugin identity and integration manifest.
 * Version: 1.0.0
 * Author: 👑 DR RAJESH KHANDELWAL IBC 👑
 * Text Domain: supreme
 */
if (!defined('ABSPATH')) { exit; }

define('SUPREME_VERSION', '1.0.0');

if (!function_exists('supreme_plugin_manifest')) {
    function supreme_plugin_manifest() {
        return array(
            'slug' => 'supreme',
            'name' => 'SUPREME',
            'display_name' => 'SUPREME by SUPREMESETUHUB',
            'parent_hub' => 'SUPREMESETUHUB',
            'identity_folders' => array('dr_rajesh_khandelwal_ibc', 'dr_rajesh_khandelwal_ibc_official', 'rajesh_khandelwal', 'rajesh_khandelwal_official'),
        );
    }
}

add_action('admin_menu', function () {
    add_menu_page(
        'SUPREME',
        'SUPREME',
        'manage_options',
        'supreme',
        function () {
            if (!current_user_can('manage_options')) { return; }
            echo '<div class="wrap"><h1>SUPREME</h1>';
            echo '<p><strong>SUPREME by SUPREMESETUHUB</strong></p>';
            echo '<p>Identity folders registered: ' . esc_html((string) count(supreme_plugin_manifest()['identity_folders'])) . '</p>';
            echo '</div>';
        },
        'dashicons-admin-generic'
    );
});
