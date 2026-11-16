# GLOBAL AI CORE Architecture

Application authentication -> Global AI Core provider resolution and policy metadata -> provider-specific API adapter -> injected ENGINE execution -> DATABASE/STORAGE persistence -> application response.

Each runtime provider registry entry has a dedicated product Core package. Product packages are thin read-only facades; they do not duplicate SDKs, credentials, transport or inference execution. Runtime provider metadata is the source of truth. Legacy API and adjacent partner aliases remain compatibility-only. Core health reports catalog state, zero verified live connections and zero API calls.
