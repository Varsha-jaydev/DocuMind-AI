import pickle
from langchain_text_splitters import RecursiveCharacterTextSplitter


with open("../../vectorstore/docs.pkl", "rb") as f:
    docs = pickle.load(f)


splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)


chunks = splitter.split_documents(docs)


print(f"Created {len(chunks)} chunks")


with open("../../vectorstore/chunks.pkl", "wb") as f:
    pickle.dump(chunks, f)