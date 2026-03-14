from brain.embedder import collection


def search(query, k=5):

    results = collection.query(
        query_texts=[query],
        n_results=k
    )

    docs = results["documents"][0]

    return docs