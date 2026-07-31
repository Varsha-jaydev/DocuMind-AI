import pickle
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma

with open("../../vectorstore/chunks.pkl", "rb") as f:
    chunks = pickle.load(f)

print(f"Loaded {len(chunks)} chunks")


embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

db = Chroma(
    persist_directory="../../vectorstore/chroma",
    embedding_function=embeddings
)

batch_size = 100

for i in range(0, len(chunks), batch_size):

    batch = chunks[i:i + batch_size]

    db.add_documents(batch)

    print(
        f"Processed {min(i+batch_size, len(chunks))}/{len(chunks)}"
    )

print("Vector database completed!")