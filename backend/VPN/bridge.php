<?php
/** Optional PHP interoperability boundary for the VPN domain.
 * This file is not executed by the Python backend. Do not put secrets here.
 */
final class VpnDomainBridge {
    public static function domain(): string { return 'VPN'; }
    public static function status(): string { return 'scaffold'; }
}
