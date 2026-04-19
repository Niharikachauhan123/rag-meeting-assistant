import sys
import os
import shutil
import streamlit as st

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from app.rag_pipeline import ingest_data, get_retriever, answer_query
from app.summarizer import generate_summary

st.set_page_config(page_title="AI Meeting Assistant", page_icon="🤖", layout="centered")

st.title("🤖 AI Meeting Assistant")
st.write("Upload a transcript or document, then generate a summary or ask questions.")

os.makedirs("data/uploads", exist_ok=True)

uploaded_file = st.file_uploader("Upload document", type=["txt", "pdf", "docx"])

if uploaded_file:
    if os.path.exists("data/chroma_db"):
        shutil.rmtree("data/chroma_db")

    file_path = os.path.join("data", "uploads", uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("File uploaded successfully")

    with st.spinner("Processing document..."):
        vectorstore = ingest_data(file_path)
        retriever = get_retriever(vectorstore)

    st.subheader("Summary Section")
    if st.button("Generate Summary"):
        with st.spinner("Generating summary..."):
            summary = generate_summary(retriever)
        st.text_area("Generated Summary", summary, height=300)

    st.subheader("Question Answering Section")
    query = st.text_input("Ask a question about the uploaded file")

    if st.button("Get Answer"):
        if query.strip():
            with st.spinner("Generating answer..."):
                answer = answer_query(retriever, query)
            st.text_area("Answer", answer, height=150)
        else:
            st.warning("Please enter a question.")
