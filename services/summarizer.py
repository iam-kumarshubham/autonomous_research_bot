import os
import httpx
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

async def summarize_text(text: str) -> str:
    """
    Summarizes a given text using OpenAI's GPT API.
    """
    prompt = f"Summarize the following article in 5-7 bullet points:\n\n{text}"

    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }

    body = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3,
        "max_tokens": 500
    }

    async with httpx.AsyncClient() as client:
        response = await client.post("https://api.openai.com/v1/chat/completions", json=body, headers=headers)
        result = response.json()
        
        if "choices" in result:
            return result["choices"][0]["message"]["content"].strip()
        else:
            raise Exception(f"Failed to summarize: {result}")
