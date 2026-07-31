# 🤖 DocuMind AI - Local RAG Documentation Assistant

DocuMind AI is a local Retrieval-Augmented Generation (RAG) chatbot that allows users to ask questions about Python documentation and receive AI-generated answers with relevant context.

The project uses a complete RAG pipeline:
- Document loading
- Text chunking
- Embedding generation
- Vector similarity search
- LLM-based response generation

---

### Example
<img width="647" height="945" alt="image" src="https://github.com/user-attachments/assets/7e552fb4-31ef-4744-bc36-af1ea8e20f36" />

## 🚀 Features

- 📄 Loads Python documentation HTML files
- ✂️ Splits documents into searchable chunks
- 🧠 Generates embeddings using local embedding models
- 🔎 Stores vectors using ChromaDB
- 🤖 Uses local LLM inference with Ollama
- ⚡ FastAPI backend API
- 🌐 Simple web frontend
- 🔒 Runs completely locally (no paid APIs)

---

## ⚙️ How to Run

### 1. Clone the repository

```bash
git clone <repository-url>
cd dev_docs-ai
```

### 2. Create virtual environment

```bash
python -m venv myenv
```

Activate:

```bash
myenv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r backend/requirements.txt
```

### 4. Setup Ollama

Install Ollama:

https://ollama.com/

Download models:

```bash
ollama pull qwen3:8b
ollama pull nomic-embed-text
```

Start Ollama:

```bash
ollama serve
```

### 5. Create Vector Database

Go to RAG folder:

```bash
cd backend/rag
```

Run:

```bash
python loader.py
python splitter.py
python embeddings.py
python vectorstore.py
```

This will:
- Load documents
- Split documents into chunks
- Generate embeddings
- Create ChromaDB vector database

### 6. Start Backend

Open a new terminal:

```bash
cd backend
```

Run:

```bash
uvicorn main:app --reload
```

Backend:

```
http://127.0.0.1:8000
```

API Docs:

```
http://127.0.0.1:8000/docs
```

### 7. Run Frontend

Open:

```
frontend/index.html
```

in your browser.

Example questions:

- Explain Python decorators
- How do Python generators work?
- Explain async programming

---

## 🛠️ Tech Stack

### Backend
- Python
- FastAPI
- LangChain
- ChromaDB

### AI
- Ollama
- Qwen
- Nomic Embeddings

### Frontend
- HTML
- CSS
- JavaScript


