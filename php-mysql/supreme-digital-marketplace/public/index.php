<?php
declare(strict_types=1);

require_once dirname(__DIR__) . '/src/Database.php';
require_once dirname(__DIR__) . '/src/DigitalDesignRepository.php';

function e(string $value): string
{
    return htmlspecialchars($value, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8');
}

$market = strtoupper(trim((string) ($_GET['market'] ?? 'IN')));
if (!in_array($market, ['IN', 'GLOBAL'], true)) {
    $market = 'IN';
}
$currencySymbol = $market === 'IN' ? '₹' : '$';
$designs = [];
$catalogAvailable = true;

try {
    $designs = (new DigitalDesignRepository(Database::connection()))->publishedCatalog($market, 48, 0);
} catch (Throwable $error) {
    error_log('SUPREME storefront could not load catalog: ' . $error->getMessage());
    $catalogAvailable = false;
}
?>
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="Discover original AI-assisted digital artwork, posters, wallpapers and creative downloads from SUPREME.">
    <title>SUPREME DIGITAL DESIGN MARKETPLACE</title>
    <style>
        :root{color-scheme:dark;--bg:#08101f;--panel:#111c31;--line:#293954;--text:#f5f7ff;--muted:#aab7ce;--blue:#79a9ff;--gold:#f3d18a}
        *{box-sizing:border-box}body{margin:0;background:radial-gradient(ellipse at top,#172b4a 0,#08101f 55%);color:var(--text);font:16px/1.5 system-ui,-apple-system,Segoe UI,sans-serif}
        a{color:inherit}.wrap{width:min(1180px,calc(100% - 32px));margin:auto}.top{padding:28px 0;border-bottom:1px solid var(--line)}
        .brand{font-weight:900;letter-spacing:.14em}.hero{padding:54px 0 32px}.eyebrow{color:var(--gold);font-size:.78rem;font-weight:800;letter-spacing:.16em}
        h1{max-width:780px;font-size:clamp(2.1rem,5vw,4.5rem);line-height:1.04;margin:12px 0}
        .lead{max-width:680px;color:var(--muted);font-size:1.08rem}.toolbar{display:flex;flex-wrap:wrap;gap:10px;align-items:center;justify-content:space-between;margin:24px 0}
        .markets{display:flex;gap:8px}.pill{display:inline-block;padding:9px 14px;border:1px solid var(--line);border-radius:999px;text-decoration:none}
        .pill.active{background:var(--blue);border-color:var(--blue);color:#07101f;font-weight:800}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:18px;padding-bottom:56px}
        .card{background:linear-gradient(160deg,#17243b,#0e1729);border:1px solid var(--line);border-radius:18px;overflow:hidden}
        .preview{aspect-ratio:4/3;background:#1b2b45;display:grid;place-items:center;overflow:hidden}.preview img{width:100%;height:100%;object-fit:cover}
        .fallback{padding:18px;text-align:center;color:var(--muted);font-weight:800;letter-spacing:.08em}.body{padding:17px}.category{font-size:.74rem;color:var(--gold);font-weight:800;text-transform:uppercase;letter-spacing:.1em}
        h2{font-size:1.08rem;line-height:1.25;margin:7px 0}.desc{min-height:48px;color:var(--muted);font-size:.9rem}.price{font-size:1.35rem;font-weight:900;margin:14px 0}
        .note{color:var(--muted);font-size:.85rem}.empty{padding:24px;border:1px dashed var(--line);border-radius:16px;color:var(--muted);grid-column:1/-1}
        footer{border-top:1px solid var(--line);padding:24px 0;color:var(--muted);font-size:.85rem}
    </style>
</head>
<body>
<header class="top"><div class="wrap brand">👑 SUPREME DIGITAL DESIGN MARKETPLACE</div></header>
<main class="wrap">
    <section class="hero">
        <div class="eyebrow">ORIGINAL DIGITAL ART · BHARAT + GLOBAL</div>
        <h1>Discover digital designs worth keeping.</h1>
        <p class="lead">Explore original artwork, posters, wallpapers and creative downloads. Buy digitally and download when your order is securely confirmed. No physical products, printing or shipping.</p>
        <div class="toolbar">
            <strong><?= count($designs) ?> published designs</strong>
            <nav class="markets" aria-label="Choose market">
                <a class="pill<?= $market === 'IN' ? ' active' : '' ?>" href="?market=IN">Bharat · INR</a>
                <a class="pill<?= $market === 'GLOBAL' ? ' active' : '' ?>" href="?market=GLOBAL">Global · USD</a>
            </nav>
        </div>
    </section>
    <section class="grid" aria-label="Digital design catalog">
        <?php if (!$catalogAvailable): ?>
            <div class="empty"><strong>Catalog setup pending.</strong><br>Connect the PHP runtime to the configured MySQL database and import <code>database/schema.sql</code>. No credentials are shown here.</div>
        <?php elseif ($designs === []): ?>
            <div class="empty"><strong>New designs are coming soon.</strong><br>Only reviewed and published designs appear here. Draft designs stay hidden until approved.</div>
        <?php else: ?>
            <?php foreach ($designs as $design): ?>
                <article class="card">
                    <div class="preview">
                        <?php if (!empty($design['preview_path'])): ?>
                            <img src="<?= e((string) $design['preview_path']) ?>" alt="<?= e((string) $design['title']) ?>" loading="lazy">
                        <?php else: ?>
                            <div class="fallback">SUPREME ORIGINAL ART</div>
                        <?php endif; ?>
                    </div>
                    <div class="body">
                        <div class="category"><?= e((string) $design['category']) ?></div>
                        <h2><?= e((string) $design['title']) ?></h2>
                        <p class="desc"><?= e((string) $design['description']) ?></p>
                        <div class="price"><?= e($currencySymbol) ?><?= e(number_format(((int) $design['price_minor']) / 100, 2, '.', ',')) ?></div>
                        <div class="note"><?= e((string) $design['license_label']) ?> · Digital product</div>
                    </div>
                </article>
            <?php endforeach; ?>
        <?php endif; ?>
    </section>
</main>
<footer><div class="wrap">SUPREME DIGITAL DESIGN MARKETPLACE · Original digital products only · Secure checkout/download integration required before live sales.</div></footer>
</body>
</html>
