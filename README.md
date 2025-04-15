# 🧠 My AI PKB – Local AI-Powered Knowledge Base

This is a lightweight, fully local system for managing your personal knowledge with the support of an AI language model. It combines Markdown files, embeddings, a local LLM, and a web interface for semantic search and interaction.

**This project is an early PoC, do not use in production!**

---

## 🚀 Features

- 📝 Storage in Markdown files  
- 📚 Embedding with Sentence Transformers  
- 🔍 Semantic search using Chroma DB  
- 🧠 LLM integration via Mistral 7B with Ollama  
- 🗣️ Voice input using Whisper (optional)  
- 🖥️ Web frontend with Streamlit  
- 🔌 RAG integration via LangChain  

---

## 📦 Project Structure

```
my-ai-pkb/
├── data/            # Your Markdown notes
├── embeddings/      # Chroma vector database
├── app/
│   ├── embedder.py      # Creates embeddings from Markdown files
│   ├── rag.py           # Retrieval + LLM response
│   ├── whisper_input.py # Voice recording & transcription (optional)
│   └── ui.py            # Streamlit UI
├── requirements.txt
└── README.md
```

---

## 🛠️ Installation

### 1. Prerequisites

- Python 3.10+  
- [Ollama](https://ollama.com/) installed and running  
- ffmpeg for Whisper (e.g., `sudo apt install ffmpeg`)  

### 2. Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## ⚙️ Usage

### 1. Start the Mistral LLM via Ollama

```bash
ollama serve
ollama run mistral
```

### 2. Index your notes

```bash
python app/embedder.py
```

### 3. Launch the UI

```bash
streamlit run app/ui.py
```

---

## 🎤 Voice Interface (optional)

```bash
python app/whisper_input.py
```

> Uses Whisper for speech-to-text transcription.

---

## 🔒 Privacy

All data and models run **locally** – no cloud, no tracking.

---

## 📍 Roadmap

- 🔁 Automatic re-indexing via Git hook  
- 🧾 YAML metadata for Markdown files  
- 📄 PDF/OCR support  
- 🗣️ Voice output with Coqui TTS  
