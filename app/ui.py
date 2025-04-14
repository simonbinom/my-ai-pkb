import streamlit as st
from app.rag import ask_question
from app.embedder import index_notes

st.title("Deine AI-Wissensdatenbank")
if st.button("Re-Indexiere Notizen"):
    index_notes()
    st.success("Index aktualisiert!")

query = st.text_input("Frage:")
if query:
    answer = ask_question(query)
    st.write("Antwort:", answer)