import chromadb

print("1. Import OK")

client = chromadb.PersistentClient(path="test_db")

print("2. Client OK")

collection = client.get_or_create_collection("test")

print("3. Collection OK")

collection.add(
    ids=["1"],
    documents=["Hello world"]
)

print("4. Document added")

print("Count:", collection.count())