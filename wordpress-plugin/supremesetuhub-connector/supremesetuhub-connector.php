<?php
/**
 * Plugin Name: SUPREMESETUHUB Connector
 * Description: Connects a WordPress storefront to the SUPREMESETUHUB public API catalog and health endpoint.
 * Version: 1.0.0
 * Requires at least: 6.2
 * Requires PHP: 7.4
 * Author: DR RAJESH KHANDELWAL IBC
 * License: GPL-2.0-or-later
 * Text Domain: supremesetuhub-connector
 */

if (!defined('ABSPATH')) {
    exit;
}

final class SUPREMESETUHUB_Connector {
    const OPTION = 'supremesetuhub_connector_options';
    const CACHE_TTL = 300;

    public static function init() {
        add_action('admin_menu', array(__CLASS__, 'admin_menu'));
        add_action('admin_init', array(__CLASS__, 'register_settings'));
        add_action('admin_post_suph_connector_test', array(__CLASS__, 'test_connection'));
        add_shortcode('supremesetuhub_status', array(__CLASS__, 'status_shortcode'));
        add_shortcode('supremesetuhub_pod_catalog', array(__CLASS__, 'pod_catalog_shortcode'));
        add_shortcode('supremesetuhub_digital_catalog', array(__CLASS__, 'digital_catalog_shortcode'));
    }

    private static function options() {
        $value = get_option(self::OPTION, array());
        return is_array($value) ? $value : array();
    }

    private static function api_base() {
        $options = self::options();
        $base = isset($options['api_base']) ? trim((string) $options['api_base']) : '';
        $base = esc_url_raw($base, array('https'));
        return untrailingslashit($base);
    }

    private static function request_json($path) {
        $base = self::api_base();
        if (!$base || !wp_http_validate_url($base) || strpos($base, 'https://') !== 0) {
            return new WP_Error('suph_api_url_missing', __('Set a valid HTTPS API base URL in Settings → SUPREMESETUHUB.', 'supremesetuhub-connector'));
        }

        $cache_key = 'suph_' . md5($base . '|' . $path);
        $cached = get_transient($cache_key);
        if ($cached !== false) {
            return $cached;
        }

        $response = wp_remote_get($base . $path, array(
            'timeout' => 8,
            'redirection' => 2,
            'headers' => array('Accept' => 'application/json'),
            'user-agent' => 'SUPREMESETUHUB-WordPress-Connector/1.0',
        ));

        if (is_wp_error($response)) {
            return $response;
        }

        $status = (int) wp_remote_retrieve_response_code($response);
        if ($status < 200 || $status >= 300) {
            return new WP_Error('suph_api_http_' . $status, sprintf(__('SUPREMESETUHUB API returned HTTP %d.', 'supremesetuhub-connector'), $status));
        }

        $decoded = json_decode(wp_remote_retrieve_body($response), true);
        if (!is_array($decoded)) {
            return new WP_Error('suph_api_invalid_json', __('The API response was not valid JSON.', 'supremesetuhub-connector'));
        }

        set_transient($cache_key, $decoded, self::CACHE_TTL);
        return $decoded;
    }

    public static function admin_menu() {
        add_options_page(
            __('SUPREMESETUHUB Connector', 'supremesetuhub-connector'),
            __('SUPREMESETUHUB', 'supremesetuhub-connector'),
            'manage_options',
            'supremesetuhub-connector',
            array(__CLASS__, 'settings_page')
        );
    }

    public static function register_settings() {
        register_setting('suph_connector_settings', self::OPTION, array(
            'type' => 'array',
            'sanitize_callback' => array(__CLASS__, 'sanitize_options'),
            'default' => array('api_base' => ''),
        ));
    }

    public static function sanitize_options($input) {
        $input = is_array($input) ? $input : array();
        $url = isset($input['api_base']) ? trim((string) $input['api_base']) : '';
        if ($url === '') {
            return array('api_base' => '');
        }
        $url = esc_url_raw($url, array('https'));
        if (!$url || strpos($url, 'https://') !== 0 || !wp_http_validate_url($url)) {
            add_settings_error(self::OPTION, 'invalid_api_base', __('Enter a valid HTTPS API base URL, for example https://api.example.com.', 'supremesetuhub-connector'));
            return self::options();
        }
        return array('api_base' => untrailingslashit($url));
    }

    public static function settings_page() {
        if (!current_user_can('manage_options')) {
            return;
        }
        $options = self::options();
        ?>
        <div class="wrap">
            <h1><?php esc_html_e('SUPREMESETUHUB Connector', 'supremesetuhub-connector'); ?></h1>
            <p><?php esc_html_e('Connect this WordPress site to your deployed FastAPI backend. Use the public HTTPS API base URL only; never paste passwords, API keys, or hosting credentials here.', 'supremesetuhub-connector'); ?></p>
            <?php settings_errors(self::OPTION); ?>
            <form method="post" action="options.php">
                <?php settings_fields('suph_connector_settings'); ?>
                <table class="form-table" role="presentation">
                    <tr>
                        <th scope="row"><label for="suph-api-base"><?php esc_html_e('Backend API Base URL', 'supremesetuhub-connector'); ?></label></th>
                        <td>
                            <input id="suph-api-base" class="regular-text" type="url" name="<?php echo esc_attr(self::OPTION); ?>[api_base]" value="<?php echo esc_attr(isset($options['api_base']) ? $options['api_base'] : ''); ?>" placeholder="https://api.your-domain.com" required />
                            <p class="description"><?php esc_html_e('Do not include a trailing slash or an endpoint path.', 'supremesetuhub-connector'); ?></p>
                        </td>
                    </tr>
                </table>
                <?php submit_button(__('Save API URL', 'supremesetuhub-connector')); ?>
            </form>
            <hr />
            <h2><?php esc_html_e('Connection test', 'supremesetuhub-connector'); ?></h2>
            <p><?php esc_html_e('Save the API URL first, then test the backend health endpoint.', 'supremesetuhub-connector'); ?></p>
            <form method="post" action="<?php echo esc_url(admin_url('admin-post.php')); ?>">
                <input type="hidden" name="action" value="suph_connector_test" />
                <?php wp_nonce_field('suph_connector_test'); ?>
                <?php submit_button(__('Test Backend Connection', 'supremesetuhub-connector'), 'secondary', 'submit', false); ?>
            </form>
            <?php if (isset($_GET['suph_test'])): ?>
                <p><strong><?php echo esc_html(sanitize_text_field(wp_unslash($_GET['suph_test']))); ?></strong></p>
            <?php endif; ?>
            <h2><?php esc_html_e('Shortcodes', 'supremesetuhub-connector'); ?></h2>
            <ul>
                <li><code>[supremesetuhub_status]</code> — backend health status</li>
                <li><code>[supremesetuhub_pod_catalog market="IN"]</code> — print-on-demand estimate catalog</li>
                <li><code>[supremesetuhub_digital_catalog market="IN"]</code> — published digital designs catalog</li>
            </ul>
            <p><?php esc_html_e('Catalog prices are estimates or configured listing prices. This connector does not process payments, create print orders, or deliver paid downloads.', 'supremesetuhub-connector'); ?></p>
        </div>
        <?php
    }

    public static function test_connection() {
        if (!current_user_can('manage_options')) {
            wp_die(esc_html__('You are not allowed to test this connection.', 'supremesetuhub-connector'));
        }
        check_admin_referer('suph_connector_test');
        $result = self::request_json('/health');
        $message = is_wp_error($result)
            ? 'Connection failed: ' . $result->get_error_message()
            : 'Connection successful: ' . (isset($result['status']) ? sanitize_text_field((string) $result['status']) : 'HTTP 200');
        wp_safe_redirect(add_query_arg(array(
            'page' => 'supremesetuhub-connector',
            'suph_test' => rawurlencode($message),
        ), admin_url('options-general.php')));
        exit;
    }

    public static function status_shortcode() {
        $result = self::request_json('/health');
        if (is_wp_error($result)) {
            return '<p class="suph-status suph-status-error">' . esc_html($result->get_error_message()) . '</p>';
        }
        $status = isset($result['status']) ? sanitize_text_field((string) $result['status']) : 'reachable';
        return '<p class="suph-status">' . esc_html(sprintf(__('SUPREMESETUHUB backend: %s', 'supremesetuhub-connector'), $status)) . '</p>';
    }

    public static function pod_catalog_shortcode($atts) {
        $atts = shortcode_atts(array('market' => 'IN'), $atts, 'supremesetuhub_pod_catalog');
        $market = strtoupper(sanitize_text_field($atts['market']));
        if (!in_array($market, array('IN', 'GLOBAL'), true)) {
            $market = 'IN';
        }
        $result = self::request_json('/api/v1/print-on-demand/public/catalog?market=' . rawurlencode($market));
        if (is_wp_error($result) || empty($result['data']['products']) || !is_array($result['data']['products'])) {
            return '<p class="suph-catalog-error">' . esc_html(is_wp_error($result) ? $result->get_error_message() : __('POD catalog is unavailable. Please try again later.', 'supremesetuhub-connector')) . '</p>';
        }
        $data = $result['data'];
        $currency = isset($data['currency']) ? sanitize_text_field($data['currency']) : ($market === 'IN' ? 'INR' : 'USD');
        $html = '<div class="suph-catalog" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:16px">';
        foreach ($data['products'] as $item) {
            $name = isset($item['name']) ? sanitize_text_field($item['name']) : '';
            $category = isset($item['category']) ? sanitize_text_field($item['category']) : '';
            $description = isset($item['description']) ? sanitize_text_field($item['description']) : '';
            $price = isset($item['standard_from']) ? number_format_i18n((float) $item['standard_from'], 2) : '';
            $premium = isset($item['premium_from']) ? number_format_i18n((float) $item['premium_from'], 2) : '';
            $html .= '<article style="border:1px solid #d8e2f0;border-radius:10px;padding:16px">';
            $html .= '<h3>' . esc_html($name) . '</h3><p>' . esc_html($category) . '</p><p>' . esc_html($description) . '</p>';
            $html .= '<p><strong>' . esc_html($currency . ' ' . $price) . '</strong> ' . esc_html__('standard estimate', 'supremesetuhub-connector') . '</p>';
            $html .= '<p>' . esc_html($currency . ' ' . $premium) . ' ' . esc_html__('premium estimate', 'supremesetuhub-connector') . '</p>';
            $html .= '</article>';
        }
        $html .= '</div><p class="suph-price-notice">' . esc_html(isset($data['pricing_notice']) ? $data['pricing_notice'] : __('Prices are estimates and must be confirmed with a fulfillment provider.', 'supremesetuhub-connector')) . '</p>';
        return $html;
    }

    public static function digital_catalog_shortcode($atts) {
        $atts = shortcode_atts(array('market' => 'IN', 'limit' => 24), $atts, 'supremesetuhub_digital_catalog');
        $market = strtoupper(sanitize_text_field($atts['market']));
        if (!in_array($market, array('IN', 'GLOBAL'), true)) {
            $market = 'IN';
        }
        $limit = max(1, min(100, absint($atts['limit'])));
        $result = self::request_json('/api/v1/digital-marketplace/catalog?market=' . rawurlencode($market) . '&limit=' . $limit);
        if (is_wp_error($result) || empty($result['data']['designs']) || !is_array($result['data']['designs'])) {
            return '<p class="suph-catalog-error">' . esc_html(is_wp_error($result) ? $result->get_error_message() : __('No published digital designs are available yet.', 'supremesetuhub-connector')) . '</p>';
        }
        $html = '<div class="suph-digital-catalog" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:16px">';
        foreach ($result['data']['designs'] as $item) {
            $title = isset($item['title']) ? sanitize_text_field($item['title']) : '';
            $description = isset($item['description']) ? sanitize_text_field($item['description']) : '';
            $category = isset($item['category']) ? sanitize_text_field($item['category']) : '';
            $preview = isset($item['preview_url']) ? esc_url($item['preview_url']) : '';
            $price = isset($item['price']) ? sanitize_text_field((string) $item['price']) : '';
            $currency = isset($item['currency_code']) ? sanitize_text_field($item['currency_code']) : ($market === 'IN' ? 'INR' : 'USD');
            $html .= '<article style="border:1px solid #d8e2f0;border-radius:10px;padding:16px">';
            if ($preview) {
                $html .= '<img loading="lazy" alt="' . esc_attr($title) . '" src="' . $preview . '" style="width:100%;height:auto;border-radius:6px" />';
            }
            $html .= '<h3>' . esc_html($title) . '</h3><p>' . esc_html($category) . '</p><p>' . esc_html($description) . '</p><p><strong>' . esc_html($currency . ' ' . $price) . '</strong></p>';
            $html .= '</article>';
        }
        $html .= '</div><p>' . esc_html__('Checkout and paid download delivery are not enabled yet. Contact the site owner for availability.', 'supremesetuhub-connector') . '</p>';
        return $html;
    }
}

SUPREMESETUHUB_Connector::init();
