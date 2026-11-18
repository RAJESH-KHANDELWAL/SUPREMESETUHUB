# DeepSeek CORE Architecture

The provider root registers four capability packages: chat_completions, responses, search and fetch. Each package follows the ten-folder Google product-Core convention: authentication, capabilities, docs, events, lifecycle, models, schemas, security, services and tests, plus package contracts, service, config, manifest and README.

CORE validates request shape only. It does not resolve credentials, make network requests, retry, persist or execute provider operations. API transport remains in the existing DeepSeek API ecosystem; runtime execution belongs to ENGINE. Existing API catalogs are referenced, not duplicated.
