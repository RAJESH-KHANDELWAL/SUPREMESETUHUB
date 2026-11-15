<?php
/**
 * SUPREME Dashboard module.
 * Loaded by the DR RAJESH KHANDELWAL IBC parent plugin; not a separate plugin.
 */
if (!defined('ABSPATH')) { exit; }

if (!function_exists('supreme_dashboard_manifest')) {
    function supreme_dashboard_manifest() {
        return array(
            'module' => 'SUPREME DASHBOARD',
            'parent' => 'DR RAJESH KHANDELWAL IBC',
            'parent_brand' => 'DR RAJESH KHANDELWAL IBC',
        );
    }
}

if (!function_exists('supreme_dashboard_render_page')) {
    function supreme_dashboard_render_page() {
        if (!current_user_can('manage_options')) { return; }

        $identities = array(
            array('RAJESH KHANDELWAL', 'RAJESHKHANDELWAL', 'supreme_identity_rajesh_khandelwal_manifest'),
            array('RAJESH KHANDELWAL OFFICIAL', 'RAJESHKHANDELWALOFFICIAL', 'supreme_identity_rajesh_khandelwal_official_manifest'),
            array('DR RAJESH KHANDELWAL IBC', 'DRRAJESHKHANDELWALIBC', 'supreme_identity_dr_rajesh_khandelwal_ibc_manifest'),
            array('DR RAJESH KHANDELWAL IBC OFFICIAL', 'DRRAJESHKHANDELWALIBCOFFICIAL', 'supreme_identity_dr_rajesh_khandelwal_ibc_official_manifest'),
        );

        echo '<div class="wrap"><h1>👑 SUPREME DASHBOARD 👑</h1>';
        echo '<p>Dashboard module of 👑 DR RAJESH KHANDELWAL IBC 👑.</p>';
        echo '<h2>👑 FOUR BRAND PROFILES 👑</h2>';
        echo '<table class="widefat striped"><thead><tr><th>Brand Profile</th><th>Identity ID</th><th>Module Status</th></tr></thead><tbody>';
        foreach ($identities as $identity) {
            $loaded = function_exists($identity[2]);
            echo '<tr><td><strong>👑 ' . esc_html($identity[0]) . ' 👑</strong></td>';
            echo '<td><code>' . esc_html($identity[1]) . '</code></td>';
            echo '<td>' . esc_html($loaded ? 'Loaded' : 'Not loaded') . '</td></tr>';
        }
        echo '</tbody></table>';
        echo '<p class="description">These are four logical brand profiles managed inside this IBC plugin; they are not four separate WordPress plugins.</p></div>';
    }
}

add_action('admin_menu', function () {
    add_submenu_page(
        'dr-rajesh-khandelwal-ibc-dashboard',
        '👑 SUPREME DASHBOARD 👑',
        '👑 SUPREME DASHBOARD 👑',
        'manage_options',
        'supreme-dashboard',
        'supreme_dashboard_render_page'
    );
}, 99);
