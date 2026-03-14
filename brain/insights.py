from pathlib import Path
from brain.llm import chat

NOTES = Path("knowledge/notes")

def generate_insights():

    texts = []

    for f in NOTES.glob("*.md"):
        with open(f) as file:
            texts.append(file.read())

    context = "\n\n".join(texts)[:6000]

    prompt = f"""
Analyze my knowledge notes.

Identify:

1. recurring themes
2. interesting connections
3. potential research ideas

Notes:
{context}
"""

    result = chat([
        {"role": "user", "content": prompt}
    ])

    print("\n=== AI INSIGHTS ===\n")
    print(result)