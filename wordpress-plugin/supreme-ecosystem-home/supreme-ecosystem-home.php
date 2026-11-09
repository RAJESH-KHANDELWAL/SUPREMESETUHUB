<?php
/**
 * Plugin Name: SUPREME ECOSYSTEM Home
 * Description: Responsive SUPREME ECOSYSTEM homepage sections and platform directory for WordPress.
 * Version: 1.0.0
 * Requires at least: 6.2
 * Requires PHP: 7.4
 * Author: DR RAJESH KHANDELWAL IBC
 * License: GPL-2.0-or-later
 * Text Domain: supreme-ecosystem-home
 */
if (!defined('ABSPATH')) { exit; }

final class Supreme_Ecosystem_Home {
    public static function init() {
        add_shortcode('supreme_ecosystem_home', array(__CLASS__, 'render'));
    }

    public static function render($atts = array()) {
        $atts = shortcode_atts(array(
            'pod_url' => home_url('/print-on-demand/'),
            'digital_url' => home_url('/digital-store/'),
            'services_url' => home_url('/services/'),
            'about_url' => home_url('/about/'),
        ), $atts, 'supreme_ecosystem_home');
        $cards = array(
            array('icon' => '🎨', 'title' => 'SUPREME PRINT ON DEMAND', 'desc' => 'Explore custom T-shirts, hoodies, mugs, posters, tote bags and more.', 'url' => $atts['pod_url'], 'cta' => 'EXPLORE POD'),
            array('icon' => '💻', 'title' => 'DIGITAL STORE', 'desc' => 'A home for digital products, creative assets and future downloadable resources.', 'url' => $atts['digital_url'], 'cta' => 'EXPLORE DIGITAL'),
            array('icon' => '🚀', 'title' => 'DIGITAL SERVICES', 'desc' => 'Discover website, online presence and digital business service offerings.', 'url' => $atts['services_url'], 'cta' => 'VIEW SERVICES'),
            array('icon' => '🌍', 'title' => 'OUR MISSION', 'desc' => 'One connected digital ecosystem designed to bring services and ideas together.', 'url' => $atts['about_url'], 'cta' => 'LEARN MORE'),
        );
        ob_start(); ?>
        <section class="supreme-eco" aria-label="SUPREME ECOSYSTEM">
          <style>
            .supreme-eco{--se-blue:#0b5cff;--se-ink:#101828;--se-muted:#475467;color:var(--se-ink);font-family:inherit}
            .supreme-eco *{box-sizing:border-box}.supreme-eco-hero{padding:clamp(28px,6vw,64px);border-radius:24px;background:linear-gradient(135deg,#071b49,#0b5cff 65%,#62a5ff);color:#fff;overflow:hidden}
            .supreme-eco-kicker{font-weight:800;letter-spacing:.12em;font-size:.78rem;opacity:.9}.supreme-eco h1{color:inherit;font-size:clamp(2rem,5vw,3.5rem);line-height:1.08;margin:.7rem 0 1rem}.supreme-eco-hero p{max-width:760px;font-size:1.08rem;line-height:1.7;margin:0 0 22px}
            .supreme-eco-btn{display:inline-block;background:#fff;color:#0b45bd!important;padding:12px 18px;border-radius:12px;font-weight:900;text-decoration:none!important;margin:4px 8px 4px 0}.supreme-eco-section-title{margin:30px 0 14px;font-size:clamp(1.4rem,3vw,2rem)}
            .supreme-eco-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,230px),1fr));gap:16px}.supreme-eco-card{padding:22px;border:1px solid #dce5f2;border-radius:18px;background:#fff;box-shadow:0 8px 28px rgba(16,24,40,.05);display:flex;flex-direction:column;align-items:flex-start;min-height:220px}
            .supreme-eco-icon{font-size:2rem}.supreme-eco-card h3{font-size:1.08rem;line-height:1.4;margin:12px 0 8px}.supreme-eco-card p{color:var(--se-muted);line-height:1.65;margin:0 0 18px}.supreme-eco-card a{margin-top:auto;color:var(--se-blue);font-weight:900;text-decoration:none}.supreme-eco-note{margin-top:18px;padding:14px 16px;background:#f2f6ff;border-radius:12px;color:#344054;font-size:.93rem}
          </style>
          <div class="supreme-eco-hero">
            <div class="supreme-eco-kicker">ONE CONNECTED DIGITAL WORLD</div>
            <h1>👑 SUPREME ECOSYSTEM</h1>
            <p>Welcome to SUPREMESETUHUB — a growing digital platform bringing products, creative ideas and online services into one connected destination.</p>
            <a class="supreme-eco-btn" href="<?php echo esc_url($atts['pod_url']); ?>">🎨 SUPREME PRINT ON DEMAND</a>
            <a class="supreme-eco-btn" href="<?php echo esc_url($atts['services_url']); ?>">🚀 EXPLORE SERVICES</a>
          </div>
          <h2 class="supreme-eco-section-title">EXPLORE THE ECOSYSTEM</h2>
          <div class="supreme-eco-grid">
          <?php foreach ($cards as $card) : ?>
            <article class="supreme-eco-card">
              <div class="supreme-eco-icon" aria-hidden="true"><?php echo esc_html($card['icon']); ?></div>
              <h3><?php echo esc_html($card['title']); ?></h3>
              <p><?php echo esc_html($card['desc']); ?></p>
              <a href="<?php echo esc_url($card['url']); ?>"><?php echo esc_html($card['cta']); ?> →</a>
            </article>
          <?php endforeach; ?>
          </div>
          <p class="supreme-eco-note"><strong>Platform status:</strong> Catalog listings and service information may be available before checkout or fulfilment is enabled. Confirm availability and final pricing before placing or paying for an order.</p>
        </section>
        <?php
        return ob_get_clean();
    }
}
Supreme_Ecosystem_Home::init();
