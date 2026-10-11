"""Registry of companies represented in the Global Companies Ecosystem."""

COMPANIES = [
    {"name": "Google", "category": "Technology", "website": "https://www.google.com"},
    {"name": "Apple", "category": "Consumer technology", "website": "https://www.apple.com"},
    {"name": "Amazon", "category": "E-commerce and technology", "website": "https://www.amazon.com"},
    {"name": "Amazon Web Services (AWS)", "category": "Cloud computing", "website": "https://aws.amazon.com"},
    {"name": "Microsoft", "category": "Software and cloud", "website": "https://www.microsoft.com"},
    {"name": "Meta", "category": "Social technology", "website": "https://about.meta.com"},
    {"name": "NVIDIA", "category": "Computing and AI", "website": "https://www.nvidia.com"},
    {"name": "OpenAI", "category": "Artificial intelligence", "website": "https://openai.com"},
    {"name": "IBM", "category": "Enterprise technology", "website": "https://www.ibm.com"},
    {"name": "Oracle", "category": "Database and enterprise software", "website": "https://www.oracle.com"},
    {"name": "Salesforce", "category": "CRM and cloud software", "website": "https://www.salesforce.com"},
    {"name": "Adobe", "category": "Creative and marketing software", "website": "https://www.adobe.com"},
    {"name": "Intel", "category": "Semiconductors", "website": "https://www.intel.com"},
    {"name": "AMD", "category": "Semiconductors", "website": "https://www.amd.com"},
    {"name": "Samsung", "category": "Consumer electronics", "website": "https://www.samsung.com"},
    {"name": "Sony", "category": "Electronics and entertainment", "website": "https://www.sony.com"},
    {"name": "Tesla", "category": "Electric vehicles and energy", "website": "https://www.tesla.com"},
    {"name": "Netflix", "category": "Streaming entertainment", "website": "https://www.netflix.com"},
    {"name": "Uber", "category": "Mobility platform", "website": "https://www.uber.com"},
    {"name": "Airbnb", "category": "Travel marketplace", "website": "https://www.airbnb.com"},
    {"name": "Shopify", "category": "E-commerce software", "website": "https://www.shopify.com"},
    {"name": "Stripe", "category": "Payments technology", "website": "https://stripe.com"},
    {"name": "PayPal", "category": "Digital payments", "website": "https://www.paypal.com"},
    {"name": "Visa", "category": "Payments network", "website": "https://www.visa.com"},
    {"name": "Mastercard", "category": "Payments network", "website": "https://www.mastercard.com"},
    {"name": "Reliance Industries", "category": "Indian conglomerate", "website": "https://www.ril.com"},
    {"name": "Tata Consultancy Services (TCS)", "category": "IT services", "website": "https://www.tcs.com"},
    {"name": "Infosys", "category": "IT services", "website": "https://www.infosys.com"},
    {"name": "Wipro", "category": "IT services", "website": "https://www.wipro.com"},
    {"name": "HCLTech", "category": "IT services", "website": "https://www.hcltech.com"},
    {"name": "Tata Motors", "category": "Automotive", "website": "https://www.tatamotors.com"},
]


def get_companies():
    """Return the company registry."""
    return list(COMPANIES)
