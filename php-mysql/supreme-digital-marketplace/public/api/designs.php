<?php
declare(strict_types=1);

require_once dirname(__DIR__, 2) . '/src/Database.php';
require_once dirname(__DIR__, 2) . '/src/DigitalDesignRepository.php';

header('Content-Type: application/json; charset=utf-8');
header('X-Content-Type-Options: nosniff');
header('Cache-Control: public, max-age=60, stale-while-revalidate=120');

if ($_SERVER['REQUEST_METHOD'] !== 'GET') {
    header('Allow: GET');
    http_response_code(405);
    echo json_encode(['success' => false, 'error' => 'METHOD_NOT_ALLOWED']);
    exit;
}

$market = strtoupper(trim((string) ($_GET['market'] ?? 'IN')));
if (!in_array($market, ['IN', 'GLOBAL'], true)) {
    http_response_code(422);
    echo json_encode(['success' => false, 'error' => 'MARKET_MUST_BE_IN_OR_GLOBAL']);
    exit;
}

$limit = filter_var($_GET['limit'] ?? 24, FILTER_VALIDATE_INT);
$offset = filter_var($_GET['offset'] ?? 0, FILTER_VALIDATE_INT);
if ($limit === false || $offset === false || $limit < 1 || $offset < 0) {
    http_response_code(422);
    echo json_encode(['success' => false, 'error' => 'INVALID_PAGINATION']);
    exit;
}

try {
    $repository = new DigitalDesignRepository(Database::connection());
    $designs = $repository->publishedCatalog($market, $limit, $offset);
    echo json_encode([
        'success' => true,
        'market' => $market,
        'count' => count($designs),
        'data' => $designs,
    ], JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE | JSON_THROW_ON_ERROR);
} catch (Throwable $error) {
    // Do not disclose SQL, credentials, or internal exception details to visitors.
    error_log('SUPREME digital catalog request failed: ' . $error->getMessage());
    http_response_code(503);
    echo json_encode(['success' => false, 'error' => 'CATALOG_TEMPORARILY_UNAVAILABLE']);
}
