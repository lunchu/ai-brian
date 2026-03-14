from pathlib import Path
from brain.llm import chat

ZETTEL = Path("knowledge/zettelkasten")


def weave_notes():

    files = list(ZETTEL.glob("*.md"))

    if len(files) < 2:
        print("Not enough zettels.")
        return

    texts = []

    for f in files[:20]:  # 限制 token
        with open(f) as file:
            texts.append(file.read())

    context = "\n\n".join(texts)[:6000]

    prompt = f"""
Analyze these Zettelkasten notes.

Find relationships between ideas.

Return suggestions like:

Concept A -> Concept B : explanation

Notes:
{context}
"""

    result = chat([
        {"role": "user", "content": prompt}
    ])

    print("\n=== Knowledge Weave ===\n")
    print(result)