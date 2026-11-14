<?php
/**
 * GitHub Releases updater for the two first-party SUPREMESETUHUB plugins.
 * Loaded by the active SUPREMESETUHUB hub plugin; no third-party updater required.
 */
if (!defined('ABSPATH')) { exit; }

if (!function_exists('supremesetuhub_github_plugin_catalog')) {
    function supremesetuhub_github_plugin_catalog() {
        return array(
            'supremesetuhub/supremesetuhub.php' => array(
                'slug' => 'supremesetuhub',
                'name' => 'SUPREMESETUHUB',
                'tag_prefix' => 'supremesetuhub-v',
                'asset' => 'supremesetuhub.zip',
            ),
            'dr-rajesh-khandelwal-ibc/dr-rajesh-khandelwal-ibc.php' => array(
                'slug' => 'dr-rajesh-khandelwal-ibc',
                'name' => 'DR RAJESH KHANDELWAL IBC',
                'tag_prefix' => 'dr-rajesh-khandelwal-ibc-v',
                'asset' => 'dr-rajesh-khandelwal-ibc.zip',
            ),
        );
    }
}

if (!function_exists('supremesetuhub_github_releases')) {
    function supremesetuhub_github_releases() {
        $cached = get_transient('supremesetuhub_github_releases_v1');
        if (is_array($cached)) { return $cached; }

        $response = wp_remote_get(
            'https://api.github.com/repos/RAJESH-KHANDELWAL/SUPREMESETUHUB/releases?per_page=100',
            array(
                'timeout' => 15,
                'headers' => array(
                    'Accept' => 'application/vnd.github+json',
                    'X-GitHub-Api-Version' => '2022-11-28',
                    'User-Agent' => 'SUPREMESETUHUB-WordPress-Updater',
                ),
            )
        );

        if (is_wp_error($response) || 200 !== wp_remote_retrieve_response_code($response)) {
            return array();
        }

        $releases = json_decode(wp_remote_retrieve_body($response), true);
        if (!is_array($releases)) { return array(); }

        set_transient('supremesetuhub_github_releases_v1', $releases, 6 * HOUR_IN_SECONDS);
        return $releases;
    }
}

if (!function_exists('supremesetuhub_github_latest_release')) {
    function supremesetuhub_github_latest_release($plugin_config) {
        $best = null;
        foreach (supremesetuhub_github_releases() as $release) {
            $tag = isset($release['tag_name']) ? (string) $release['tag_name'] : '';
            if (0 !== strpos($tag, $plugin_config['tag_prefix'])) { continue; }

            $version = substr($tag, strlen($plugin_config['tag_prefix']));
            if (!preg_match('/^\\d+\\.\\d+\\.\\d+(?:[-+][0-9A-Za-z.-]+)?$/', $version)) { continue; }

            $asset_url = '';
            if (!empty($release['assets']) && is_array($release['assets'])) {
                foreach ($release['assets'] as $asset) {
                    if (isset($asset['name'], $asset['browser_download_url']) && $plugin_config['asset'] === $asset['name']) {
                        $asset_url = esc_url_raw($asset['browser_download_url']);
                        break;
                    }
                }
            }
            if (!$asset_url) { continue; }

            if (!$best || version_compare($version, $best['version'], '>')) {
                $best = array(
                    'version' => $version,
                    'package' => $asset_url,
                    'notes' => isset($release['body']) ? (string) $release['body'] : '',
                    'url' => isset($release['html_url']) ? esc_url_raw($release['html_url']) : '',
                );
            }
        }
        return $best;
    }
}

add_filter('pre_set_site_transient_update_plugins', function ($transient) {
    if (!is_object($transient) || empty($transient->checked) || !function_exists('get_plugins')) {
        return $transient;
    }

    if (!function_exists('get_plugins')) {
        require_once ABSPATH . 'wp-admin/includes/plugin.php';
    }
    $installed = get_plugins();
    if (!isset($transient->response) || !is_array($transient->response)) { $transient->response = array(); }
    if (!isset($transient->no_update) || !is_array($transient->no_update)) { $transient->no_update = array(); }
    foreach (supremesetuhub_github_plugin_catalog() as $plugin_file => $config) {
        if (!isset($installed[$plugin_file], $transient->checked[$plugin_file])) { continue; }

        $latest = supremesetuhub_github_latest_release($config);
        if (!$latest || !version_compare($latest['version'], $transient->checked[$plugin_file], '>')) { continue; }

        $update = (object) array(
            'id' => 'https://github.com/RAJESH-KHANDELWAL/SUPREMESETUHUB',
            'slug' => $config['slug'],
            'plugin' => $plugin_file,
            'new_version' => $latest['version'],
            'url' => $latest['url'],
            'package' => $latest['package'],
            'tested' => get_bloginfo('version'),
            'requires' => '5.8',
            'requires_php' => '7.4',
        );
        $transient->response[$plugin_file] = $update;
        unset($transient->no_update[$plugin_file]);
    }

    return $transient;
});

add_filter('plugins_api', function ($result, $action, $args) {
    if ('plugin_information' !== $action || empty($args->slug)) { return $result; }

    foreach (supremesetuhub_github_plugin_catalog() as $plugin_file => $config) {
        if ($config['slug'] !== $args->slug) { continue; }
        $latest = supremesetuhub_github_latest_release($config);
        if (!$latest) { return $result; }

        return (object) array(
            'name' => $config['name'],
            'slug' => $config['slug'],
            'version' => $latest['version'],
            'author' => '<a href="https://github.com/RAJESH-KHANDELWAL">DR RAJESH KHANDELWAL IBC</a>',
            'homepage' => 'https://github.com/RAJESH-KHANDELWAL/SUPREMESETUHUB',
            'download_link' => $latest['package'],
            'sections' => array(
                'description' => esc_html($config['name']) . ' — official first-party WordPress plugin.',
                'changelog' => wp_kses_post(nl2br(esc_html($latest['notes']))),
            ),
        );
    }

    return $result;
}, 20, 3);

/** Enable WordPress core automatic updates for both first-party plugins. */
add_filter('auto_update_plugin', function ($update, $item) {
    $plugin_file = isset($item->plugin) ? $item->plugin : '';
    if (isset(supremesetuhub_github_plugin_catalog()[$plugin_file])) {
        return true;
    }
    return $update;
}, 20, 2);
