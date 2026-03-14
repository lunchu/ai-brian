from brain.search import search
import anthropic
from brain.llm import chat

def ask(query):

    results = search(query)
    
    print("Retrieved notes:", results)
    
    context = "\n\n".join(results)
    
    context = context[:6000]
    print("Context:", context)    

    prompt = f"""
Answer the question using the following notes.

Context:
{context}

Question:
{query}
"""

    return chat([
        {"role": "user", "content": prompt}
    ])