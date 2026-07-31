import pickle
import ollama


with open("../../vectorstore/chunks.pkl", "rb") as f:
    chunks = pickle.load(f)


print(f"Loaded {len(chunks)} chunks")


def create_embedding(text):

    response = ollama.embeddings(
        model="nomic-embed-text",
        prompt=text
    )

    return response["embedding"]


# test first chunk

embedding = create_embedding(
    chunks[0].page_content
)


print("Embedding size:", len(embedding))
print(embedding[:5])