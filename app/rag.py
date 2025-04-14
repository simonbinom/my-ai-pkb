from langchain_community.llms import Ollama
from sentence_transformers import SentenceTransformer
import chromadb

model = SentenceTransformer('all-MiniLM-L6-v2')
client = chromadb.PersistentClient(path="./embeddings")
llm = Ollama(model="mistral")

def ask_question(query):
    collection = client.get_or_create_collection("notes")  # robust!
    embedding = model.encode(query)
    results = collection.query(query_embeddings=[embedding], n_results=3)
    context = "\n".join(results["documents"][0])
    prompt = f"Beantworte die Frage basierend auf dem folgenden Kontext:\n\n{context}\n\nFrage: {query}"
    return llm(prompt)