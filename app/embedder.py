from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings
from pathlib import Path
import os

DB_DIR = "./embeddings"
DATA_DIR = "./data"
model = SentenceTransformer('all-MiniLM-L6-v2')
client = chromadb.Client(Settings(persist_directory=DB_DIR))
collection = client.get_or_create_collection("notes")

def index_notes():
    for file in Path(DATA_DIR).rglob("*.md"):
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()
            embedding = model.encode(content)
            collection.add(
                documents=[content],
                embeddings=[embedding],
                ids=[str(file)]
            )
    client.persist()