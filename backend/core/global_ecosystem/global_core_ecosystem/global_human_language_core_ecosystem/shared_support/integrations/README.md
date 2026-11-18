# LANGUAGE PROVIDER INTEGRATIONS BOUNDARY

Provider domains include Alibaba, AWS, Baidu, DeepL, Google, IBM, Microsoft, Naver, OpenAI, Tencent and Yandex. They are cross-cutting metadata providers for human-language and programming-language capabilities.

CORE stores provider identity and capability metadata only. API/ENGINE/adapter layers own OAuth, SDK calls, API requests, rate limits, translation/speech/model jobs and webhook processing. Credentials must remain in an approved external secret store. No live connection is claimed.
