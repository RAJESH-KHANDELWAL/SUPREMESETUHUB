"""Registry of digital platforms represented in the Global Platforms Ecosystem."""

PLATFORMS = [
    {"name": "Google Search", "category": "Search", "website": "https://www.google.com"},
    {"name": "YouTube", "category": "Video", "website": "https://www.youtube.com"},
    {"name": "Google Cloud", "category": "Cloud", "website": "https://cloud.google.com"},
    {"name": "Microsoft Azure", "category": "Cloud", "website": "https://azure.microsoft.com"},
    {"name": "Amazon Web Services (AWS)", "category": "Cloud", "website": "https://aws.amazon.com"},
    {"name": "GitHub", "category": "Developer platform", "website": "https://github.com"},
    {"name": "GitLab", "category": "Developer platform", "website": "https://gitlab.com"},
    {"name": "Bitbucket", "category": "Developer platform", "website": "https://bitbucket.org"},
    {"name": "WordPress", "category": "Website publishing", "website": "https://wordpress.org"},
    {"name": "Blogger", "category": "Blog publishing", "website": "https://www.blogger.com"},
    {"name": "Instagram", "category": "Social media", "website": "https://www.instagram.com"},
    {"name": "Facebook", "category": "Social media", "website": "https://www.facebook.com"},
    {"name": "LinkedIn", "category": "Professional networking", "website": "https://www.linkedin.com"},
    {"name": "X", "category": "Social media", "website": "https://x.com"},
    {"name": "Threads", "category": "Social media", "website": "https://www.threads.net"},
    {"name": "Reddit", "category": "Community platform", "website": "https://www.reddit.com"},
    {"name": "WhatsApp", "category": "Messaging", "website": "https://www.whatsapp.com"},
    {"name": "Telegram", "category": "Messaging", "website": "https://telegram.org"},
    {"name": "Slack", "category": "Team communication", "website": "https://slack.com"},
    {"name": "Discord", "category": "Community communication", "website": "https://discord.com"},
    {"name": "Shopify", "category": "E-commerce", "website": "https://www.shopify.com"},
    {"name": "WooCommerce", "category": "E-commerce", "website": "https://woocommerce.com"},
    {"name": "Stripe", "category": "Payments", "website": "https://stripe.com"},
    {"name": "PayPal", "category": "Payments", "website": "https://www.paypal.com"},
    {"name": "OpenAI", "category": "AI platform", "website": "https://openai.com"},
    {"name": "Hugging Face", "category": "AI platform", "website": "https://huggingface.co"},
    {"name": "Vercel", "category": "Deployment", "website": "https://vercel.com"},
    {"name": "Netlify", "category": "Deployment", "website": "https://www.netlify.com"},
    {"name": "Render", "category": "Cloud hosting", "website": "https://render.com"},
    {"name": "Hostinger", "category": "Web hosting", "website": "https://www.hostinger.com"},
    {"name": "Cloudflare", "category": "Network and security", "website": "https://www.cloudflare.com"},
    {"name": "Firebase", "category": "Application backend", "website": "https://firebase.google.com"},
    {"name": "Supabase", "category": "Application backend", "website": "https://supabase.com"},
    {"name": "PostgreSQL", "category": "Database", "website": "https://www.postgresql.org"},
    {"name": "MongoDB", "category": "Database", "website": "https://www.mongodb.com"},
    {"name": "Docker", "category": "Developer tools", "website": "https://www.docker.com"},
    {"name": "Kubernetes", "category": "Infrastructure", "website": "https://kubernetes.io"},
]


def get_platforms():
    """Return the platform registry."""
    return list(PLATFORMS)
