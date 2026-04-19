import hashlib
import os
from pathlib import Path

DB_ROOT = Path("data/chroma_db")


def _get_source_id(file_path, source_id=None):
    if source_id:
        return source_id

    file_bytes = Path(file_path).read_bytes()
    return hashlib.sha256(file_bytes).hexdigest()


def _get_vectorstore_path(source_id):
    return DB_ROOT / source_id


def _get_collection_name(source_id):
    return f"doc_{source_id[:16]}"


def _has_existing_db(persist_directory):
    return persist_directory.is_dir() and any(persist_directory.iterdir())


def ingest_data(file_path, source_id=None, force_rebuild=False):
    from app.chunker import chunk_documents
    from app.embedding import get_embedding_model
    from app.loaders import load_document
    from app.vectorstore import create_vector_store, load_vector_store

    embeddings = get_embedding_model()
    resolved_source_id = _get_source_id(file_path, source_id)
    persist_directory = _get_vectorstore_path(resolved_source_id)
    collection_name = _get_collection_name(resolved_source_id)

    if _has_existing_db(persist_directory) and not force_rebuild:
        vectorstore = load_vector_store(
            embeddings,
            persist_directory=str(persist_directory),
            collection_name=collection_name,
        )
    else:
        docs = load_document(file_path)
        chunks = chunk_documents(docs)
        persist_directory.mkdir(parents=True, exist_ok=True)
        vectorstore = create_vector_store(
            chunks,
            embeddings,
            persist_directory=str(persist_directory),
            collection_name=collection_name,
        )

    return vectorstore


def get_retriever(vectorstore):
    return vectorstore.as_retriever(search_kwargs={"k": 2})


def answer_query(retriever, query):
    from app.llm import get_llm

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
    return getattr(response, "content", str(response))
