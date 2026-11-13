<?php
/**
 * SUPREMESETUHUB core PHP module.
 * Main WordPress plugin bootstrap loads this module.
 */
if (!defined('ABSPATH')) { exit; }

if (!function_exists('supremesetuhub_core_manifest')) {
    function supremesetuhub_core_manifest() {
        return array(
            'hub' => 'SUPREMESETUHUB',
            'brand' => '👑 DR RAJESH KHANDELWAL IBC 👑',
            'plugins' => array(
                'supreme' => 'SUPREME by SUPREMESETUHUB',
                'supreme_ecosystem' => 'SUPREME ECOSYSTEM by SUPREMESETUHUB',
            ),
        );
    }
}
