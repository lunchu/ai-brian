from pathlib import Path
from brain.llm import chat

NOTES = Path("knowledge/notes")


def generate_timeline():

    files = sorted(NOTES.glob("*.md"), key=lambda f: f.stat().st_mtime, reverse=True)

    if not files:
        print("No notes found.")
        return

    texts = []

    for f in files[:10]:  # 最近 10 筆
        with open(f) as file:
            texts.append(file.read())

    context = "\n\n".join(texts)[:6000]

    prompt = f"""
Review my recent knowledge notes.

Generate a timeline summary:

1. What I learned recently
2. Recurring themes
3. Interesting insights
4. Potential ideas worth exploring

Notes:
{context}
"""

    result = chat([
        {"role": "user", "content": prompt}
    ])

    print("\n=== AI Knowledge Timeline ===\n")
    print(result)