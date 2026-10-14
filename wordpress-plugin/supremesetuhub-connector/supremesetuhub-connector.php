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
    const DEFAULT_API_BASE = 'https://api.rajeshkhandelwalofficial.com';
    const CACHE_TTL = 300;

    public static function init() {
        add_action('admin_menu', array(__CLASS__, 'admin_menu'));
        add_action('admin_init', array(__CLASS__, 'register_settings'));
        add_action('admin_post_suph_connector_test', array(__CLASS__, 'test_connection'));
        add_shortcode('supremesetuhub_status', array(__CLASS__, 'status_shortcode'));
        add_shortcode('supremesetuhub_pod_catalog', array(__CLASS__, 'pod_catalog_shortcode'));
        add_shortcode('supremesetuhub_digital_catalog', array(__CLASS__, 'digital_catalog_shortcode'));

        // Keep ecosystem features inside this existing DR RAJESH KHANDELWAL IBC plugin.
        add_shortcode('supreme_ecosystem_home', array(__CLASS__, 'ecosystem_home_shortcode'));
        add_shortcode('supreme_snippet_home', array(__CLASS__, 'ecosystem_home_shortcode'));
        add_shortcode('supreme_global_business_ecosystem', array(__CLASS__, 'global_business_ecosystem_shortcode'));
        add_shortcode('supreme_contact', array(__CLASS__, 'contact_shortcode'));
        add_shortcode('supreme_youtag_wellness', array(__CLASS__, 'youtag_wellness_shortcode'));
        add_shortcode('supreme_bada_business', array(__CLASS__, 'bada_business_shortcode'));
        add_shortcode('supreme_print_on_demand', array(__CLASS__, 'pod_catalog_shortcode'));
        add_shortcode('supreme_backend_status', array(__CLASS__, 'status_shortcode'));
    }

    private static function options() {
        $value = get_option(self::OPTION, array());
        return is_array($value) ? $value : array();
    }

    private static function api_base() {
        $options = self::options();
        $base = isset($options['api_base']) ? trim((string) $options['api_base']) : '';
        if ($base === '') {
            $base = self::DEFAULT_API_BASE;
        }
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
            'default' => array('api_base' => self::DEFAULT_API_BASE),
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
                            <input id="suph-api-base" class="regular-text" type="url" name="<?php echo esc_attr(self::OPTION); ?>[api_base]" value="<?php echo esc_attr(!empty($options['api_base']) ? $options['api_base'] : self::DEFAULT_API_BASE); ?>" placeholder="https://api.rajeshkhandelwalofficial.com" required />
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

    /**
     * Single-plugin ecosystem landing page. Styling is scoped to this component.
     */
    public static function ecosystem_home_shortcode($atts = array()) {
        $atts = shortcode_atts(array(
            'pod_url' => home_url('/print-on-demand/'),
            'digital_url' => home_url('/digital-store/'),
            'services_url' => home_url('/services/'),
            'about_url' => home_url('/about/'),
        ), $atts, 'supreme_ecosystem_home');
        $cards = array(
            array('icon' => '🎨', 'title' => 'SUPREME PRINT ON DEMAND', 'desc' => 'Explore customizable products and creative merchandise.', 'url' => $atts['pod_url'], 'cta' => 'EXPLORE POD'),
            array('icon' => '💻', 'title' => 'DIGITAL STORE', 'desc' => 'Discover digital products and creative resources as they become available.', 'url' => $atts['digital_url'], 'cta' => 'EXPLORE DIGITAL'),
            array('icon' => '🚀', 'title' => 'DIGITAL SERVICES', 'desc' => 'Explore website, online presence and digital business services.', 'url' => $atts['services_url'], 'cta' => 'VIEW SERVICES'),
            array('icon' => '🌍', 'title' => 'OUR MISSION', 'desc' => 'One connected digital ecosystem bringing ideas and services together.', 'url' => $atts['about_url'], 'cta' => 'LEARN MORE'),
        );
        ob_start(); ?>
        <section class="suph-ecosystem" aria-label="SUPREME ECOSYSTEM">
          <style>
            .suph-ecosystem{--se-blue:#0b5cff;--se-ink:#101828;--se-muted:#475467;color:var(--se-ink);font-family:inherit}
            .suph-ecosystem *{box-sizing:border-box}.suph-ecosystem-hero{padding:clamp(28px,6vw,64px);border-radius:24px;background:linear-gradient(135deg,#071b49,#0b5cff 65%,#62a5ff);color:#fff;overflow:hidden}
            .suph-ecosystem-hero h1{color:#fff;font-size:clamp(2rem,5vw,3.5rem);line-height:1.08;margin:.7rem 0 1rem}.suph-ecosystem-hero p{max-width:760px;font-size:1.08rem;line-height:1.7;margin:0 0 22px}
            .suph-eco-btn{display:inline-block;background:#fff;color:#0b45bd!important;padding:12px 18px;border-radius:12px;font-weight:900;text-decoration:none!important;margin:4px 8px 4px 0}
            .suph-eco-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,230px),1fr));gap:16px;margin-top:16px}.suph-eco-card{padding:22px;border:1px solid #dce5f2;border-radius:18px;background:#fff;box-shadow:0 8px 28px rgba(16,24,40,.05);display:flex;flex-direction:column;align-items:flex-start;min-height:210px}
            .suph-eco-card h2{font-size:1.08rem;line-height:1.4;margin:12px 0 8px}.suph-eco-card p{color:var(--se-muted);line-height:1.65;margin:0 0 18px}.suph-eco-card a{margin-top:auto;color:var(--se-blue);font-weight:900;text-decoration:none}
            .suph-eco-note{margin-top:18px;padding:14px 16px;background:#f2f6ff;border-radius:12px;color:#344054;font-size:.93rem}
          </style>
          <div class="suph-ecosystem-hero">
            <div><strong>ONE CONNECTED DIGITAL WORLD</strong></div>
            <h1>👑 SUPREME ECOSYSTEM</h1>
            <p>Welcome to SUPREMESETUHUB — a growing digital platform connecting products, creative ideas and online services.</p>
            <a class="suph-eco-btn" href="<?php echo esc_url($atts['pod_url']); ?>">🎨 SUPREME PRINT ON DEMAND</a>
            <a class="suph-eco-btn" href="<?php echo esc_url($atts['services_url']); ?>">🚀 EXPLORE SERVICES</a>
          </div>
          <h2>EXPLORE THE ECOSYSTEM</h2>
          <div class="suph-eco-grid">
          <?php foreach ($cards as $card) : ?>
            <article class="suph-eco-card"><div aria-hidden="true" style="font-size:2rem"><?php echo esc_html($card['icon']); ?></div>
              <h2><?php echo esc_html($card['title']); ?></h2><p><?php echo esc_html($card['desc']); ?></p>
              <a href="<?php echo esc_url($card['url']); ?>"><?php echo esc_html($card['cta']); ?> →</a>
            </article>
          <?php endforeach; ?>
          </div>
          <p class="suph-eco-note"><strong>Important:</strong> Catalog listings and displayed prices may be estimates. Checkout, payment and fulfilment are not enabled merely by displaying this page.</p>
        </section>
        <?php
        return ob_get_clean();
    }

    /**
     * Embed the backend-served ecosystem frontend using the saved HTTPS API base.
     */
    public static function global_business_ecosystem_shortcode() {
        $base = self::api_base();
        if (!$base || !wp_http_validate_url($base)) {
            return '<p class="suph-catalog-error">' . esc_html__('Set the backend HTTPS URL under Settings → SUPREMESETUHUB first.', 'supremesetuhub-connector') . '</p>';
        }
        $src = $base . '/api/v1/frontend/global-business-ecosystem';
        return '<div class="suph-global-ecosystem" style="width:100%;overflow:hidden"><iframe title="SUPREME Global Business Ecosystem" src="' . esc_url($src) . '" loading="lazy" referrerpolicy="strict-origin-when-cross-origin" style="display:block;width:100%;min-height:850px;border:0;border-radius:16px" sandbox="allow-scripts allow-same-origin allow-forms allow-popups"></iframe></div>';
    }

    public static function contact_shortcode() {
        $html = '<section class="suph-brand-panel" style="padding:24px;border:1px solid #d8e2f0;border-radius:16px;background:#f7faff">';
        $html .= '<h2>' . esc_html__('CONTACT DR RAJESH KHANDELWAL IBC', 'supremesetuhub-connector') . '</h2>';
        $html .= '<p>' . esc_html__('For business enquiries, website projects and collaboration, use the contact options published on this website.', 'supremesetuhub-connector') . '</p>';
        $html .= '<a href="' . esc_url(home_url('/contact/')) . '" style="display:inline-block;padding:11px 16px;background:#0b5cff;color:#fff;border-radius:10px;text-decoration:none;font-weight:700">' . esc_html__('OPEN CONTACT PAGE', 'supremesetuhub-connector') . '</a></section>';
        return $html;
    }

    public static function youtag_wellness_shortcode() {
        return '<section class="suph-brand-panel" style="padding:24px;border:1px solid #d8e2f0;border-radius:16px"><h2>YOUTAG WELLNESS</h2><p>' .
            esc_html__('Explore the YOUTAG WELLNESS business information and available offerings. Confirm current plans, terms and prices with the provider before making a purchase.', 'supremesetuhub-connector') .
            '</p></section>';
    }

    public static function bada_business_shortcode() {
        return '<section class="suph-brand-panel" style="padding:24px;border:1px solid #d8e2f0;border-radius:16px"><h2>BADA BUSINESS</h2><p>' .
            esc_html__('Business learning and entrepreneurship resources. Review the provider’s current program details, fees and terms directly before enrolling.', 'supremesetuhub-connector') .
            '</p></section>';
    }

}

SUPREMESETUHUB_Connector::init();
