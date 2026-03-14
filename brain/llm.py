import os
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("ANTHROPIC_BASE_URL")
TOKEN = os.getenv("ANTHROPIC_AUTH_TOKEN")


def chat(messages, model="claude-4.5-sonnet", max_tokens=1000):

    url = f"{BASE_URL}/messages"

    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": model,
        "max_tokens": max_tokens,
        "messages": messages
    }

    r = requests.post(url, headers=headers, json=payload)

    if r.status_code != 200:
        raise Exception(f"API Error: {r.text}")

    data = r.json()

    return data["content"][0]["text"]