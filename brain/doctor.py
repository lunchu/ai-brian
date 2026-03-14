from pathlib import Path
from brain.embedder import collection
from brain.search import search


def run_doctor():

    print("\n=== AI Brain Diagnostics ===\n")

    # check notes
    notes_path = Path("knowledge/notes")

    if not notes_path.exists():
        print("❌ knowledge/notes folder missing")
        return

    notes = list(notes_path.glob("*.md"))

    print("Notes count:", len(notes))

    if not notes:
        print("⚠️ No notes found. Run: aibrain process")

    # check vector DB
    try:
        count = collection.count()
        print("Vector DB documents:", count)

        if count == 0:
            print("⚠️ Vector DB empty. Need embedding.")

    except Exception as e:
        print("❌ Vector DB error:", e)

    # test search
    try:
        results = search("test")

        print("Search test results:", len(results))

        if not results:
            print("⚠️ Search returned nothing")

    except Exception as e:
        print("❌ Search failed:", e)

    print("\nDiagnostics complete.\n")