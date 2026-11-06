<?php
/** Optional PHP interoperability boundary for the VPS domain.
 * This file is not executed by the Python backend. Do not put secrets here.
 */
final class VpsDomainBridge {
    public static function domain(): string { return 'VPS'; }
    public static function status(): string { return 'scaffold'; }
}
