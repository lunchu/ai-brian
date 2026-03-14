from brain.llm import chat

def summarize(text):

    prompt = f"""
Summarize this note.

{text}
"""

    return chat([
        {"role": "user", "content": prompt}
    ])