/* SUPREME PRINT ON DEMAND — draft catalog, quote and design-brief UI */
(() => {
    const API_BASE = window.SUPREME_API_BASE ||
        (window.location.hostname.endsWith("github.io")
            ? "https://api.rajeshkhandelwalofficial.com"
            : window.location.origin);
    const tokenKey = "main_base_foundation_token";
    const byId = (id) => document.getElementById(id);
    const market = byId("podMarket");
    const product = byId("podProduct");
    const tier = byId("podTier");
    const demand = byId("podDemand");
    const quantity = byId("podQuantity");
    const prompt = byId("podPrompt");
    const notes = byId("podNotes");
    const status = byId("podStatus");
    const productGrid = byId("podProductGrid");
    const quoteButton = byId("podQuoteButton");
    const saveButton = byId("podSaveButton");
    let lastQuote = null;

    function token() {
        return sessionStorage.getItem(tokenKey) || "";
    }

    function money(value, currency) {
        return new Intl.NumberFormat(currency === "INR" ? "en-IN" : "en-US", {
            style: "currency", currency, maximumFractionDigits: 0
        }).format(value);
    }

    function showStatus(message) {
        status.textContent = message;
    }

    async function api(path, options = {}) {
        const authToken = token();
        if (!authToken) {
            throw new Error("Please SIGN IN first, then return to SUPREME PRINT ON DEMAND.");
        }
        const response = await fetch(API_BASE + path, {
            ...options,
            headers: {
                "Content-Type": "application/json",
                "Accept": "application/json",
                "Authorization": "Bearer " + authToken,
                ...(options.headers || {})
            }
        });
        const data = await response.json().catch(() => ({}));
        if (!response.ok) {
            throw new Error(data.detail || data.message || "POD API request failed (" + response.status + ").");
        }
        return data;
    }

    function currentRequest() {
        return {
            product_sku: product.value,
            market: market.value,
            tier: tier.value,
            demand_score: Number(demand.value),
            quantity: Number(quantity.value)
        };
    }

    async function loadCatalog() {
        lastQuote = null;
        product.innerHTML = "";
        product.add(new Option("Loading catalog…", ""));
        productGrid.replaceChildren();
        try {
            const result = await api("/api/v1/print-on-demand/catalog?market=" + encodeURIComponent(market.value));
            const data = result.data;
            product.replaceChildren();
            data.products.forEach((item) => {
                product.add(new Option(item.name + " · " + item.sku, item.sku));
                const card = document.createElement("article");
                card.className = "pod-product";
                const title = document.createElement("strong");
                title.textContent = item.name;
                const category = document.createElement("small");
                category.textContent = item.category + " · " + item.description;
                const standard = document.createElement("div");
                standard.className = "pod-price";
                standard.textContent = "Standard from " + money(item.standard_from, data.currency);
                const premium = document.createElement("small");
                premium.textContent = "Premium from " + money(item.premium_from, data.currency);
                card.append(title, category, standard, premium);
                productGrid.append(card);
            });
            if (data.design_starters) {
                byId("podDesignStarters").querySelectorAll("[data-pod-prompt]").forEach((button) => {
                    button.addEventListener("click", () => { prompt.value = button.dataset.podPrompt; });
                });
            }
            showStatus("Catalog loaded for " + data.market + ". Select a product and calculate a draft quote. " + data.pricing_notice);
        } catch (error) {
            product.replaceChildren(new Option("Sign in to load catalog", ""));
            showStatus(error.message);
        }
    }

    async function calculateQuote() {
        quoteButton.disabled = true;
        try {
            const result = await api("/api/v1/print-on-demand/quote", {
                method: "POST",
                body: JSON.stringify(currentRequest())
            });
            lastQuote = result.data;
            const q = lastQuote;
            showStatus(
                "DRAFT PRICE · " + q.tier + " · " + q.market + "\n" +
                "Unit price: " + money(q.unit_price, q.currency) + "\n" +
                "Quantity: " + q.quantity + "\n" +
                "Estimated total: " + money(q.total_price, q.currency) + "\n" +
                "Estimated gross margin: " + Math.round(q.estimated_gross_margin * 100) + "% (before excluded costs)\n\n" +
                q.notice + " Excludes " + q.excluded_costs.join(", ") + "."
            );
        } catch (error) {
            lastQuote = null;
            showStatus(error.message);
        } finally {
            quoteButton.disabled = false;
        }
    }

    async function saveBrief() {
        if (!prompt.value.trim()) {
            showStatus("Please describe the original graphic before saving the design brief.");
            prompt.focus();
            return;
        }
        saveButton.disabled = true;
        try {
            const result = await api("/api/v1/print-on-demand/design-briefs", {
                method: "POST",
                body: JSON.stringify({ ...currentRequest(), design_prompt: prompt.value.trim(), notes: notes.value.trim() })
            });
            const saved = result.data;
            const q = saved.quote;
            showStatus(
                "DESIGN BRIEF SAVED · " + saved.brief_id + "\n" +
                "Status: " + saved.status + "\n" +
                "Draft total: " + money(q.total_price, q.currency) + "\n\n" +
                saved.message + "\n\n" +
                "Next stage: connect an approved print provider, verify real production/shipping costs, and configure checkout before taking payment."
            );
        } catch (error) {
            showStatus(error.message);
        } finally {
            saveButton.disabled = false;
        }
    }

    demand.addEventListener("input", () => {
        byId("podDemandValue").textContent = demand.value;
        lastQuote = null;
    });
    [market, product, tier, quantity].forEach((element) => {
        element.addEventListener("change", () => { lastQuote = null; });
    });
    market.addEventListener("change", loadCatalog);
    quoteButton.addEventListener("click", calculateQuote);
    saveButton.addEventListener("click", saveBrief);

    if (!token()) {
        showStatus("SIGN IN is required to access your catalog, calculate pricing or save a private design brief.");
    }
    loadCatalog();
})();
