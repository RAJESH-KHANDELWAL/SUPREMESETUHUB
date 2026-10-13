<?php
/**
 * Plugin Name: SUPREME QIKINK WooCommerce Bridge
 * Description: Sends paid, correctly mapped WooCommerce orders to Qikink. Disabled until explicitly configured.
 * Version: 1.0.0
 * Requires at least: 6.2
 * Requires PHP: 7.4
 * Author: DR RAJESH KHANDELWAL IBC
 * License: GPL-2.0-or-later
 * Text Domain: supreme-qikink-bridge
 */

if (!defined('ABSPATH')) { exit; }

final class Supreme_Qikink_WooCommerce_Bridge {
    const META_STATUS = '_supreme_qikink_status';
    const META_ORDER_ID = '_supreme_qikink_order_id';
    const META_ERROR = '_supreme_qikink_last_error';
    const TOKEN_TRANSIENT = 'supreme_qikink_access_token';

    public static function init() {
        add_action('plugins_loaded', array(__CLASS__, 'boot'));
    }

    public static function boot() {
        if (!class_exists('WooCommerce')) { return; }
        add_action('woocommerce_product_options_inventory_product_data', array(__CLASS__, 'product_fields'));
        add_action('woocommerce_admin_process_product_object', array(__CLASS__, 'save_product_fields'));
        add_action('woocommerce_product_after_variable_attributes', array(__CLASS__, 'variation_fields'), 10, 3);
        add_action('woocommerce_save_product_variation', array(__CLASS__, 'save_variation_fields'), 10, 2);
        add_action('woocommerce_payment_complete', array(__CLASS__, 'submit_paid_order'), 20, 1);
        add_action('woocommerce_admin_order_data_after_order_details', array(__CLASS__, 'render_order_status'));
        add_action('admin_notices', array(__CLASS__, 'configuration_notice'));
    }

    private static function config() {
        $mode = defined('SUPREME_QIKINK_ENV') ? strtolower((string) SUPREME_QIKINK_ENV) : 'sandbox';
        if (!in_array($mode, array('sandbox', 'live'), true)) { $mode = 'invalid'; }
        return array(
            'mode' => $mode,
            'enabled' => defined('SUPREME_QIKINK_ENABLE_ORDERS') && SUPREME_QIKINK_ENABLE_ORDERS === true,
            'client_id' => defined('SUPREME_QIKINK_CLIENT_ID') ? trim((string) SUPREME_QIKINK_CLIENT_ID) : '',
            'client_secret' => defined('SUPREME_QIKINK_CLIENT_SECRET') ? trim((string) SUPREME_QIKINK_CLIENT_SECRET) : '',
            'base_url' => $mode === 'live' ? 'https://api.qikink.com' : 'https://sandbox.qikink.com',
        );
    }

    public static function configuration_notice() {
        if (!current_user_can('manage_woocommerce')) { return; }
        $c = self::config();
        if ($c['enabled'] && $c['mode'] === 'live' && $c['client_id'] !== '' && $c['client_secret'] !== '') { return; }
        echo '<div class="notice notice-warning"><p><strong>SUPREME QIKINK:</strong> order submission is disabled or not fully configured. Set credentials and mode as described in the plugin readme. Do not enable live orders until a sandbox test and product mapping are complete.</p></div>';
    }

    private static function field($key, $label, $description = '', $type = 'text') {
        woocommerce_wp_text_input(array(
            'id' => $key,
            'label' => $label,
            'desc_tip' => $description !== '',
            'description' => $description,
            'type' => $type,
        ));
    }

    public static function product_fields() {
        echo '<div class="options_group"><p><strong>Qikink fulfilment mapping</strong></p>';
        self::field('_supreme_qikink_sku', 'Qikink SKU', 'Exact Qikink product/variant SKU. Use the SKU from your Qikink account.');
        self::field('_supreme_qikink_design_code', 'Design code (optional)', 'Qikink design code when required.');
        self::field('_supreme_qikink_design_link', 'Public design file URL (optional)', 'HTTPS URL Qikink can fetch. Do not use a private/admin URL.');
        self::field('_supreme_qikink_mockup_link', 'Public mockup URL (optional)', 'HTTPS URL to a mockup image.');
        self::field('_supreme_qikink_placement_sku', 'Placement SKU', 'Qikink placement identifier, for example fr. Confirm the valid value with Qikink.');
        self::field('_supreme_qikink_width_inches', 'Design width (inches)', 'Required with design URL if your Qikink design flow requires dimensions.', 'number');
        self::field('_supreme_qikink_height_inches', 'Design height (inches)', 'Required with design URL if your Qikink design flow requires dimensions.', 'number');
        echo '</div>';
    }

    public static function save_product_fields($product) {
        if (!is_a($product, 'WC_Product') || !current_user_can('edit_post', $product->get_id())) { return; }
        foreach (array('_supreme_qikink_sku', '_supreme_qikink_design_code', '_supreme_qikink_design_link', '_supreme_qikink_mockup_link', '_supreme_qikink_placement_sku') as $key) {
            if (isset($_POST[$key])) {
                $value = $key === '_supreme_qikink_design_link' || $key === '_supreme_qikink_mockup_link'
                    ? esc_url_raw(wp_unslash($_POST[$key]))
                    : sanitize_text_field(wp_unslash($_POST[$key]));
                $product->update_meta_data($key, $value);
            }
        }
        foreach (array('_supreme_qikink_width_inches', '_supreme_qikink_height_inches') as $key) {
            if (isset($_POST[$key])) { $product->update_meta_data($key, wc_format_decimal(wp_unslash($_POST[$key]), 2)); }
        }
    }

    public static function variation_fields($loop, $variation_data, $variation) {
        $id = (int) $variation->ID;
        echo '<div class="form-row form-row-full"><strong>Qikink fulfilment mapping</strong></div>';
        foreach (array(
            '_supreme_qikink_sku' => 'Qikink SKU',
            '_supreme_qikink_design_code' => 'Design code (optional)',
            '_supreme_qikink_design_link' => 'Public design URL (optional)',
            '_supreme_qikink_mockup_link' => 'Public mockup URL (optional)',
            '_supreme_qikink_placement_sku' => 'Placement SKU',
        ) as $key => $label) {
            woocommerce_wp_text_input(array(
                'id' => $key . '[' . $loop . ']',
                'name' => $key . '[' . $loop . ']',
                'value' => get_post_meta($id, $key, true),
                'label' => $label,
                'wrapper_class' => 'form-row form-row-full',
            ));
        }
        foreach (array('_supreme_qikink_width_inches' => 'Design width (inches)', '_supreme_qikink_height_inches' => 'Design height (inches)') as $key => $label) {
            woocommerce_wp_text_input(array(
                'id' => $key . '[' . $loop . ']',
                'name' => $key . '[' . $loop . ']',
                'value' => get_post_meta($id, $key, true),
                'label' => $label,
                'type' => 'number',
                'custom_attributes' => array('step' => '0.01', 'min' => '0'),
                'wrapper_class' => 'form-row form-row-full',
            ));
        }
    }

    public static function save_variation_fields($variation_id, $i) {
        if (!current_user_can('edit_post', $variation_id)) { return; }
        foreach (array('_supreme_qikink_sku', '_supreme_qikink_design_code', '_supreme_qikink_placement_sku') as $key) {
            if (isset($_POST[$key][$i])) { update_post_meta($variation_id, $key, sanitize_text_field(wp_unslash($_POST[$key][$i]))); }
        }
        foreach (array('_supreme_qikink_design_link', '_supreme_qikink_mockup_link') as $key) {
            if (isset($_POST[$key][$i])) { update_post_meta($variation_id, $key, esc_url_raw(wp_unslash($_POST[$key][$i]))); }
        }
        foreach (array('_supreme_qikink_width_inches', '_supreme_qikink_height_inches') as $key) {
            if (isset($_POST[$key][$i])) { update_post_meta($variation_id, $key, wc_format_decimal(wp_unslash($_POST[$key][$i]), 2)); }
        }
    }

    private static function mapped_meta($product, $key) {
        $value = trim((string) $product->get_meta($key, true));
        if ($value === '' && $product->is_type('variation')) {
            $parent = wc_get_product($product->get_parent_id());
            if ($parent) { $value = trim((string) $parent->get_meta($key, true)); }
        }
        return $value;
    }

    private static function token($config) {
        $cached = get_transient(self::TOKEN_TRANSIENT . '_' . $config['mode']);
        if (is_string($cached) && $cached !== '') { return $cached; }
        $response = wp_remote_post($config['base_url'] . '/api/token', array(
            'timeout' => 20,
            'redirection' => 0,
            'headers' => array('Content-Type' => 'application/x-www-form-urlencoded', 'Accept' => 'application/json'),
            'body' => array('ClientId' => $config['client_id'], 'client_secret' => $config['client_secret']),
        ));
        if (is_wp_error($response)) { throw new Exception('Qikink token request failed: ' . $response->get_error_message()); }
        $status = (int) wp_remote_retrieve_response_code($response);
        $data = json_decode(wp_remote_retrieve_body($response), true);
        $token = is_array($data) ? (string) ($data['Accesstoken'] ?? $data['access_token'] ?? '') : '';
        if ($status < 200 || $status >= 300 || $token === '') { throw new Exception('Qikink token request was rejected (HTTP ' . $status . '). Check credentials and API access.'); }
        set_transient(self::TOKEN_TRANSIENT . '_' . $config['mode'], $token, 50 * MINUTE_IN_SECONDS);
        return $token;
    }

    public static function submit_paid_order($order_id) {
        if (get_post_meta($order_id, self::META_STATUS, true)) { return; }
        $config = self::config();
        if (!$config['enabled'] || $config['client_id'] === '' || $config['client_secret'] === '' || $config['mode'] === 'invalid') { return; }
        if ($config['mode'] === 'live' && !($config['enabled'] === true)) { return; }
        $order = wc_get_order($order_id);
        if (!$order || !$order->is_paid()) { return; }

        $line_items = array();
        foreach ($order->get_items('line_item') as $item_id => $item) {
            $product = $item->get_product();
            if (!$product) { self::fail($order, 'Order item product could not be loaded.'); return; }
            $sku = self::mapped_meta($product, '_supreme_qikink_sku');
            if ($sku === '') { self::fail($order, 'Missing Qikink SKU for product/variation ID ' . $product->get_id() . '.'); return; }
            $line = array(
                'search_from_my_products' => $config['mode'] === 'live' ? 1 : 0,
                'price' => wc_format_decimal($item->get_total() / max(1, $item->get_quantity()), 2),
                'quantity' => (string) max(1, (int) $item->get_quantity()),
                'sku' => $sku,
            );
            $design_link = self::mapped_meta($product, '_supreme_qikink_design_link');
            $mockup_link = self::mapped_meta($product, '_supreme_qikink_mockup_link');
            $design_code = self::mapped_meta($product, '_supreme_qikink_design_code');
            if ($design_link !== '' || $mockup_link !== '' || $design_code !== '') {
                $placement = self::mapped_meta($product, '_supreme_qikink_placement_sku');
                $width = self::mapped_meta($product, '_supreme_qikink_width_inches');
                $height = self::mapped_meta($product, '_supreme_qikink_height_inches');
                if (!$design_link || !$mockup_link || !$design_code || !$placement || (float) $width <= 0 || (float) $height <= 0) {
                    self::fail($order, 'Design mapping is incomplete. Add design code, public design/mockup URLs, placement and positive dimensions, or clear all optional design fields to use a saved Qikink product.');
                    return;
                }
                $line['designs'] = array(array(
                    'design_code' => $design_code,
                    'width_inches' => (float) $width,
                    'height_inches' => (float) $height,
                    'placement_sku' => $placement,
                    'design_link' => $design_link,
                    'mockup_link' => $mockup_link,
                ));
            }
            $line_items[] = $line;
        }
        if (!$line_items) { self::fail($order, 'Order contains no eligible line items.'); return; }

        $first = $order->get_billing_first_name();
        $last = $order->get_billing_last_name();
        $address1 = $order->get_shipping_address_1();
        if ($address1 === '') { $address1 = $order->get_billing_address_1(); }
        $address2 = $order->get_shipping_address_2();
        if ($address2 === '') { $address2 = $order->get_billing_address_2(); }
        $city = $order->get_shipping_city() ?: $order->get_billing_city();
        $postcode = $order->get_shipping_postcode() ?: $order->get_billing_postcode();
        $state = $order->get_shipping_state() ?: $order->get_billing_state();
        $country = $order->get_shipping_country() ?: $order->get_billing_country();
        $phone = $order->get_billing_phone();
        $email = $order->get_billing_email();
        if (!$first || !$address1 || !$city || !$postcode || !$country || !$phone || !$email) {
            self::fail($order, 'Customer shipping/billing details are incomplete.'); return;
        }
        if ($config['mode'] === 'live' && $country !== 'IN') {
            self::fail($order, 'This initial Qikink bridge is restricted to India (country code IN).'); return;
        }

        $numeric = preg_replace('/[^A-Za-z0-9]/', '', (string) $order->get_id());
        $order_number = 'SP' . substr($numeric, -13);
        $payload = array(
            'order_number' => $order_number,
            'qikink_shipping' => '1',
            'gateway' => 'Prepaid',
            'total_order_value' => wc_format_decimal($order->get_total(), 2),
            'line_items' => $line_items,
            'shipping_address' => array(
                'first_name' => $first, 'last_name' => $last,
                'address1' => $address1, 'address2' => $address2,
                'phone' => $phone, 'email' => $email,
                'city' => $city, 'zip' => $postcode,
                'province' => $state, 'country' => $country, 'country_code' => $country,
            ),
        );

        // Atomically claim this order before any outbound request. A plain
        // read-then-write allows two concurrent payment-complete hooks to submit
        // duplicate supplier orders.
        if (!add_post_meta($order_id, self::META_STATUS, 'submitting', true)) { return; }
        try {
            $token = self::token($config);
            $response = wp_remote_post($config['base_url'] . '/api/order/create', array(
                'timeout' => 30,
                'redirection' => 0,
                'headers' => array('ClientId' => $config['client_id'], 'Accesstoken' => $token, 'Content-Type' => 'application/json', 'Accept' => 'application/json'),
                'body' => wp_json_encode($payload),
            ));
            if (is_wp_error($response)) { throw new Exception('Qikink order request failed: ' . $response->get_error_message()); }
            $http = (int) wp_remote_retrieve_response_code($response);
            $body = json_decode(wp_remote_retrieve_body($response), true);
            $provider_id = is_array($body) ? (string) ($body['order_id'] ?? '') : '';
            $success = $http >= 200 && $http < 300 && $provider_id !== '' && (
                (string) ($body['status_code'] ?? '') === '200' ||
                (string) ($body['code'] ?? '') === '1' ||
                !empty($body['success'])
            );
            if (!$success) { throw new Exception('Qikink did not confirm order acceptance (HTTP ' . $http . '). Check the Qikink dashboard before retrying.'); }
            update_post_meta($order_id, self::META_STATUS, 'submitted');
            update_post_meta($order_id, self::META_ORDER_ID, sanitize_text_field($provider_id));
            delete_post_meta($order_id, self::META_ERROR);
            $order->add_order_note('Submitted to Qikink. Qikink order ID: ' . sanitize_text_field($provider_id) . '.');
        } catch (Throwable $e) {
            self::fail($order, $e->getMessage(), true);
        }
    }

    private static function fail($order, $message, $already_submitting = false) {
        update_post_meta($order->get_id(), self::META_STATUS, 'error');
        update_post_meta($order->get_id(), self::META_ERROR, sanitize_text_field($message));
        $order->add_order_note('Qikink submission needs review: ' . sanitize_text_field($message) . ' Automatic retry is disabled to avoid duplicate supplier orders.');
    }

    public static function render_order_status($order) {
        if (!current_user_can('manage_woocommerce') || !is_a($order, 'WC_Order')) { return; }
        $status = get_post_meta($order->get_id(), self::META_STATUS, true);
        if (!$status) { return; }
        $provider_id = get_post_meta($order->get_id(), self::META_ORDER_ID, true);
        $error = get_post_meta($order->get_id(), self::META_ERROR, true);
        echo '<p><strong>Qikink status:</strong> ' . esc_html($status);
        if ($provider_id) { echo ' — Provider order ID: ' . esc_html($provider_id); }
        if ($error) { echo '<br><strong>Last issue:</strong> ' . esc_html($error); }
        echo '</p>';
    }
}
Supreme_Qikink_WooCommerce_Bridge::init();
