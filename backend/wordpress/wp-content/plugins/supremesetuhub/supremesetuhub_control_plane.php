<?php
/**
 * Shared owner-only database and FTP control panel for the first-party plugins.
 * Backend credentials stay on the server; only a bearer token is stored in a
 * non-autoloaded WordPress option and sent over HTTPS to the private API.
 */
if (!defined('ABSPATH')) { exit; }

if (!function_exists('supremesetuhub_control_plane_request')) {
    function supremesetuhub_control_plane_request($path, $method = 'GET', $body = null) {
        $base = untrailingslashit((string) get_option('supremesetuhub_api_base_url', ''));
        $token = (string) get_option('supremesetuhub_api_token', '');
        if ($base === '' || $token === '') {
            return array('success' => false, 'status' => 'API_NOT_CONFIGURED');
        }
        $scheme = wp_parse_url($base, PHP_URL_SCHEME);
        $host = wp_parse_url($base, PHP_URL_HOST);
        if (!$host || ($scheme !== 'https' && !in_array($host, array('localhost', '127.0.0.1'), true))) {
            return array('success' => false, 'status' => 'HTTPS_API_URL_REQUIRED');
        }
        $args = array(
            'method' => $method,
            'timeout' => 20,
            'redirection' => 0,
            'headers' => array(
                'Accept' => 'application/json',
                'Authorization' => 'Bearer ' . $token,
            ),
        );
        if ($body !== null) {
            $args['headers']['Content-Type'] = 'application/json';
            $args['body'] = wp_json_encode($body);
        }
        $response = wp_remote_request($base . $path, $args);
        if (is_wp_error($response)) {
            return array('success' => false, 'status' => 'BACKEND_UNREACHABLE', 'message' => $response->get_error_message());
        }
        $code = (int) wp_remote_retrieve_response_code($response);
        $data = json_decode(wp_remote_retrieve_body($response), true);
        if (!is_array($data)) {
            return array('success' => false, 'status' => 'INVALID_BACKEND_RESPONSE', 'http_status' => $code);
        }
        if ($code < 200 || $code >= 300) {
            return array('success' => false, 'status' => 'BACKEND_REQUEST_FAILED', 'http_status' => $code, 'detail' => isset($data['detail']) ? $data['detail'] : null);
        }
        return $data;
    }
}

if (!function_exists('supremesetuhub_control_plane_save_settings')) {
    function supremesetuhub_control_plane_save_settings() {
        if (!current_user_can('manage_options')) { wp_die('Administrator access required.'); }
        check_admin_referer('supremesetuhub_control_plane_settings');
        $base = isset($_POST['api_base_url']) ? esc_url_raw(trim(wp_unslash($_POST['api_base_url']))) : '';
        $token = isset($_POST['api_token']) ? trim(wp_unslash($_POST['api_token'])) : '';
        if ($base !== '' && !wp_parse_url($base, PHP_URL_HOST)) {
            wp_safe_redirect(add_query_arg('control_plane_notice', 'invalid_url', wp_get_referer()));
            exit;
        }
        update_option('supremesetuhub_api_base_url', untrailingslashit($base), false);
        if ($token !== '') {
            update_option('supremesetuhub_api_token', $token, false);
        }
        wp_safe_redirect(add_query_arg('control_plane_notice', 'saved', wp_get_referer()));
        exit;
    }
}
add_action('admin_post_supremesetuhub_save_control_plane', 'supremesetuhub_control_plane_save_settings');

if (!function_exists('supremesetuhub_control_plane_check_ftp')) {
    function supremesetuhub_control_plane_check_ftp() {
        if (!current_user_can('manage_options')) { wp_die('Administrator access required.'); }
        $profile = isset($_POST['profile_id']) ? sanitize_key(wp_unslash($_POST['profile_id'])) : '';
        check_admin_referer('supremesetuhub_check_ftp_' . $profile);
        $result = supremesetuhub_control_plane_request('/infrastructure/ftp/profiles/' . rawurlencode($profile) . '/check', 'POST');
        set_transient('supremesetuhub_ftp_check_' . get_current_user_id(), $result, 60);
        wp_safe_redirect(wp_get_referer());
        exit;
    }
}
add_action('admin_post_supremesetuhub_check_ftp', 'supremesetuhub_control_plane_check_ftp');

if (!function_exists('supremesetuhub_render_control_plane_panel')) {
    function supremesetuhub_render_control_plane_panel($title = 'Database & FTP Control') {
        if (!current_user_can('manage_options')) { return; }
        $base = (string) get_option('supremesetuhub_api_base_url', '');
        $configured = ($base !== '' && (string) get_option('supremesetuhub_api_token', '') !== '');
        echo '<div class="wrap"><h1>' . esc_html($title) . '</h1>';
        if (isset($_GET['control_plane_notice']) && $_GET['control_plane_notice'] === 'saved') {
            echo '<div class="notice notice-success"><p>Backend connection settings saved.</p></div>';
        }
        echo '<h2>Backend API Connection</h2><form method="post" action="' . esc_url(admin_url('admin-post.php')) . '">';
        echo '<input type="hidden" name="action" value="supremesetuhub_save_control_plane">';
        wp_nonce_field('supremesetuhub_control_plane_settings');
        echo '<table class="form-table"><tr><th><label for="supremesetuhub-api-base">Backend API Base URL</label></th><td><input id="supremesetuhub-api-base" class="regular-text" type="url" name="api_base_url" value="' . esc_attr($base) . '" placeholder="https://your-backend.example.com"></td></tr>';
        echo '<tr><th><label for="supremesetuhub-api-token">Owner Bearer Token</label></th><td><input id="supremesetuhub-api-token" class="regular-text" type="password" name="api_token" value="" autocomplete="new-password" placeholder="' . ($configured ? 'Saved — leave blank to keep current token' : 'Paste owner token') . '"><p class="description">Token is never displayed back. Use HTTPS and an owner-authorized token.</p></td></tr></table>';
        submit_button('Save Backend Connection');
        echo '</form>';

        if (!$configured) {
            echo '<div class="notice notice-warning"><p>Database and FTP status are unavailable until the backend URL and owner token are configured.</p></div></div>';
            return;
        }

        $db = supremesetuhub_control_plane_request('/infrastructure/database/status');
        $ftp = supremesetuhub_control_plane_request('/infrastructure/ftp/profiles');
        $check = get_transient('supremesetuhub_ftp_check_' . get_current_user_id());
        if ($check !== false) {
            delete_transient('supremesetuhub_ftp_check_' . get_current_user_id());
            echo '<h2>Latest Read-only FTP Check</h2><pre style="max-width:900px;overflow:auto;background:#fff;padding:12px;">' . esc_html(wp_json_encode($check, JSON_PRETTY_PRINT)) . '</pre>';
        }
        echo '<h2>Central Database</h2><p><strong>Status:</strong> ' . esc_html(isset($db['status']) ? $db['status'] : (isset($db['status']) ? $db['status'] : 'NOT_VERIFIED')) . '</p>';
        if (isset($db['database'])) { echo '<p><strong>Database:</strong> ' . esc_html($db['database']) . '</p>'; }
        echo '<h2>Five Logical FTP Profiles</h2>';
        if (!empty($ftp['profiles']) && is_array($ftp['profiles'])) {
            echo '<table class="widefat striped"><thead><tr><th>Identity</th><th>Configured</th><th>Protocol</th><th>Read-only check</th></tr></thead><tbody>';
            foreach ($ftp['profiles'] as $profile) {
                echo '<tr><td>' . esc_html(isset($profile['label']) ? $profile['label'] : $profile['profile_id']) . '</td>';
                echo '<td>' . esc_html(!empty($profile['configured']) ? 'Ready' : 'Missing configuration') . '</td>';
                echo '<td>Explicit FTPS</td><td><form method="post" action="' . esc_url(admin_url('admin-post.php')) . '">';
                echo '<input type="hidden" name="action" value="supremesetuhub_check_ftp"><input type="hidden" name="profile_id" value="' . esc_attr($profile['profile_id']) . '">';
                wp_nonce_field('supremesetuhub_check_ftp_' . $profile['profile_id']);
                submit_button('Check connection', 'secondary small', 'submit', false, empty($profile['configured']) ? array('disabled' => 'disabled') : array());
                echo '</form></td></tr>';
            }
            echo '</tbody></table>';
        } else {
            echo '<p>FTP status unavailable: ' . esc_html(isset($ftp['status']) ? $ftp['status'] : 'BACKEND_REQUEST_FAILED') . '</p>';
        }
        echo '<p class="description">FTP checks only verify FTPS login and the account starting directory. They do not prove per-identity directory isolation and do not upload, edit, or delete files.</p></div>';
    }
}

add_action('admin_menu', function () {
    add_submenu_page(
        'supremesetuhub',
        'Database & FTP Control',
        'Database & FTP',
        'manage_options',
        'supremesetuhub-database-ftp',
        function () { supremesetuhub_render_control_plane_panel('SUPREMESETUHUB — Database & FTP'); }
    );
});
