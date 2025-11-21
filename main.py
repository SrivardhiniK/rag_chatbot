import streamlit as st
from app.secure_ingest import ingest_pdf
from app.vectorstore import FaissStore
from app.query import answer_query

st.set_page_config(page_title="RAG Chatbot", layout="wide")

st.title("📚 RAG Chatbot (Lightweight Edition)")
st.write("Upload a PDF and ask questions about it!")

uploaded_file = st.file_uploader("Upload PDF", type="pdf")
query = st.text_input("Ask a question")

if uploaded_file:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    text = ingest_pdf("temp.pdf")
    store = FaissStore()
    store.add(text.split("\n"))

    if query:
        context = " ".join(store.search(query))
        answer = answer_query(query, context)
        st.subheader("Answer")
        st.write(answer)
