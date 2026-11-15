<?php
/**
 * Plugin Name: SUPREME PRINT ON DEMAND
 * Description: Responsive public Print on Demand catalog shortcode powered by the SUPREMESETUHUB API.
 * Version: 1.0.0
 * Requires at least: 6.2
 * Requires PHP: 7.4
 * Author: DR RAJESH KHANDELWAL IBC
 * License: GPL-2.0-or-later
 * Text Domain: supreme-print-on-demand
 */
if (!defined('ABSPATH')) { exit; }

final class Supreme_Print_On_Demand {
    const OPTION = 'supreme_pod_api_base';
    public static function init() {
        add_action('admin_menu', array(__CLASS__, 'admin_menu'));
        add_action('admin_init', array(__CLASS__, 'register_settings'));
        add_shortcode('supreme_print_on_demand', array(__CLASS__, 'render'));
    }
    public static function admin_menu() {
        add_options_page('SUPREME PRINT ON DEMAND', 'SUPREME PRINT ON DEMAND', 'manage_options', 'supreme-pod', array(__CLASS__, 'settings_page'));
    }
    public static function register_settings() {
        register_setting('supreme_pod_settings', self::OPTION, array('sanitize_callback' => array(__CLASS__, 'sanitize_api_base'), 'default' => ''));
    }
    public static function sanitize_api_base($value) {
        $value = trim((string) $value);
        if ($value === '') { return ''; }
        $value = esc_url_raw($value, array('https'));
        if (!$value || strpos($value, 'https://') !== 0 || !wp_http_validate_url($value)) {
            add_settings_error(self::OPTION, 'invalid_api_base', 'Enter a valid HTTPS API base URL.');
            return (string) get_option(self::OPTION, '');
        }
        return untrailingslashit($value);
    }
    public static function settings_page() {
        if (!current_user_can('manage_options')) { return; }
        ?>
        <div class="wrap"><h1>SUPREME PRINT ON DEMAND</h1>
          <p>Enter the deployed SUPREMESETUHUB FastAPI base URL (HTTPS only), without an endpoint path.</p>
          <form method="post" action="options.php">
            <?php settings_fields('supreme_pod_settings'); ?>
            <table class="form-table"><tr><th scope="row"><label for="supreme_pod_api_base">API Base URL</label></th><td><input class="regular-text" type="url" id="supreme_pod_api_base" name="<?php echo esc_attr(self::OPTION); ?>" value="<?php echo esc_attr(get_option(self::OPTION, '')); ?>" placeholder="https://your-api-domain.example" /></td></tr></table>
            <?php submit_button('Save API URL'); ?>
          </form>
        </div>
        <?php
    }
    private static function catalog($market) {
        $base = trim((string) get_option(self::OPTION, ''));
        if (!$base || strpos($base, 'https://') !== 0 || !wp_http_validate_url($base)) {
            return new WP_Error('supreme_pod_api_missing', 'The catalog API is not configured yet. The site administrator must set Settings → SUPREME PRINT ON DEMAND.');
        }
        $url = $base . '/api/v1/print-on-demand/public/catalog?market=' . rawurlencode($market);
        $response = wp_remote_get($url, array('timeout' => 12, 'redirection' => 2, 'headers' => array('Accept' => 'application/json'), 'user-agent' => 'SUPREME-PRINT-ON-DEMAND-WordPress/1.0'));
        if (is_wp_error($response)) { return $response; }
        $status = (int) wp_remote_retrieve_response_code($response);
        if ($status < 200 || $status >= 300) { return new WP_Error('supreme_pod_http_error', 'The catalog API returned HTTP ' . $status . '.'); }
        $json = json_decode(wp_remote_retrieve_body($response), true);
        if (!is_array($json) || empty($json['data']['products']) || !is_array($json['data']['products'])) {
            return new WP_Error('supreme_pod_invalid_catalog', 'The public catalog is not available right now.');
        }
        return $json['data'];
    }
    public static function render($atts = array()) {
        $atts = shortcode_atts(array('market' => 'IN'), $atts, 'supreme_print_on_demand');
        $market = strtoupper(sanitize_text_field($atts['market']));
        if (!in_array($market, array('IN', 'GLOBAL'), true)) { $market = 'IN'; }
        $data = self::catalog($market);
        if (is_wp_error($data)) {
            return '<div class="supreme-pod-alert" role="status">' . esc_html($data->get_error_message()) . '</div>';
        }
        $currency = isset($data['currency']) ? sanitize_text_field($data['currency']) : ($market === 'IN' ? 'INR' : 'USD');
        $products = $data['products'];
        ob_start(); ?>
        <section class="supreme-pod" aria-label="SUPREME PRINT ON DEMAND">
          <style>
            .supreme-pod{--sp-blue:#0b5cff;--sp-ink:#101828;color:var(--sp-ink);font-family:inherit}.supreme-pod *{box-sizing:border-box}
            .supreme-pod-hero{padding:clamp(24px,5vw,48px);background:linear-gradient(135deg,#071b49,#0b5cff);color:#fff;border-radius:22px;margin-bottom:24px}
            .supreme-pod-hero h1{color:#fff;font-size:clamp(1.8rem,4vw,3rem);line-height:1.1;margin:0 0 12px}.supreme-pod-hero p{line-height:1.7;max-width:800px;margin:0}
            .supreme-pod-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,230px),1fr));gap:16px}.supreme-pod-card{border:1px solid #dce5f2;border-radius:16px;background:#fff;padding:20px;box-shadow:0 8px 24px rgba(16,24,40,.05)}
            .supreme-pod-card h2{font-size:1.15rem;margin:0 0 8px}.supreme-pod-category{color:#0b5cff;font-size:.8rem;font-weight:800;text-transform:uppercase;letter-spacing:.06em}.supreme-pod-card p{line-height:1.6;color:#475467}
            .supreme-pod-price{font-weight:900;color:#101828;margin:12px 0 4px}.supreme-pod-premium{font-size:.92rem;color:#475467}.supreme-pod-notice,.supreme-pod-alert{padding:14px 16px;background:#f2f6ff;border-radius:12px;margin-top:18px;line-height:1.6}.supreme-pod-alert{background:#fff4e5;color:#7a2e0e}
          </style>
          <header class="supreme-pod-hero"><h1>🎨 SUPREME PRINT ON DEMAND</h1><p>Discover customizable products for your brand, creative ideas and business. Choose a product to start planning your design.</p></header>
          <div class="supreme-pod-grid">
          <?php foreach ($products as $item) :
              $name = isset($item['name']) ? sanitize_text_field($item['name']) : 'Product';
              $category = isset($item['category']) ? sanitize_text_field($item['category']) : '';
              $description = isset($item['description']) ? sanitize_text_field($item['description']) : '';
              $standard = isset($item['standard_from']) ? (float) $item['standard_from'] : null;
              $premium = isset($item['premium_from']) ? (float) $item['premium_from'] : null;
          ?>
            <article class="supreme-pod-card"><div class="supreme-pod-category"><?php echo esc_html($category); ?></div><h2><?php echo esc_html($name); ?></h2><p><?php echo esc_html($description); ?></p>
              <?php if ($standard !== null) : ?><div class="supreme-pod-price"><?php echo esc_html($currency . ' ' . number_format_i18n($standard, 2)); ?> <span class="supreme-pod-premium">standard estimate</span></div><?php endif; ?>
              <?php if ($premium !== null) : ?><div class="supreme-pod-premium"><?php echo esc_html($currency . ' ' . number_format_i18n($premium, 2)); ?> premium estimate</div><?php endif; ?>
            </article>
          <?php endforeach; ?>
          </div>
          <p class="supreme-pod-notice"><strong>Pricing notice:</strong> <?php echo esc_html(isset($data['pricing_notice']) ? $data['pricing_notice'] : 'Prices are estimates only and must be confirmed with a fulfilment provider.'); ?> Checkout, payment capture, supplier ordering and fulfilment are not enabled by this catalog plugin.</p>
        </section>
        <?php
        return ob_get_clean();
    }
}
Supreme_Print_On_Demand::init();
