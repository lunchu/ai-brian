import chromadb
from brain.chunker import chunk_text

# persistent database
client = chromadb.PersistentClient(path="vector_db")

collection = client.get_or_create_collection(name="brain")


def add_note(note, note_id):

    chunks = chunk_text(note)

    for i, chunk in enumerate(chunks):

        chunk_id = f"{note_id}_{i}"

        print("Embedding chunk:", chunk_id)

        collection.add(
            documents=[chunk],
            ids=[chunk_id]
        )