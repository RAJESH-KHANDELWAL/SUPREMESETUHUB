<?php
declare(strict_types=1);

final class DigitalDesignRepository
{
    public function __construct(private readonly PDO $pdo)
    {
    }

    /**
     * Return only published designs with a price for the selected market.
     * Private original-file keys are intentionally never selected.
     *
     * @return list<array<string, mixed>>
     */
    public function publishedCatalog(string $market, int $limit = 24, int $offset = 0): array
    {
        if (!in_array($market, ['IN', 'GLOBAL'], true)) {
            throw new InvalidArgumentException('Market must be IN or GLOBAL.');
        }

        $limit = max(1, min($limit, 100));
        $offset = max(0, $offset);

        $sql = <<<'SQL'
            SELECT
                d.id,
                d.slug,
                d.title,
                d.description,
                d.category,
                d.preview_path,
                d.license_label,
                p.market_code,
                p.currency_code,
                p.price_minor,
                d.published_at
            FROM digital_designs AS d
            INNER JOIN digital_design_prices AS p
                ON p.design_id = d.id
               AND p.market_code = :market
               AND p.is_active = 1
            WHERE d.status = 'PUBLISHED'
            ORDER BY d.published_at DESC, d.id DESC
            LIMIT :row_limit OFFSET :row_offset
        SQL;

        $statement = $this->pdo->prepare($sql);
        $statement->bindValue(':market', $market, PDO::PARAM_STR);
        $statement->bindValue(':row_limit', $limit, PDO::PARAM_INT);
        $statement->bindValue(':row_offset', $offset, PDO::PARAM_INT);
        $statement->execute();

        $rows = $statement->fetchAll();
        foreach ($rows as &$row) {
            $minor = (int) $row['price_minor'];
            $row['price'] = number_format($minor / 100, 2, '.', '');
            $row['price_minor'] = $minor;
        }
        unset($row);

        return $rows;
    }
}
