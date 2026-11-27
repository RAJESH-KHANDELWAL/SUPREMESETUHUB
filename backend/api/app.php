<?php
declare(strict_types=1);

/**
 * SUPREMESETUHUB PHP API application.
 *
 * This is an independent PHP entry point. Python remains the FastAPI service
 * in backend/api/app.py. Requests under /api/ are forwarded to that service
 * over HTTP; PHP owns its own /health endpoint.
 *
 * Configure SUPREMESETUHUB_PYTHON_API_BASE_URL in the server environment.
 * Example for a local FastAPI process: http://127.0.0.1:8000
 * Never commit credentials or a production host URL here.
 */

const SUPREME_PHP_APP_NAME = 'SUPREMESETUHUB PHP API';
const SUPREME_PHP_APP_VERSION = '1.0.0';

function supreme_php_json_response(array $payload, int $status = 200): never
{
    http_response_code($status);
    header('Content-Type: application/json; charset=utf-8');
    header('Cache-Control: no-store');
    echo json_encode($payload, JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE);
    exit;
}

function supreme_python_api_base_url(): ?string
{
    $value = getenv('SUPREMESETUHUB_PYTHON_API_BASE_URL');
    if ($value === false || trim($value) === '') {
        return null;
    }

    $value = rtrim(trim($value), '/');
    $parts = parse_url($value);
    if (
        $parts === false
        || !isset($parts['scheme'], $parts['host'])
        || !in_array(strtolower($parts['scheme']), ['http', 'https'], true)
        || isset($parts['user'])
        || isset($parts['pass'])
        || isset($parts['query'])
        || isset($parts['fragment'])
    ) {
        throw new RuntimeException('SUPREMESETUHUB_PYTHON_API_BASE_URL must be a valid HTTP(S) base URL without credentials, query, or fragment.');
    }

    return $value;
}

function supreme_php_forward_to_python(string $baseUrl, string $requestPath): never
{
    if (!function_exists('curl_init')) {
        supreme_php_json_response([
            'success' => false,
            'error' => 'PHP cURL extension is required for Python API connectivity.',
        ], 503);
    }

    $method = strtoupper($_SERVER['REQUEST_METHOD'] ?? 'GET');
    $allowedMethods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'HEAD'];
    if (!in_array($method, $allowedMethods, true)) {
        header('Allow: ' . implode(', ', $allowedMethods));
        supreme_php_json_response(['success' => false, 'error' => 'HTTP method not allowed.'], 405);
    }

    $targetUrl = $baseUrl . $requestPath;
    $query = $_SERVER['QUERY_STRING'] ?? '';
    if ($query !== '') {
        $targetUrl .= '?' . $query;
    }

    $forwardHeaders = [];
    foreach (['HTTP_ACCEPT' => 'Accept', 'CONTENT_TYPE' => 'Content-Type', 'HTTP_AUTHORIZATION' => 'Authorization', 'HTTP_X_REQUEST_ID' => 'X-Request-ID'] as $serverKey => $headerName) {
        if (isset($_SERVER[$serverKey]) && $_SERVER[$serverKey] !== '') {
            $forwardHeaders[] = $headerName . ': ' . $_SERVER[$serverKey];
        }
    }

    $handle = curl_init($targetUrl);
    if ($handle === false) {
        supreme_php_json_response(['success' => false, 'error' => 'Could not initialize the Python API connection.'], 502);
    }

    $options = [
        CURLOPT_CUSTOMREQUEST => $method,
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_HEADER => false,
        CURLOPT_FOLLOWLOCATION => false,
        CURLOPT_CONNECTTIMEOUT => 5,
        CURLOPT_TIMEOUT => 30,
        CURLOPT_HTTPHEADER => $forwardHeaders,
        CURLOPT_HEADERFUNCTION => static function ($curl, string $headerLine): int {
            $length = strlen($headerLine);
            $parts = explode(':', $headerLine, 2);
            if (count($parts) === 2 && strtolower(trim($parts[0])) === 'content-type') {
                header('Content-Type: ' . trim($parts[1]));
            }
            return $length;
        },
    ];

    if (!in_array($method, ['GET', 'HEAD'], true)) {
        $body = file_get_contents('php://input');
        $options[CURLOPT_POSTFIELDS] = $body === false ? '' : $body;
    }

    curl_setopt_array($handle, $options);
    $responseBody = curl_exec($handle);
    $curlError = curl_error($handle);
    $statusCode = (int) curl_getinfo($handle, CURLINFO_RESPONSE_CODE);
    curl_close($handle);

    if ($responseBody === false) {
        supreme_php_json_response([
            'success' => false,
            'error' => 'Python API service is unavailable.',
            'detail' => $curlError,
        ], 502);
    }

    http_response_code($statusCode > 0 ? $statusCode : 502);
    header('Cache-Control: no-store');
    if ($method !== 'HEAD') {
        echo $responseBody;
    }
    exit;
}

$requestUri = $_SERVER['REQUEST_URI'] ?? '/';
$requestPath = parse_url($requestUri, PHP_URL_PATH);
$requestPath = is_string($requestPath) && $requestPath !== '' ? $requestPath : '/';

if ($requestPath === '/health' || $requestPath === '/health/') {
    supreme_php_json_response([
        'success' => true,
        'application' => SUPREME_PHP_APP_NAME,
        'version' => SUPREME_PHP_APP_VERSION,
        'runtime' => 'PHP',
        'python_api_configured' => (getenv('SUPREMESETUHUB_PYTHON_API_BASE_URL') !== false && trim((string) getenv('SUPREMESETUHUB_PYTHON_API_BASE_URL')) !== ''),
    ]);
}

if ($requestPath === '/' || $requestPath === '/index.php') {
    supreme_php_json_response([
        'success' => true,
        'application' => SUPREME_PHP_APP_NAME,
        'version' => SUPREME_PHP_APP_VERSION,
        'status' => 'READY',
        'integration' => 'Independent PHP application connected to the Python FastAPI application through HTTP.',
        'health_endpoint' => '/health',
        'python_api_route_prefix' => '/api/',
    ]);
}

if (!str_starts_with($requestPath, '/api/')) {
    supreme_php_json_response([
        'success' => false,
        'error' => 'Route not found.',
        'allowed_route_prefix' => '/api/',
    ], 404);
}

try {
    $pythonApiBaseUrl = supreme_python_api_base_url();
    if ($pythonApiBaseUrl === null) {
        supreme_php_json_response([
            'success' => false,
            'error' => 'Python API connection is not configured.',
            'required_environment_variable' => 'SUPREMESETUHUB_PYTHON_API_BASE_URL',
        ], 503);
    }

    supreme_php_forward_to_python($pythonApiBaseUrl, $requestPath);
} catch (RuntimeException $exception) {
    supreme_php_json_response(['success' => false, 'error' => $exception->getMessage()], 500);
}
