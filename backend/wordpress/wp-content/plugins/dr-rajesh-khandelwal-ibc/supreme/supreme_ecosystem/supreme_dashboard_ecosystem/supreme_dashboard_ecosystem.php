<?php
/**
 * SUPREME ECOSYSTEM Dashboard module.
 * Loaded by supreme_ecosystem.php; not a separate WordPress plugin.
 */
if (!defined('ABSPATH')) { exit; }

if (!function_exists('supreme_dashboard_ecosystem_manifest')) {
    function supreme_dashboard_ecosystem_manifest() {
        return array(
            'module' => 'SUPREME DASHBOARD ECOSYSTEM',
            'parent' => 'SUPREME ECOSYSTEM',
            'root_module' => 'SUPREME',
            'parent_brand' => 'DR RAJESH KHANDELWAL IBC',
        );
    }
}

if (!function_exists('supreme_dashboard_ecosystem_render_page')) {
    function supreme_dashboard_ecosystem_render_page() {
        if (!current_user_can('manage_options')) { return; }
        $manifest = supreme_dashboard_ecosystem_manifest();
        echo '<div class="wrap"><h1>👑 SUPREME ECOSYSTEM DASHBOARD 👑</h1>';
        echo '<p><strong>Parent:</strong> ' . esc_html($manifest['parent']) . ' → ' . esc_html($manifest['root_module']) . '</p>';
        echo '<p><strong>Owner brand:</strong> ' . esc_html($manifest['parent_brand']) . '</p>';
        echo '<h2>Dashboard areas</h2><ul>';
        foreach (array(
            'Owner Admin & Governance',
            'Four Brand Profiles',
            'Google / Microsoft / WhatsApp Integrations',
            'Business & Partner Programs',
            'AI Ecosystem',
            'API & Capabilities',
            'Control Status & Commands',
        ) as $area) {
            echo '<li>' . esc_html($area) . '</li>';
        }
        echo '</ul>';
        echo '<h2>Backend API</h2><p><code>/api/v1/supreme-ecosystem</code></p>';
        echo '<p class="description">This WordPress page confirms the module structure only. API authentication, provider connections, database status, and live service health must be verified against the running backend; they are not represented as connected here.</p>';
        echo '</div>';
    }
}

add_action('admin_menu', function () {
    add_submenu_page(
        'dr-rajesh-khandelwal-ibc-dashboard',
        '👑 SUPREME ECOSYSTEM DASHBOARD 👑',
        '👑 SUPREME ECOSYSTEM DASHBOARD 👑',
        'manage_options',
        'supreme-ecosystem-dashboard',
        'supreme_dashboard_ecosystem_render_page'
    );
}, 100);
