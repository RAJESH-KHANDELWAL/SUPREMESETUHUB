<?php
declare(strict_types=1);

namespace SupremeSetuHub\\GlobalEcosystem\\PHP\\BadaBusiness;

/**
 * Read-only PHP adapter for the Bada Business resource catalog.
 *
 * It intentionally does not authenticate to Bada Business or perform account,
 * payment, enrollment, lead, or transaction operations. Supply catalog data
 * from the owning application; no referral URLs are hard-coded here.
 */
final class BadaBusinessPHPAdapter
{
    /** @param array<int, array<string, mixed>> $links */
    public function __construct(private readonly array $links = [])
    {
    }

    /** @return array{provider: string, mode: string, connected: bool, links: array<int, array<string, mixed>>, count: int} */
    public function catalog(): array
    {
        return [
            'provider' => 'BADA_BUSINESS',
            'mode' => 'READ_ONLY_RESOURCE_CATALOG',
            'connected' => false,
            'links' => $this->links,
            'count' => count($this->links),
        ];
    }

    /** @return array<int, array<string, mixed>> */
    public function search(string $query): array
    {
        $needle = strtolower(trim($query));
        if ($needle === '') {
            return array_values($this->links);
        }

        return array_values(array_filter($this->links, static function (array $link) use ($needle): bool {
            foreach (['id', 'name', 'type', 'url'] as $field) {
                $value = $link[$field] ?? null;
                if (is_scalar($value) && str_contains(strtolower((string) $value), $needle)) {
                    return true;
                }
            }
            return false;
        }));
    }
}
