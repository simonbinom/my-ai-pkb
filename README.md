# 🧠 My AI PKB – Lokale AI-gestützte Wissensdatenbank

Dies ist ein leichtgewichtiges, vollständig lokales System zur Verwaltung deines persönlichen Wissens mit Unterstützung durch ein KI-Sprachmodell. Es kombiniert Markdown-Dateien, Embeddings, ein lokales LLM und eine Weboberfläche zur semantischen Suche und Interaktion.

---

## 🚀 Features

- 📝 Speicherung in Markdown-Dateien
- 📚 Embedding mit Sentence Transformers
- 🔍 Semantische Suche mit Chroma DB
- 🧠 LLM-Integration über Mistral 7B via Ollama
- 🗣️ Sprach-Eingabe mit Whisper (optional)
- 🖥️ Web-Frontend mit Streamlit
- 🔌 RAG-Integration mit LangChain

---

## 📦 Projektstruktur

```
my-ai-pkb/
├── data/            # Deine Markdown-Notizen
├── embeddings/      # Chroma Vektordatenbank
├── app/
│   ├── embedder.py      # Erstellt Embeddings aus Markdown-Dateien
│   ├── rag.py           # Retrieval + LLM-Antwort
│   ├── whisper_input.py # Sprachaufnahme & Transkription (optional)
│   └── ui.py            # Streamlit UI
├── requirements.txt
└── README.md
```

---

## 🛠️ Installation

### 1. Voraussetzungen

- Python 3.10+
- [Ollama](https://ollama.com/) installiert und lauffähig
- ffmpeg für Whisper (z.B. `sudo apt install ffmpeg`)

### 2. Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## ⚙️ Nutzung

### 1. Starte das Mistral LLM via Ollama

```bash
ollama run mistral
```

### 2. Indexiere deine Notizen

```bash
python app/embedder.py
```

### 3. Starte die Oberfläche

```bash
streamlit run app/ui.py
```

---

## 🎤 Sprachinterface (optional)

```bash
python app/whisper_input.py
```

> Nutzt Whisper zur Sprache-zu-Text-Transkription.

---

## 🔒 Datenschutz

Alle Daten und Modelle laufen **lokal** – keine Cloud, kein Tracking.

---

## 📍 Roadmap

- 🔁 Automatischer Re-Index via Git Hook
- 🧾 YAML-Metadaten für Markdown-Dateien
- 📄 PDF/OCR-Support
- 🗣️ Sprach-Ausgabe mit Coqui TTS

---

## 📬 Kontakt

Erstellt als anonymes Template. Anpassbar und erweiterbar nach eigenen Bedürfnissen.
