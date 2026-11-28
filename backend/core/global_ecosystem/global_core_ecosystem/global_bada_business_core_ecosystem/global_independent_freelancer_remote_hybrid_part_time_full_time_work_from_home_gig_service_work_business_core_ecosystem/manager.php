<?php
declare(strict_types=1);

/** PHP interoperability facade; Python/Global Core own canonical taxonomy metadata. */
final class GlobalIndependentWorkServiceBusinessCoreManager
{
    public const ECOSYSTEM_ID = 'GLOBAL-INDEPENDENT-FREELANCER-REMOTE-HYBRID-PART-TIME-FULL-TIME-WORK-FROM-HOME-GIG-SERVICE-WORK-BUSINESS-CORE-ECOSYSTEM';

    public static function status(): array
    {
        return [
            'ecosystem_id' => self::ECOSYSTEM_ID,
            'parent_id' => 'GLOBAL-BADA-BUSINESS-CORE-ECOSYSTEM',
            'status' => 'CORE_CATALOG_ONLY',
            'canonical_owner' => 'GLOBAL-INDEPENDENT-FREELANCER-REMOTE-HYBRID-PART-TIME-FULL-TIME-WORK-FROM-HOME-GIG-CORE-ECOSYSTEM',
            'business_capabilities' => ['SERVICE_WORK', 'SERVICE_WORK_BUSINESS'],
            'python_is_canonical' => true,
        ];
    }
}
