<?php
declare(strict_types=1);

/**
 * Provider-wide Cohere CORE contract validator.
 * This class validates metadata only; it never calls Cohere or resolves secrets.
 */
final class CohereCoreContract
{
    private const CAPABILITIES = ['classify', 'command', 'embed', 'rerank', 'tokenize'];
    private const SECRET_KEYS = [
        'api_key', 'apikey', 'token', 'access_token', 'refresh_token',
        'secret', 'client_secret', 'password', 'authorization',
        'credential', 'credential_value', 'private_key',
    ];

    public function supports(string $capability): bool
    {
        return in_array(strtolower(trim($capability)), self::CAPABILITIES, true);
    }

    public function validate(array $request): array
    {
        $capability = strtolower(trim((string)($request['capability'] ?? '')));
        if (!$this->supports($capability)) {
            return $this->rejected('Unsupported Cohere capability');
        }
        if ($this->containsSecretField($request)) {
            return $this->rejected('Secret material is not accepted in CORE request metadata');
        }
        if (array_diff(array_keys($request), ['capability', 'inputs', 'model', 'options'])) {
            return $this->rejected('Unsupported request fields');
        }
        if (array_key_exists('options', $request) && (!is_array($request['options']) || count($request['options']) > 0)) {
            return $this->rejected('options are not defined by the current CORE contracts; execution options belong to API/ENGINE');
        }
        if (!isset($request['inputs']) || !is_array($request['inputs'])) {
            return $this->rejected('inputs must be an array');
        }
        if (isset($request['model']) && (!is_string($request['model']) || trim($request['model']) === '')) {
            return $this->rejected('model must be a non-empty string when supplied');
        }

        $inputs = $request['inputs'];
        switch ($capability) {
            case 'classify':
                if (!isset($inputs['inputs']) || !$this->stringList($inputs['inputs'])) {
                    return $this->rejected('classify inputs must contain non-empty strings');
                }
                if (isset($inputs['examples']) && !$this->mappingList($inputs['examples'])) {
                    return $this->rejected('classify examples must be a sequence of mappings');
                }
                if (array_diff(array_keys($inputs), ['inputs', 'examples'])) {
                    return $this->rejected('Unsupported classify input fields');
                }
                break;

            case 'command':
                if (!isset($inputs['message']) || !is_string($inputs['message']) || trim($inputs['message']) === '') {
                    return $this->rejected('message must be a non-empty string');
                }
                if (isset($inputs['chat_history']) && !$this->mappingList($inputs['chat_history'])) {
                    return $this->rejected('chat_history must be a sequence of mappings');
                }
                if (array_diff(array_keys($inputs), ['message', 'chat_history'])) {
                    return $this->rejected('Unsupported command input fields');
                }
                break;

            case 'embed':
                if (!isset($inputs['texts']) || !$this->stringList($inputs['texts'])) {
                    return $this->rejected('texts must contain non-empty strings');
                }
                if (isset($inputs['input_type']) && (!is_string($inputs['input_type']) || trim($inputs['input_type']) === '')) {
                    return $this->rejected('input_type must be a non-empty string when supplied');
                }
                if (array_diff(array_keys($inputs), ['texts', 'input_type'])) {
                    return $this->rejected('Unsupported embed input fields');
                }
                break;

            case 'rerank':
                if (!isset($inputs['query']) || !is_string($inputs['query']) || trim($inputs['query']) === '') {
                    return $this->rejected('query must be a non-empty string');
                }
                if (!isset($inputs['documents']) || !$this->stringList($inputs['documents'])) {
                    return $this->rejected('documents must contain non-empty strings');
                }
                if (isset($inputs['top_n']) && (!is_int($inputs['top_n']) || $inputs['top_n'] < 1)) {
                    return $this->rejected('top_n must be a positive integer');
                }
                if (array_diff(array_keys($inputs), ['query', 'documents', 'top_n'])) {
                    return $this->rejected('Unsupported rerank input fields');
                }
                break;

            case 'tokenize':
                if (!isset($inputs['text']) || !is_string($inputs['text']) || trim($inputs['text']) === '') {
                    return $this->rejected('text must be a non-empty string');
                }
                if (array_diff(array_keys($inputs), ['text'])) {
                    return $this->rejected('Unsupported tokenize input fields');
                }
                break;
        }

        return [
            'ok' => true,
            'status' => 'validated',
            'capability' => $capability,
            'live_provider_calls_enabled' => false,
            'api_call_performed' => false,
        ];
    }

    private function stringList($value): bool
    {
        if (!is_array($value) || count($value) === 0) {
            return false;
        }
        foreach ($value as $item) {
            if (!is_string($item) || trim($item) === '') {
                return false;
            }
        }
        return true;
    }

    private function mappingList($value): bool
    {
        if (!is_array($value)) {
            return false;
        }
        foreach ($value as $item) {
            if (!is_array($item)) {
                return false;
            }
        }
        return true;
    }

    private function containsSecretField($value): bool
    {
        if (!is_array($value)) {
            return false;
        }
        foreach ($value as $key => $nested) {
            if (in_array(strtolower(trim((string)$key)), self::SECRET_KEYS, true)) {
                return true;
            }
            if ($this->containsSecretField($nested)) {
                return true;
            }
        }
        return false;
    }

    private function rejected(string $message): array
    {
        return [
            'ok' => false,
            'status' => 'rejected',
            'errors' => [$message],
            'live_provider_calls_enabled' => false,
            'api_call_performed' => false,
        ];
    }
}
