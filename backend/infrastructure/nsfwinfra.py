"""NSFWInfra API connector for SUPREMESETUHUB."""

import os

import httpx


API_URL = "https://api.nsfwinfra.com/v1/images/generate"


async def generate_image(prompt: str) -> dict:
    api_key = os.getenv("NSFWINFRA_API_KEY")

    if not api_key:
        raise RuntimeError("NSFWINFRA_API_KEY is not configured")

    if not prompt.strip():
        raise ValueError("Prompt cannot be empty")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    async with httpx.AsyncClient(timeout=60.0) as client:
        response = await client.post(
            API_URL,
            headers=headers,
            json={"prompt": prompt.strip()},
        )
        response.raise_for_status()
        return response.json()
