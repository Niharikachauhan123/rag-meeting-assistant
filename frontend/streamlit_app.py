import sys
import os
import hashlib

os.environ["STREAMLIT_SERVER_FILE_WATCHER_TYPE"] = "none"

try:
    import torch

    torch.classes.__path__ = []
except Exception:
    torch = None

import streamlit as st

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

st.set_page_config(page_title="AI Meeting Assistant", page_icon="🤖", layout="centered")

st.title("🤖 AI Meeting Assistant")
st.write("Upload a transcript or document, then generate a summary or ask questions.")

os.makedirs("data/uploads", exist_ok=True)


@st.cache_resource(show_spinner=False)
def build_vectorstore(file_path, file_key):
    from app.rag_pipeline import ingest_data

    return ingest_data(file_path, source_id=file_key)


@st.cache_resource(show_spinner=False)
def build_retriever(file_path, file_key):
    from app.rag_pipeline import get_retriever

    vectorstore = build_vectorstore(file_path, file_key)
    return get_retriever(vectorstore)


def run_summary(retriever):
    from app.summarizer import generate_summary

    return generate_summary(retriever)


def run_answer_query(retriever, query):
    from app.rag_pipeline import answer_query

    return answer_query(retriever, query)

uploaded_file = st.file_uploader("Upload document", type=["txt", "pdf", "docx"])

if uploaded_file:
    file_path = os.path.join("data", "uploads", uploaded_file.name)
    file_bytes = uploaded_file.getvalue()
    file_key = hashlib.sha256(file_bytes).hexdigest()

    with open(file_path, "wb") as f:
        f.write(file_bytes)

    st.success("File uploaded successfully")

    with st.spinner("Processing document..."):
        retriever = build_retriever(file_path, file_key)

    st.subheader("Summary Section")
    if st.button("Generate Summary"):
        with st.spinner("Generating summary..."):
            summary = run_summary(retriever)
        st.text_area("Generated Summary", summary, height=300)

    st.subheader("Question Answering Section")
    query = st.text_input("Ask a question about the uploaded file")

    if st.button("Get Answer"):
        if query.strip():
            with st.spinner("Generating answer..."):
                answer = run_answer_query(retriever, query)
            st.text_area("Answer", answer, height=150)
        else:
            st.warning("Please enter a question.")
