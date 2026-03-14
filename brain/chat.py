from brain.search import search
from brain.llm import chat


def interactive_chat():

    print("\nAI Brain Chat (type 'exit' to quit)\n")

    history = []

    while True:

        query = input("You: ")

        if query.lower() in ["exit", "quit"]:
            break

        # search knowledge base
        results = search(query)

        context = "\n\n".join(results)[:6000]

        prompt = f"""
You are answering questions using my knowledge base.

Knowledge:
{context}

Conversation:
{history}

User question:
{query}
"""

        answer = chat([
            {"role": "user", "content": prompt}
        ])

        print("\nAI:", answer, "\n")

        # save history
        history.append(f"User: {query}")
        history.append(f"AI: {answer}")
        history = history[-10:]