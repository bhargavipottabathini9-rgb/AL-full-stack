import chromadb
import streamlit as st
from ollama import chat
from sentence_transformers import SentenceTransformer

st.set_page_config(page_title="Technova Concierge",page_icon=".",layout="wide")

@st.cache_resource
def load_resources():
    model=SentenceTransformer('all-MiniLM-L6-V2')
    client=chromadb.PersistentClient(path="chroma_db")
    collection=client.get_or_create_collection("fest_docs")
    return model,collection
model,collection=load_resources()
st.title("🏠Nova, the Technova concierge")
st.caption("I only know about the fest documents. Ask me anything about Technova.")

st.session_state.setdefault("last_query","-")
st.session_state.setdefault("results",[])

with st.sidebar:
    st.header(" 🧠Knowledge meter")
    st.metric("Total chunks in memory",collection.count())
    st.caption("last searched qurey")
    st.write(st.session_state.last_query)