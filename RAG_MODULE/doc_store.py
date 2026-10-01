from ollama import embed
import chromadb

print("1. Starting...")

# Read file
with open("fest_info.txt", "r", encoding="utf-8") as f:
    text = f.read()

print("2. File loaded")
print("Characters:", len(text))


# Chunk text
def chunk_text(text, chunk_size=300, overlap=50):
    chunks = []
    start = 0

    while start < len(text):
        chunks.append(text[start:start + chunk_size])
        start += chunk_size - overlap

    return chunks


chunks = chunk_text(text)

print("3. Chunks created:", len(chunks))


# Create embeddings
print("4. Creating embeddings...")

response = embed(
    model="nomic-embed-text",
    input=chunks
)

embeddings = response.embeddings

print("5. Embeddings created:", len(embeddings))


# Start ChromaDB
print("6. Starting ChromaDB...")

client = chromadb.PersistentClient(
    path="chroma_db"
)

print("7. ChromaDB started")


# Create collection
collection = client.get_or_create_collection(
    name="fest_docs"
)

print("9. Adding documents...")

collection.add(
    ids=[f"chunk_{i}" for i in range(len(chunks))],
    documents=chunks,
    embeddings=embeddings
)

print("10. Documents added")

print(f"Total {collection.count()} docs created.")