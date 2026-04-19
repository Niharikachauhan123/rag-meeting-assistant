from langchain_community.vectorstores import Chroma

def create_vector_store(chunks, embeddings):
    return Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="data/chroma_db"
    )

def load_vector_store(embeddings):
    return Chroma(
        persist_directory="data/chroma_db",
        embedding_function=embeddings
    )