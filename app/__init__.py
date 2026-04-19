def ingest_data(*args, **kwargs):
    from .rag_pipeline import ingest_data as _ingest_data

    return _ingest_data(*args, **kwargs)


def get_retriever(*args, **kwargs):
    from .rag_pipeline import get_retriever as _get_retriever

    return _get_retriever(*args, **kwargs)


def answer_query(*args, **kwargs):
    from .rag_pipeline import answer_query as _answer_query

    return _answer_query(*args, **kwargs)


__all__ = ["ingest_data", "get_retriever", "answer_query"]
