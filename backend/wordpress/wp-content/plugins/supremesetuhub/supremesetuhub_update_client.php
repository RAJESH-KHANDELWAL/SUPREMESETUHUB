<?php
/**
 * First-party updater client for the SUPREME UPDATE SERVER.
 * The API server publishes packages; GitHub is not used for update delivery.
 */
if (!defined('ABSPATH')) { exit; }

if (!function_exists('supremesetuhub_update_server_url')) {
    function supremesetuhub_update_server_url() {
        $default = 'https://supremesetuhub-3v4e.onrender.com';
        if (defined('SUPREME_UPDATE_SERVER_URL') && SUPREME_UPDATE_SERVER_URL) {
            $default = SUPREME_UPDATE_SERVER_URL;
        }
        return untrailingslashit(esc_url_raw(apply_filters('supremesetuhub_update_server_url', $default)));
    }
}

if (!function_exists('supremesetuhub_update_catalog')) {
    function supremesetuhub_update_catalog() {
        return array(
            'supremesetuhub/supremesetuhub.php' => array(
                'slug' => 'supremesetuhub',
                'name' => 'SUPREMESETUHUB',
            ),
            'dr-rajesh-khandelwal-ibc/dr-rajesh-khandelwal-ibc.php' => array(
                'slug' => 'dr-rajesh-khandelwal-ibc',
                'name' => 'DR RAJESH KHANDELWAL IBC',
            ),
        );
    }
}

if (!function_exists('supremesetuhub_update_metadata')) {
    function supremesetuhub_update_metadata($plugin_file, $installed_version) {
        $catalog = supremesetuhub_update_catalog();
        if (!isset($catalog[$plugin_file])) { return null; }

        $slug = $catalog[$plugin_file]['slug'];
        $url = add_query_arg(
            array('installed_version' => $installed_version),
            supremesetuhub_update_server_url() . '/api/v1/supreme-updates/check/' . rawurlencode($slug)
        );
        $response = wp_remote_get($url, array(
            'timeout' => 20,
            'redirection' => 2,
            'headers' => array('Accept' => 'application/json', 'User-Agent' => 'SUPREMESETUHUB-WordPress-Updater'),
        ));
        if (is_wp_error($response) || 200 !== wp_remote_retrieve_response_code($response)) {
            return null;
        }
        $data = json_decode(wp_remote_retrieve_body($response), true);
        if (!is_array($data) || empty($data['success']) || empty($data['latest_version'])) {
            return null;
        }
        if (empty($data['package']) || empty($data['sha256']) || !preg_match('/^[a-f0-9]{64}$/i', $data['sha256'])) {
            return null;
        }
        $data['package'] = (0 === strpos($data['package'], 'https://') || 0 === strpos($data['package'], 'http://'))
            ? $data['package']
            : supremesetuhub_update_server_url() . '/' . ltrim($data['package'], '/');
        $data['_plugin_name'] = $catalog[$plugin_file]['name'];
        return $data;
    }
}

add_filter('pre_set_site_transient_update_plugins', function ($transient) {
    if (!is_object($transient) || empty($transient->checked)) { return $transient; }
    if (!isset($transient->response) || !is_array($transient->response)) { $transient->response = array(); }
    if (!isset($transient->no_update) || !is_array($transient->no_update)) { $transient->no_update = array(); }

    foreach (supremesetuhub_update_catalog() as $plugin_file => $config) {
        if (!isset($transient->checked[$plugin_file])) { continue; }
        $installed = (string) $transient->checked[$plugin_file];
        $metadata = supremesetuhub_update_metadata($plugin_file, $installed);
        if (!$metadata) { continue; }

        if (version_compare($metadata['latest_version'], $installed, '>') && !empty($metadata['update_available'])) {
            $package_url = esc_url_raw($metadata['package']);
            set_site_transient(
                'supreme_update_sha256_' . md5($package_url),
                strtolower($metadata['sha256']),
                30 * MINUTE_IN_SECONDS
            );
            $transient->response[$plugin_file] = (object) array(
                'id' => supremesetuhub_update_server_url(),
                'slug' => $config['slug'],
                'plugin' => $plugin_file,
                'new_version' => sanitize_text_field($metadata['latest_version']),
                'url' => esc_url_raw($metadata['homepage'] ?? ''),
                'package' => $package_url,
                'tested' => sanitize_text_field($metadata['tested'] ?? ''),
                'requires' => sanitize_text_field($metadata['requires'] ?? '5.8'),
                'requires_php' => sanitize_text_field($metadata['requires_php'] ?? '7.4'),
            );
            unset($transient->no_update[$plugin_file]);
        } else {
            $transient->no_update[$plugin_file] = (object) array(
                'id' => supremesetuhub_update_server_url(),
                'slug' => $config['slug'],
                'plugin' => $plugin_file,
                'new_version' => $installed,
                'url' => '',
                'package' => '',
            );
            unset($transient->response[$plugin_file]);
        }
    }
    return $transient;
});

add_filter('plugins_api', function ($result, $action, $args) {
    if ('plugin_information' !== $action || empty($args->slug)) { return $result; }
    foreach (supremesetuhub_update_catalog() as $plugin_file => $config) {
        if ($config['slug'] !== $args->slug) { continue; }
        $installed = '';
        if (!function_exists('get_plugins')) {
            require_once ABSPATH . 'wp-admin/includes/plugin.php';
        }
        $plugins = get_plugins();
        if (isset($plugins[$plugin_file]['Version'])) {
            $installed = $plugins[$plugin_file]['Version'];
        }
        $metadata = supremesetuhub_update_metadata($plugin_file, $installed);
        if (!$metadata) { return $result; }
        return (object) array(
            'name' => $config['name'],
            'slug' => $config['slug'],
            'version' => sanitize_text_field($metadata['latest_version']),
            'author' => 'DR RAJESH KHANDELWAL IBC',
            'homepage' => esc_url_raw($metadata['homepage'] ?? ''),
            'download_link' => esc_url_raw($metadata['package']),
            'sections' => array(
                'description' => esc_html($config['name']) . ' — official first-party plugin.',
                'changelog' => wp_kses_post(nl2br(esc_html($metadata['notes'] ?? ''))),
            ),
        );
    }
    return $result;
}, 20, 3);

/** Verify the package SHA-256 before WordPress installs it. */
add_filter('upgrader_pre_download', function ($reply, $package, $upgrader, $hook_extra) {
    $server = supremesetuhub_update_server_url();
    if (0 !== strpos((string) $package, $server . '/')) { return $reply; }

    $expected = get_site_transient('supreme_update_sha256_' . md5((string) $package));
    if (!is_string($expected) || !preg_match('/^[a-f0-9]{64}$/', $expected)) {
        return new WP_Error('supreme_update_checksum_missing', 'SUPREME UPDATE SERVER checksum metadata is missing. Please check for updates again.');
    }

    require_once ABSPATH . 'wp-admin/includes/file.php';
    $downloaded = download_url($package, 300);
    if (is_wp_error($downloaded)) { return $downloaded; }

    $actual = hash_file('sha256', $downloaded);
    if (!is_string($actual) || !hash_equals($expected, strtolower($actual))) {
        @unlink($downloaded);
        return new WP_Error('supreme_update_checksum_failed', 'SUPREME UPDATE SERVER package SHA-256 verification failed. The plugin was not installed.');
    }
    delete_site_transient('supreme_update_sha256_' . md5((string) $package));
    return $downloaded;
}, 10, 4);

/** Enable WordPress automatic updates for both first-party plugins. */
add_filter('auto_update_plugin', function ($update, $item) {
    $plugin_file = isset($item->plugin) ? $item->plugin : '';
    return isset(supremesetuhub_update_catalog()[$plugin_file]) ? true : $update;
}, 20, 2);
