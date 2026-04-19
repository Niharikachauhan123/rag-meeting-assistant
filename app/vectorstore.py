from langchain_community.vectorstores import Chroma


def create_vector_store(chunks, embeddings, persist_directory, collection_name):
    return Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=persist_directory,
        collection_name=collection_name,
    )


def load_vector_store(embeddings, persist_directory, collection_name):
    return Chroma(
        persist_directory=persist_directory,
        embedding_function=embeddings,
        collection_name=collection_name,
    )
