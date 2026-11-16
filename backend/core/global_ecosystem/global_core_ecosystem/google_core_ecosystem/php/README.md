# Google Core PHP Interoperability Contract

`GoogleCoreContract.php` is a PHP 8+ value/validation boundary for JSON-compatible responses emitted by the Python Google Core layer.

- Validates required Core result fields and their primitive types.
- Parses and serializes JSON without making network requests.
- Recursively removes token, secret, password and authorization fields.
- Does not implement Google OAuth, API transport, storage, or live provider access.
- The calling PHP application remains responsible for authenticated transport to a separately deployed Core API endpoint.

This is a language interoperability contract, not a second Google integration stack.
