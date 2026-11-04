<?php
/** Optional PHP bridge for GLOBAL_VPN_ECOSYSTEM; metadata only, no live provider calls. */
final class VpnEcosystemBridge {
    public static function ecosystem(): string { return 'GLOBAL_VPN_ECOSYSTEM'; }
    public static function connectionStatus(): string { return 'not_configured'; }
}
