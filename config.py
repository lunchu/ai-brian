from dotenv import load_dotenv
import os

load_dotenv()

ANTHROPIC_AUTH_TOKEN = os.getenv("ANTHROPIC_AUTH_TOKEN")
ANTHROPIC_BASE_URL = os.getenv("ANTHROPIC_BASE_URL")

if not ANTHROPIC_AUTH_TOKEN:
    raise ValueError("ANTHROPIC_AUTH_TOKEN not found")

if not ANTHROPIC_BASE_URL:
    raise ValueError("ANTHROPIC_BASE_URL not found")