# 🤖 AI Meeting Assistant (RAG-Based)

An AI-powered system that analyzes meeting transcripts and documents to generate structured summaries and answer questions using Retrieval-Augmented Generation (RAG).

---

## 🚀 Features

- 📄 Upload documents (PDF, TXT, DOCX)
- 🧠 Generate structured summaries:
  - Summary
  - Key Points
  - Action Items
  - Decisions Made
- ❓ Ask questions based on document content
- ⚡ Fast LLM responses using Groq API
- 🖥️ Interactive UI built with Streamlit

---

## 🏗️ Tech Stack

- Python
- LangChain
- ChromaDB (Vector Database)
- Sentence Transformers (Embeddings)
- Groq API (LLM)
- Streamlit (Frontend)

---

## 🧠 How It Works

1. User uploads a document
2. Text is split into chunks
3. Embeddings are generated using Sentence Transformers
4. Stored in ChromaDB (vector database)
5. Relevant chunks are retrieved based on query
6. LLM generates final response using retrieved context

---

## ▶️ Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Niharikachauhan123/rag-meeting-assistant.git
cd rag-meeting-assistant