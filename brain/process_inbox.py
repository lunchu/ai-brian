from pathlib import Path
from brain.processor import summarize
from brain.embedder import add_note

INBOX = Path("knowledge/inbox")
NOTES = Path("knowledge/notes")


def process_inbox():

    for file in INBOX.glob("*.txt"):

        with open(file) as f:
            text = f.read()

        result = summarize(text)

        final_note = f"""
# AI Summary

{result}

---

# Original Source

{text[:5000]}
"""
		
        note_path = NOTES / file.name.replace(".txt", ".md")

        with open(note_path, "w") as f:
            f.write(final_note)

        add_note(final_note, file.name)

        print("Processed:", file)

        file.unlink()