<?php
/** Optional PHP bridge for GLOBAL_VPS_ECOSYSTEM; metadata only, no live provider calls. */
final class VpsEcosystemBridge {
    public static function ecosystem(): string { return 'GLOBAL_VPS_ECOSYSTEM'; }
    public static function connectionStatus(): string { return 'not_configured'; }
}
