<?php
/**
 * SUPREME ECOSYSTEM — HOME renderer.
 *
 * Uses the canonical HOME HTML and CSS files in:
 *   frontend/supreme/supreme-ecosystem/
 *
 * The markup and stylesheet are loaded directly into the page so it can
 * grow naturally with its content and does not create a nested scroll area.
 * The source HTML/CSS files remain unchanged.
 */

declare(strict_types=1);

$projectRoot = dirname(__DIR__, 2);
$htmlPath = $projectRoot . '/frontend/supreme/supreme-ecosystem/home-html.html';
$cssPath  = $projectRoot . '/frontend/supreme/supreme-ecosystem/home-css.css';

if (!is_file($htmlPath) || !is_readable($htmlPath) || !is_file($cssPath) || !is_readable($cssPath)) {
    http_response_code(500);
    header('Content-Type: text/plain; charset=UTF-8');
    echo 'SUPREME ECOSYSTEM HOME assets could not be loaded.';
    exit;
}

$html = file_get_contents($htmlPath);
$css  = file_get_contents($cssPath);

if ($html === false || $css === false) {
    http_response_code(500);
    header('Content-Type: text/plain; charset=UTF-8');
    echo 'SUPREME ECOSYSTEM HOME assets could not be read.';
    exit;
}

header('Content-Type: text/html; charset=UTF-8');
?>
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>SUPREME ECOSYSTEM | DR RAJESH KHANDELWAL IBC</title>
    <style>
<?= $css ?>
    </style>
</head>
<body>
<?= $html ?>
</body>
</html>
