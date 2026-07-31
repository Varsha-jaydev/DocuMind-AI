# DocuMind-AI
DocuMind AI is a local Retrieval-Augmented Generation (RAG) chatbot that allows users to ask questions about Python documentation and receive AI-generated answers with relevant context.

The project uses a complete RAG pipeline:
- Document loading
- Text chunking
- Embedding generation
- Vector similarity search
- LLM-based response generation

---

## 🚀 Features

- 📄 Loads Python documentation HTML files
- ✂️ Splits documents into searchable chunks
- 🧠 Generates embeddings using local embedding models
- 🔎 Stores vectors using ChromaDB
- 🤖 Uses local LLM inference with Ollama
- ⚡ FastAPI backend API
- 🌐 Simple web frontend
- 🔒 Runs completely locally (no paid APIs)
