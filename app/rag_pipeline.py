import os
from app.loaders import load_document
from app.chunker import chunk_documents
from app.embedding import get_embedding_model
from app.vectorstore import create_vector_store, load_vector_store
from app.llm import get_llm

DB_PATH = "data/chroma_db"

def ingest_data(file_path):
    embeddings = get_embedding_model()

    if os.path.exists(DB_PATH) and os.listdir(DB_PATH):
        vectorstore = load_vector_store(embeddings)
    else:
        docs = load_document(file_path)
        chunks = chunk_documents(docs)
        vectorstore = create_vector_store(chunks, embeddings)

    return vectorstore

def get_retriever(vectorstore):
    return vectorstore.as_retriever(search_kwargs={"k": 2})

def answer_query(retriever, query):
    docs = retriever.invoke(query)
    context = "\n\n".join([doc.page_content[:500] for doc in docs])

    prompt = f"""
You are an AI assistant.

Answer the user's question only from the context below.
Give a short, direct answer.
If the answer is not found, say:
Information not available in the document.

Context:
{context}

Question:
{query}

Answer:
"""

    llm = get_llm()
    response = llm.invoke(prompt)
    return response.content