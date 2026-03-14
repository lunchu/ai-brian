from pathlib import Path
from brain.embedder import add_note

NOTES = Path("knowledge/notes")

for file in NOTES.glob("*.md"):

    with open(file) as f:
        text = f.read()

    add_note(text, file.name)

    print("Embedded:", file.name)