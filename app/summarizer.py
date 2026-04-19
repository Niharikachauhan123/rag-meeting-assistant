def generate_summary(retriever):
    from app.llm import get_llm

    docs = retriever.invoke("Summarize this meeting or document.")
    context = "\n\n".join([doc.page_content[:500] for doc in docs])

    prompt = f"""
You are an AI Meeting Assistant.

Based only on the context below, generate the output in this exact format:

Summary:
- Write a short summary

Key Points:
- Point 1
- Point 2

Action Items:
- Item 1
- Item 2

Decisions Made:
- Decision 1
- Decision 2

If any section has no information, write "Not mentioned".

Context:
{context}

Answer:
"""

    llm = get_llm()
    response = llm.invoke(prompt)
    return getattr(response, "content", str(response))
