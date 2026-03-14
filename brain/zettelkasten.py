from pathlib import Path
from brain.llm import chat
import yaml
import re

NOTES = Path("knowledge/notes")
ZETTEL = Path("knowledge/zettelkasten")

ZETTEL.mkdir(exist_ok=True)


def slugify(text):

    import re
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'\s+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text.strip('-')[:80]


def generate_zettels():

    files = list(NOTES.glob("*.md"))

    if not files:
        print("No notes found.")
        return

    texts = []

    for f in files[-5:]:
        with open(f) as file:
            texts.append(file.read())

    context = "\n\n".join(texts)[:6000]

    prompt = f"""
Extract atomic ideas from the notes.

Return ONLY JSON.

Example format:

[
  {{
    "title": "AI chip export controls",
    "content": "Export controls restrict advanced GPUs from China.",
    "links": ["semiconductor geopolitics","Nvidia GPUs"]
  }}
]

Rules:
- one idea per note
- concise explanation
- generate related concepts

Notes:
{context}
"""

    result = chat([
        {"role": "user", "content": prompt}
    ])

    match = re.search(r'```yaml(.*?)```', result, re.S)

    if match:
        yaml_text = match.group(1)
    else:
        yaml_text = result

    try:
        ideas = yaml.safe_load(yaml_text)
    except Exception as e:
        print("YAML parse failed")
        print(result)
        return

    for idea in ideas:

        title = idea["title"]
        content = idea["content"]
        links = idea.get("links", [])

        base = slugify(title)

        filename = base + ".md"

        path = ZETTEL / filename

        i = 1
        while path.exists():
            filename = f"{base}-{i}.md"
            path = ZETTEL / filename
            i += 1

        link_text = "\n".join([f"[[{l}]]" for l in links])
        print(filename)

        note = f"""# {title}

{content}

## Related
{link_text}
"""

        with open(path, "w") as f:
            f.write(note)

        print("Created:", filename)