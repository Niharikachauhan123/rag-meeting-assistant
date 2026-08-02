chauhan123/rag-meeting-assistant.git
cd rag-meeting-assistant# 🧠 AI Meeting Intelligence Assistant

An AI-powered meeting intelligence system that analyzes **meeting documents and audio recordings** to generate structured summaries and answer contextual questions using **Retrieval-Augmented Generation (RAG)**.

---

## 🚀 Features

- 📄 Upload meeting documents (**PDF, DOCX, TXT**)
- 🎙️ Upload meeting audio (**MP3, WAV**) for automatic transcription using **OpenAI Whisper**
- 📝 Generate AI-powered meeting summaries
- 📌 Extract Key Points
- ✅ Identify Action Items
- 🎯 Detect Key Decisions
- ❓ Ask contextual questions about uploaded documents and transcripts
- 🔍 Semantic search using **ChromaDB**
- ⚡ Low-latency responses powered by **Groq LLM**
- 🖥️ Interactive web interface built with **Streamlit**

---

## 🏗️ Tech Stack

| Category | Technologies |
|----------|--------------|
| Language | Python |
| Framework | LangChain |
| Vector Database | ChromaDB |
| Embeddings | Sentence Transformers |
| Speech-to-Text | OpenAI Whisper |
| LLM | Groq API (Llama 3) |
| Frontend | Streamlit |

---

## ⚙️ System Architecture

```text
                ┌────────────────────┐
                │ Documents / Audio │
                └─────────┬──────────┘
                          │
          ┌───────────────┴───────────────┐
          │                               │
     PDF/DOCX/TXT                   MP3/WAV
          │                               │
          │                         OpenAI Whisper
          │                               │
          └───────────────┬───────────────┘
                          │
                 Text Extraction
                          │
                  Text Chunking
                          │
        Sentence Transformer Embeddings
                          │
                     ChromaDB
                          │
                 Similarity Retrieval
                          │
                   Groq LLM (Llama 3)
                          │
        ┌────────────────────────────────┐
        │ Summary                        │
        │ Key Points                     │
        │ Action Items                   │
        │ Decisions                      │
        │ Contextual Q&A                 │
        └────────────────────────────────┘
```

---

## 🧠 How It Works

### 📄 Document Processing

1. Upload a meeting document (PDF, DOCX, or TXT).
2. The document is parsed and split into smaller chunks.
3. Sentence Transformers generate vector embeddings.
4. Embeddings are stored in **ChromaDB**.
5. Relevant chunks are retrieved based on the user's query.
6. **Groq LLM** generates context-aware responses and structured meeting insights.

### 🎙️ Audio Processing

1. Upload a meeting recording (MP3 or WAV).
2. **OpenAI Whisper** converts speech into text.
3. The transcript follows the same RAG pipeline as documents.
4. Users can summarize meetings or ask questions about the discussion.

---

## 💡 Example Questions

- Summarize today's meeting.
- What decisions were made?
- List all action items.
- What tasks are assigned to the development team?
- Who is responsible for deployment?
- What were the key discussion points?

---

## 📂 Project Structure

```
rag-meeting-assistant/
│── app.py
│── utils/
│── data/
│── chroma_db/
│── requirements.txt
│── README.md
```

---

