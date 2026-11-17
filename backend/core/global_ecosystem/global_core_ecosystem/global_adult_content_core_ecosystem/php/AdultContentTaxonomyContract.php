<?php

declare(strict_types=1);

namespace SupremeSetuHub\Core\GlobalAdultContent;

final class AdultContentTaxonomyContract
{
    public const ECOSYSTEM_ID = 'GLOBAL-ADULT-CONTENT-CORE-ECOSYSTEM';

    public const ORIENTATION_LABELS = [
        'STRAIGHT',
        'GAY',
        'BISEXUAL',
        'OTHER',
        'UNSPECIFIED',
    ];

    public const PARTICIPANT_CONFIGURATIONS = [
        'DIFFERENT_GENDER',
        'SAME_GENDER',
        'MULTIPLE_GENDERS',
        'UNSPECIFIED',
    ];

    public static function isValidOrientation(string $value): bool
    {
        return in_array(strtoupper(trim($value)), self::ORIENTATION_LABELS, true);
    }

    /**
     * Returns policy requirements only; this method does not verify evidence.
     *
     * @return array<string, bool|string>
     */
    public static function policyRequirements(): array
    {
        return [
            'all_depicted_persons_verified_adults' => true,
            'informed_consent_documented' => true,
            'distribution_rights_documented' => true,
            'moderation_approved' => true,
            'jurisdiction_permitted' => true,
            'status' => 'POLICY_METADATA_ONLY',
        ];
    }
}
