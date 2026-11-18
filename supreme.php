<?php
/**
 * Plugin Name: 👑 SUPREMESETUHUB 👑
 * Description: Real WordPress control/API layer for SUPREMESETUHUB. Uses native WordPress plugin APIs and authenticated REST endpoints.
 * Version: 3.0.0
 * Author: 👑 DR RAJESH KHANDELWAL IBC 👑
 * License: GPL-2.0-or-later
 * Text Domain: supremesetuhub
 */

if ( ! defined( 'ABSPATH' ) ) { exit; }

final class SupremeSetuHub {
    const VERSION = '3.0.0';
    const REST_NAMESPACE = 'supreme/v1';

    public function __construct() {
        add_action( 'admin_menu', array( $this, 'register_admin_menu' ) );
        add_action( 'admin_enqueue_scripts', array( $this, 'enqueue_admin_assets' ) );
        add_action( 'rest_api_init', array( $this, 'register_rest_routes' ) );
    }

    private function can_manage() {
        return current_user_can( 'manage_options' ) && current_user_can( 'activate_plugins' );
    }

    private function load_plugin_dependencies() {
        if ( ! function_exists( 'get_plugins' ) ) {
            require_once ABSPATH . 'wp-admin/includes/plugin.php';
        }
        if ( ! function_exists( 'plugins_api' ) ) {
            require_once ABSPATH . 'wp-admin/includes/plugin-install.php';
        }
        if ( ! class_exists( 'Plugin_Upgrader' ) ) {
            require_once ABSPATH . 'wp-admin/includes/class-wp-upgrader.php';
            require_once ABSPATH . 'wp-admin/includes/class-plugin-upgrader.php';
        }
    }

    public function register_admin_menu() {
        if ( ! $this->can_manage() ) { return; }

        add_menu_page( '👑 SUPREMESETUHUB 👑', '👑 SUPREMESETUHUB 👑', 'manage_options', 'supreme-setuhub', array( $this, 'render_dashboard' ), 'dashicons-admin-generic', 2 );
        add_submenu_page( 'supreme-setuhub', '👑 SUPREME DASHBOARD 👑', '👑 SUPREME DASHBOARD 👑', 'manage_options', 'supreme-setuhub', array( $this, 'render_dashboard' ) );
        add_submenu_page( 'supreme-setuhub', '🧩 PLUGINS', '🧩 PLUGINS', 'manage_options', 'supreme-plugins', array( $this, 'render_plugins' ) );
        add_submenu_page( 'supreme-setuhub', '🌍 PLUGIN DIRECTORY', '🌍 PLUGIN DIRECTORY', 'manage_options', 'supreme-directory', array( $this, 'render_directory' ) );
    }

    public function enqueue_admin_assets( $hook ) {
        if ( false === strpos( (string) $hook, 'supreme' ) ) { return; }
        wp_register_style( 'supreme-setuhub-admin', false, array(), self::VERSION );
        wp_enqueue_style( 'supreme-setuhub-admin' );
        wp_add_inline_style( 'supreme-setuhub-admin', ".supreme-wrap,.supreme-wrap *{font-family:'Century Schoolbook','Libre Baskerville',serif!important;font-weight:800!important;box-sizing:border-box}.supreme-wrap{margin:24px 24px 0 0;color:#111}.supreme-header,.supreme-card{background:#fff;border:4px solid #D4AF37;border-radius:22px;box-shadow:0 12px 35px rgba(0,0,0,.10)}.supreme-header{padding:28px;margin-bottom:22px;text-align:center}.supreme-brand{color:#D4AF37;font-size:28px;line-height:1.8;letter-spacing:1.8px;text-transform:uppercase}.supreme-title{display:flex;justify-content:center;align-items:center;gap:22px;font-size:28px;line-height:1.8;letter-spacing:1.8px;text-transform:uppercase}.supreme-crown{font-size:34px}.supreme-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:18px}.supreme-card{padding:24px}.supreme-table{width:100%;border-collapse:collapse}.supreme-table th,.supreme-table td{padding:14px;border-bottom:2px solid #eee;text-align:left;vertical-align:top}.supreme-table th{background:#faf7e8}.supreme-status-active{color:#16834a}.supreme-status-inactive{color:#777}.supreme-notice{padding:14px 18px;border-left:5px solid #D4AF37;background:#faf7e8;margin:0 0 18px}@media(max-width:782px){.supreme-wrap{margin-right:10px}.supreme-title{font-size:20px;gap:10px}.supreme-brand{font-size:21px}.supreme-table{min-width:850px}}" );
    }

    public function register_rest_routes() {
        register_rest_route( self::REST_NAMESPACE, '/status', array('methods'=>WP_REST_Server::READABLE,'callback'=>array($this,'api_status'),'permission_callback'=>array($this,'api_permission')) );
        register_rest_route( self::REST_NAMESPACE, '/plugins', array('methods'=>WP_REST_Server::READABLE,'callback'=>array($this,'api_plugins'),'permission_callback'=>array($this,'api_permission')) );
        register_rest_route( self::REST_NAMESPACE, '/directory', array('methods'=>WP_REST_Server::READABLE,'callback'=>array($this,'api_directory'),'permission_callback'=>array($this,'api_permission'),'args'=>array('search'=>array('required'=>false,'sanitize_callback'=>'sanitize_text_field'),'page'=>array('required'=>false,'default'=>1,'sanitize_callback'=>'absint'))) );
        register_rest_route( self::REST_NAMESPACE, '/plugin/status', array('methods'=>WP_REST_Server::EDITABLE,'callback'=>array($this,'api_plugin_status'),'permission_callback'=>array($this,'api_permission'),'args'=>array('plugin'=>array('required'=>true,'sanitize_callback'=>'sanitize_text_field'),'status'=>array('required'=>true,'sanitize_callback'=>'sanitize_key'))) );
        register_rest_route( self::REST_NAMESPACE, '/plugin/install', array('methods'=>WP_REST_Server::CREATABLE,'callback'=>array($this,'api_plugin_install'),'permission_callback'=>array($this,'api_permission'),'args'=>array('slug'=>array('required'=>true,'sanitize_callback'=>'sanitize_title'))) );
    }

    public function api_permission() { return $this->can_manage(); }

    public function api_status() {
        $plugins = $this->get_installed_plugins();
        return rest_ensure_response(array('success'=>true,'system'=>'SUPREMESETUHUB','version'=>self::VERSION,'wordpress'=>get_bloginfo('version'),'site'=>home_url(),'plugin_count'=>count($plugins),'active_count'=>count(array_filter($plugins,function($p){return !empty($p['active']);}))));
    }

    public function api_plugins() {
        $plugins = $this->get_installed_plugins();
        return rest_ensure_response(array('success'=>true,'count'=>count($plugins),'plugins'=>$plugins));
    }

    public function api_directory( WP_REST_Request $request ) {
        $this->load_plugin_dependencies();
        $search = sanitize_text_field((string)$request->get_param('search'));
        $page = max(1,absint($request->get_param('page')));
        $args = array('per_page'=>24,'page'=>$page,'is_ssl'=>is_ssl(),'fields'=>array('short_description'=>true,'description'=>false,'sections'=>false,'tested'=>true,'requires'=>true,'rating'=>true,'active_installs'=>true));
        if ( '' !== $search ) { $args['search']=$search; }
        $result = plugins_api('query_plugins',$args);
        if ( is_wp_error($result) ) { return new WP_Error('supreme_directory_error',$result->get_error_message(),array('status'=>502)); }
        $items=array();
        foreach((array)$result->plugins as $plugin){$items[]=array('name'=>isset($plugin->name)?$plugin->name:'','slug'=>isset($plugin->slug)?$plugin->slug:'','version'=>isset($plugin->version)?$plugin->version:'','author'=>isset($plugin->author)?wp_strip_all_tags($plugin->author):'','short_description'=>isset($plugin->short_description)?wp_strip_all_tags($plugin->short_description):'','rating'=>isset($plugin->rating)?(int)$plugin->rating:0,'active_installs'=>isset($plugin->active_installs)?(int)$plugin->active_installs:0,'homepage'=>isset($plugin->homepage)?esc_url_raw($plugin->homepage):'');}
        return rest_ensure_response(array('success'=>true,'page'=>$page,'pages'=>isset($result->info['pages'])?(int)$result->info['pages']:0,'results'=>isset($result->info['results'])?(int)$result->info['results']:count($items),'search'=>$search,'plugins'=>$items));
    }

    public function api_plugin_status( WP_REST_Request $request ) {
        $this->load_plugin_dependencies();
        $plugin=plugin_basename($request->get_param('plugin')); $status=sanitize_key($request->get_param('status'));
        if(!in_array($status,array('active','inactive'),true)){return new WP_Error('supreme_invalid_status','Status must be active or inactive.',array('status'=>400));}
        if(!file_exists(WP_PLUGIN_DIR.'/'.$plugin)){return new WP_Error('supreme_plugin_not_found','Plugin is not installed.',array('status'=>404));}
        if('active'===$status){$result=activate_plugin($plugin,'',false,false);}else{deactivate_plugins($plugin,false,false);$result=true;}
        if(is_wp_error($result)){return new WP_Error('supreme_plugin_status_failed',$result->get_error_message(),array('status'=>500));}
        return rest_ensure_response(array('success'=>true,'plugin'=>$plugin,'status'=>is_plugin_active($plugin)?'active':'inactive'));
    }

    public function api_plugin_install( WP_REST_Request $request ) {
        $this->load_plugin_dependencies(); $slug=sanitize_title($request->get_param('slug'));
        if(''===$slug){return new WP_Error('supreme_invalid_slug','Plugin slug is required.',array('status'=>400));}
        $info=plugins_api('plugin_information',array('slug'=>$slug,'is_ssl'=>is_ssl(),'fields'=>array('sections'=>false)));
        if(is_wp_error($info)){return new WP_Error('supreme_plugin_info_failed',$info->get_error_message(),array('status'=>502));}
        if(empty($info->download_link)){return new WP_Error('supreme_no_download','WordPress.org did not provide a download package for this plugin.',array('status'=>502));}
        $skin=new WP_Ajax_Upgrader_Skin(); $upgrader=new Plugin_Upgrader($skin); $result=$upgrader->install($info->download_link);
        if(is_wp_error($result)){return new WP_Error('supreme_plugin_install_failed',$result->get_error_message(),array('status'=>500));}
        if(!$result){return new WP_Error('supreme_plugin_install_failed','WordPress could not complete the plugin installation.',array('status'=>500));}
        return rest_ensure_response(array('success'=>true,'slug'=>$slug,'installed'=>true));
    }

    private function get_installed_plugins() {
        $this->load_plugin_dependencies(); $all=get_plugins(); $active=(array)get_option('active_plugins',array()); $network=is_multisite()?(array)get_site_option('active_sitewide_plugins',array()):array(); $result=array();
        foreach($all as $file=>$data){$is_active=in_array($file,$active,true); if(is_multisite()&&isset($network[$file])){$is_active=true;} $result[]=array('plugin'=>$file,'name'=>isset($data['Name'])?wp_strip_all_tags($data['Name']):$file,'version'=>isset($data['Version'])?$data['Version']:'','author'=>isset($data['Author'])?wp_strip_all_tags($data['Author']):'','description'=>isset($data['Description'])?wp_strip_all_tags($data['Description']):'','plugin_uri'=>isset($data['PluginURI'])?esc_url_raw($data['PluginURI']):'','text_domain'=>isset($data['TextDomain'])?$data['TextDomain']:'','active'=>$is_active);}
        return $result;
    }

    private function render_header($title) { ?>
        <div class="supreme-header"><div class="supreme-brand">👑 DR RAJESH KHANDELWAL IBC 👑</div><div class="supreme-title"><span class="supreme-crown">👑</span><span><?php echo esc_html($title); ?></span><span class="supreme-crown">👑</span></div></div>
    <?php }

    public function render_dashboard() {
        if(!$this->can_manage()){wp_die(esc_html__('Access denied.','supremesetuhub'));}
        $plugins=$this->get_installed_plugins(); $active=count(array_filter($plugins,function($p){return !empty($p['active']);})); ?>
        <div class="supreme-wrap"><?php $this->render_header('SUPREME DASHBOARD'); ?><div class="supreme-grid">
            <div class="supreme-card"><h2>🧩 PLUGINS</h2><p>REAL WORDPRESS PLUGINS</p><h2><?php echo esc_html(count($plugins)); ?></h2></div>
            <div class="supreme-card"><h2>✅ ACTIVE</h2><p>ACTIVE WORDPRESS PLUGINS</p><h2><?php echo esc_html($active); ?></h2></div>
            <div class="supreme-card"><h2>🌍 DIRECTORY</h2><p>REAL WORDPRESS.ORG PLUGIN DIRECTORY API</p><strong>CONNECTED</strong></div>
            <div class="supreme-card"><h2>🔐 OWNER CONTROL</h2><p>INSTALLATION AND ACTIVATION REQUIRE WORDPRESS ADMIN CAPABILITY.</p><strong>PROTECTED</strong></div>
        </div><div class="supreme-card" style="margin-top:20px;"><h2>📡 LIVE WORDPRESS</h2><p>WORDPRESS: <strong><?php echo esc_html(get_bloginfo('version')); ?></strong></p><p>PLUGIN SOURCE: <strong>WORDPRESS CORE PLUGIN API</strong></p><p>SUPREME API: <strong><?php echo esc_html(self::REST_NAMESPACE); ?></strong></p></div></div>
    <?php }

    public function render_plugins() {
        if(!$this->can_manage()){wp_die(esc_html__('Access denied.','supremesetuhub'));} $plugins=$this->get_installed_plugins(); ?>
        <div class="supreme-wrap"><?php $this->render_header('PLUGINS'); ?><div class="supreme-card"><h2>📦 REAL INSTALLED WORDPRESS PLUGINS</h2><p>DATA IS READ DIRECTLY FROM WORDPRESS CORE PLUGIN DATA. NO HARDCODED PLUGIN LIST.</p></div><div class="supreme-card" style="margin-top:20px;overflow:auto;"><table class="supreme-table"><thead><tr><th>PLUGIN</th><th>VERSION</th><th>AUTHOR</th><th>STATUS</th></tr></thead><tbody>
        <?php foreach($plugins as $plugin): ?><tr><td><strong><?php echo esc_html($plugin['name']); ?></strong><div><?php echo esc_html($plugin['plugin']); ?></div></td><td><?php echo esc_html($plugin['version']); ?></td><td><?php echo esc_html($plugin['author']); ?></td><td><?php if($plugin['active']): ?><span class="supreme-status-active">● ACTIVE</span><?php else: ?><span class="supreme-status-inactive">● INACTIVE</span><?php endif; ?></td></tr><?php endforeach; ?>
        </tbody></table></div></div>
    <?php }

    public function render_directory() {
        if(!$this->can_manage()){wp_die(esc_html__('Access denied.','supremesetuhub'));} $this->load_plugin_dependencies(); $result=plugins_api('query_plugins',array('per_page'=>24,'page'=>1,'is_ssl'=>is_ssl(),'browse'=>'popular','fields'=>array('short_description'=>true,'rating'=>true,'active_installs'=>true))); ?>
        <div class="supreme-wrap"><?php $this->render_header('PLUGIN DIRECTORY'); ?><div class="supreme-card"><h2>🌍 OFFICIAL WORDPRESS PLUGIN DIRECTORY</h2><p>THIS DATA COMES FROM THE NATIVE WORDPRESS.ORG PLUGIN API.</p><?php if(is_wp_error($result)): ?><div class="supreme-notice"><?php echo esc_html($result->get_error_message()); ?></div><?php else: ?><div style="overflow:auto;"><table class="supreme-table"><thead><tr><th>PLUGIN</th><th>VERSION</th><th>AUTHOR</th><th>INSTALLS</th><th>RATING</th></tr></thead><tbody><?php foreach((array)$result->plugins as $plugin): ?><tr><td><strong><?php echo esc_html($plugin->name); ?></strong><div><?php echo esc_html($plugin->short_description); ?></div></td><td><?php echo esc_html($plugin->version); ?></td><td><?php echo wp_kses_post($plugin->author); ?></td><td><?php echo esc_html(number_format_i18n((int)$plugin->active_installs)); ?></td><td><?php echo esc_html((int)$plugin->rating); ?>%</td></tr><?php endforeach; ?></tbody></table></div><?php endif; ?></div></div>
    <?php }
}

new SupremeSetuHub();
