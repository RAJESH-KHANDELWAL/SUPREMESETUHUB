<?php
/**
 * Plugin Name: 👑 SUPREMESETUHUB 👑
 * Description: Real WordPress integration layer for SUPREMESETUHUB.
 * Version: 2.0.0
 * Author: 👑 DR RAJESH KHANDELWAL IBC 👑
 * License: GPL-2.0-or-later
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

final class SupremeSetuHub {

	const VERSION = '2.0.0';

	public function __construct() {

		add_action(
			'admin_menu',
			array( $this, 'admin_menu' )
		);

		add_action(
			'rest_api_init',
			array( $this, 'rest_api' )
		);

		add_action(
			'admin_enqueue_scripts',
			array( $this, 'admin_css' )
		);
	}

	/* ---------------------------------------------------------
	 * PERMISSION
	 * --------------------------------------------------------- */

	private function allowed() {

		return current_user_can( 'manage_options' );
	}

	/* ---------------------------------------------------------
	 * ADMIN MENU
	 * --------------------------------------------------------- */

	public function admin_menu() {

		if ( ! $this->allowed() ) {
			return;
		}

		add_menu_page(
			'👑 SUPREMESETUHUB 👑',
			'👑 SUPREMESETUHUB 👑',
			'manage_options',
			'supreme-setuhub',
			array( $this, 'dashboard' ),
			'dashicons-admin-generic',
			2
		);

		add_submenu_page(
			'supreme-setuhub',
			'👑 SUPREME DASHBOARD 👑',
			'👑 SUPREME DASHBOARD 👑',
			'manage_options',
			'supreme-setuhub',
			array( $this, 'dashboard' )
		);

		add_submenu_page(
			'supreme-setuhub',
			'🧩 PLUGINS',
			'🧩 PLUGINS',
			'manage_options',
			'supreme-plugins',
			array( $this, 'plugins_page' )
		);

		add_submenu_page(
			'supreme-setuhub',
			'➕ ADD PLUGINS',
			'➕ ADD PLUGINS',
			'manage_options',
			'supreme-add-plugins',
			array( $this, 'add_plugins_page' )
		);

		add_submenu_page(
			'supreme-setuhub',
			'📝 PLUGIN EDITOR',
			'📝 PLUGIN EDITOR',
			'manage_options',
			'supreme-plugin-editor',
			array( $this, 'editor_page' )
		);
	}

	/* ---------------------------------------------------------
	 * REST API
	 * --------------------------------------------------------- */

	public function rest_api() {

		register_rest_route(
			'supreme/v1',
			'/status',
			array(
				'methods'             => WP_REST_Server::READABLE,
				'callback'            => array( $this, 'api_status' ),
				'permission_callback' => array( $this, 'api_permission' ),
			)
		);

		register_rest_route(
			'supreme/v1',
			'/plugins',
			array(
				'methods'             => WP_REST_Server::READABLE,
				'callback'            => array( $this, 'api_plugins' ),
				'permission_callback' => array( $this, 'api_permission' ),
			)
		);
	}

	public function api_permission() {

		return $this->allowed();
	}

	public function api_status() {

		return rest_ensure_response(
			array(
				'success'   => true,
				'system'    => 'SUPREMESETUHUB',
				'version'   => self::VERSION,
				'wordpress' => get_bloginfo( 'version' ),
				'site'      => home_url(),
				'plugins'   => count( $this->get_plugins() ),
			)
		);
	}

	public function api_plugins() {

		$plugins = $this->get_plugins();

		return rest_ensure_response(
			array(
				'success' => true,
				'count'   => count( $plugins ),
				'plugins' => $plugins,
			)
		);
	}

	/* ---------------------------------------------------------
	 * WORDPRESS PLUGIN DATA
	 * --------------------------------------------------------- */

	private function load_plugin_api() {

		if ( ! function_exists( 'get_plugins' ) ) {

			require_once ABSPATH . 'wp-admin/includes/plugin.php';
		}
	}

	private function get_plugins() {

		$this->load_plugin_api();

		$all_plugins = get_plugins();

		$active_plugins = (array) get_option(
			'active_plugins',
			array()
		);

		$result = array();

		foreach ( $all_plugins as $file => $plugin ) {

			$result[] = array(
				'file'        => $file,
				'name'        => isset( $plugin['Name'] )
					? $plugin['Name']
					: $file,
				'version'     => isset( $plugin['Version'] )
					? $plugin['Version']
					: '',
				'author'      => isset( $plugin['Author'] )
					? wp_strip_all_tags( $plugin['Author'] )
					: '',
				'description' => isset( $plugin['Description'] )
					? wp_strip_all_tags( $plugin['Description'] )
					: '',
				'active'      => in_array(
					$file,
					$active_plugins,
					true
				),
				'plugin_uri'  => isset( $plugin['PluginURI'] )
					? $plugin['PluginURI']
					: '',
			);
		}

		return $result;
	}

	/* ---------------------------------------------------------
	 * ADMIN CSS
	 * --------------------------------------------------------- */

	public function admin_css() {

		$screen = get_current_screen();

		if (
			! $screen ||
			false === strpos(
				(string) $screen->id,
				'supreme'
			)
		) {
			return;
		}

		wp_register_style(
			'supreme-setuhub-admin',
			false,
			array(),
			self::VERSION
		);

		wp_enqueue_style(
			'supreme-setuhub-admin'
		);

		wp_add_inline_style(
			'supreme-setuhub-admin',
			'
			.supreme-wrap {
				margin: 25px 25px 0 0;
			}

			.supreme-header {
				background: #fff;
				border: 1px solid #e5e5e5;
				border-radius: 18px;
				padding: 28px;
				margin-bottom: 22px;
				box-shadow: 0 8px 25px rgba(0,0,0,.05);
			}

			.supreme-brand {
				text-align: center;
				font-size: 27px;
				font-weight: 800;
				margin-bottom: 12px;
			}

			.supreme-title {
				display: flex;
				justify-content: center;
				align-items: center;
				gap: 24px;
				font-size: 24px;
				font-weight: 800;
			}

			.supreme-crown {
				font-size: 34px;
			}

			.supreme-grid {
				display: grid;
				grid-template-columns:
					repeat(auto-fit,minmax(240px,1fr));
				gap: 18px;
			}

			.supreme-card {
				background: #fff;
				border: 1px solid #e5e5e5;
				border-radius: 16px;
				padding: 24px;
				box-shadow: 0 6px 20px rgba(0,0,0,.04);
			}

			.supreme-button {
				display: inline-block;
				background: #2271b1;
				color: #fff !important;
				padding: 10px 16px;
				border-radius: 7px;
				text-decoration: none;
				font-weight: 700;
			}

			.supreme-table {
				width: 100%;
				border-collapse: collapse;
			}

			.supreme-table th,
			.supreme-table td {
				padding: 13px;
				border-bottom: 1px solid #eee;
				text-align: left;
				vertical-align: top;
			}

			.supreme-table th {
				background: #f7f7f7;
			}

			.supreme-active {
				color: #16834a;
				font-weight: 700;
			}

			.supreme-inactive {
				color: #777;
				font-weight: 700;
			}

			.supreme-file {
				font-family: monospace;
				font-size: 12px;
				color: #777;
			}
			'
		);
	}

	/* ---------------------------------------------------------
	 * DASHBOARD
	 * --------------------------------------------------------- */

	public function dashboard() {

		if ( ! $this->allowed() ) {
			wp_die( 'Access denied.' );
		}

		$plugins = $this->get_plugins();

		$active = 0;

		foreach ( $plugins as $plugin ) {

			if ( ! empty( $plugin['active'] ) ) {
				$active++;
			}
		}

		?>

		<div class="supreme-wrap">

			<div class="supreme-header">

				<div class="supreme-brand">
					👑 DR RAJESH KHANDELWAL IBC 👑
				</div>

				<div class="supreme-title">

					<span class="supreme-crown">👑</span>

					<span>
						SUPREME DASHBOARD
					</span>

					<span class="supreme-crown">👑</span>

				</div>

			</div>

			<div class="supreme-grid">

				<div class="supreme-card">

					<h2>🧩 PLUGINS</h2>

					<p>
						REAL WordPress installed plugins.
					</p>

					<h2>
						<?php echo esc_html( count( $plugins ) ); ?>
					</h2>

					<a
						class="supreme-button"
						href="<?php
							echo esc_url(
								admin_url(
									'admin.php?page=supreme-plugins'
								)
							);
						?>"
					>
						OPEN PLUGINS
					</a>

				</div>

				<div class="supreme-card">

					<h2>➕ ADD PLUGINS</h2>

					<p>
						Use the real WordPress Plugin Directory.
					</p>

					<a
						class="supreme-button"
						href="<?php
							echo esc_url(
								admin_url(
									'plugin-install.php'
								)
							);
						?>"
					>
						OPEN ADD PLUGINS
					</a>

				</div>

				<div class="supreme-card">

					<h2>📝 PLUGIN EDITOR</h2>

					<p>
						Administrator-only WordPress Plugin Editor.
					</p>

					<a
						class="supreme-button"
						href="<?php
							echo esc_url(
								admin_url(
									'plugin-editor.php'
								)
							);
						?>"
					>
						OPEN EDITOR
					</a>

				</div>

				<div class="supreme-card">

					<h2>🌐 GITHUB</h2>

					<p>
						SUPREMESETUHUB source repository.
					</p>

					<strong>
						CONNECTED SOURCE
					</strong>

				</div>

				<div class="supreme-card">

					<h2>🤖 AI</h2>

					<p>
						AI integration layer.
					</p>

					<strong>
						READY
					</strong>

				</div>

				<div class="supreme-card">

					<h2>🔐 OWNER</h2>

					<p>
						SUPREMESETUHUB is restricted to administrators.
					</p>

					<strong>
						OWNER ONLY
					</strong>

				</div>

			</div>

			<div
				class="supreme-card"
				style="margin-top:20px;"
			>

				<h2>
					📡 LIVE WORDPRESS
				</h2>

				<p>
					WordPress:
					<strong>
						<?php
						echo esc_html(
							get_bloginfo( 'version' )
						);
						?>
					</strong>
				</p>

				<p>
					Installed Plugins:
					<strong>
						<?php
						echo esc_html(
							count( $plugins )
						);
						?>
					</strong>
				</p>

				<p>
					Active Plugins:
					<strong>
						<?php
						echo esc_html( $active );
						?>
					</strong>
				</p>

				<p>
					Site:
					<strong>
						<?php
						echo esc_html(
							home_url()
						);
						?>
					</strong>
				</p>

			</div>

		</div>

		<?php
	}

	/* ---------------------------------------------------------
	 * REAL INSTALLED PLUGINS
	 * --------------------------------------------------------- */

	public function plugins_page() {

		if ( ! $this->allowed() ) {
			wp_die( 'Access denied.' );
		}

		$plugins = $this->get_plugins();

		?>

		<div class="supreme-wrap">

			<div class="supreme-header">

				<div class="supreme-brand">
					👑 DR RAJESH KHANDELWAL IBC 👑
				</div>

				<div class="supreme-title">

					<span class="supreme-crown">👑</span>

					<span>PLUGINS</span>

					<span class="supreme-crown">👑</span>

				</div>

			</div>

			<div class="supreme-card">

				<h2>
					📦 REAL INSTALLED PLUGINS
				</h2>

				<p>
					This list is read directly from WordPress.
				</p>

			</div>

			<div
				class="supreme-card"
				style="margin-top:20px;overflow:auto;"
			>

				<table class="supreme-table">

					<thead>

						<tr>

							<th>PLUGIN</th>
							<th>VERSION</th>
							<th>AUTHOR</th>
							<th>STATUS</th>

						</tr>

					</thead>

					<tbody>

					<?php foreach ( $plugins as $plugin ) : ?>

						<tr>

							<td>

								<strong>
									<?php
									echo esc_html(
										$plugin['name']
									);
									?>
								</strong>

								<div class="supreme-file">
									<?php
									echo esc_html(
										$plugin['file']
									);
									?>
								</div>

							</td>

							<td>
								<?php
								echo esc_html(
									$plugin['version']
								);
								?>
							</td>

							<td>
								<?php
								echo esc_html(
									$plugin['author']
								);
								?>
							</td>

							<td>

								<?php if ( $plugin['active'] ) : ?>

									<span class="supreme-active">
										● ACTIVE
									</span>

								<?php else : ?>

									<span class="supreme-inactive">
										● INACTIVE
									</span>

								<?php endif; ?>

							</td>

						</tr>

					<?php endforeach; ?>

					</tbody>

				</table>

			</div>

		</div>

		<?php
	}

	/* ---------------------------------------------------------
	 * REAL WORDPRESS PLUGIN INSTALL SCREEN
	 * --------------------------------------------------------- */

	public function add_plugins_page() {

		if ( ! $this->allowed() ) {
			wp_die( 'Access denied.' );
		}

		?>

		<div class="supreme-wrap">

			<div class="supreme-header">

				<div class="supreme-brand">
					👑 DR RAJESH KHANDELWAL IBC 👑
				</div>

				<div class="supreme-title">

					<span class="supreme-crown">👑</span>

					<span>ADD PLUGINS</span>

					<span class="supreme-crown">👑</span>

				</div>

			</div>

			<div class="supreme-card">

				<h2>
					🌍 OFFICIAL WORDPRESS PLUGIN DIRECTORY
				</h2>

				<p>
					This opens the real WordPress plugin
					installation screen.
				</p>

				<a
					class="supreme-button"
					href="<?php
						echo esc_url(
							admin_url(
								'plugin-install.php'
							)
						);
					?>"
				>
					OPEN WORDPRESS PLUGINS
				</a>

			</div>

		</div>

		<?php
	}

	/* ---------------------------------------------------------
	 * REAL WORDPRESS PLUGIN EDITOR
	 * --------------------------------------------------------- */

	public function editor_page() {

		if ( ! $this->allowed() ) {
			wp_die( 'Access denied.' );
		}

		?>

		<div class="supreme-wrap">

			<div class="supreme-header">

				<div class="supreme-brand">
					👑 DR RAJESH KHANDELWAL IBC 👑
				</div>

				<div class="supreme-title">

					<span class="supreme-crown">👑</span>

					<span>PLUGIN EDITOR</span>

					<span class="supreme-crown">👑</span>

				</div>

			</div>

			<div class="supreme-card">

				<h2>
					📝 REAL WORDPRESS PLUGIN FILE EDITOR
				</h2>

				<p>
					This uses the existing WordPress Plugin
					File Editor.
				</p>

				<a
					class="supreme-button"
					href="<?php
						echo esc_url(
							admin_url(
								'plugin-editor.php'
							)
						);
					?>"
				>
					OPEN WORDPRESS EDITOR
				</a>

			</div>

		</div>

		<?php
	}
}

new SupremeSetuHub();
