from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_ollama import OllamaLLM


# Load embeddings
embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)


# Load existing vector database
db = Chroma(
    persist_directory="../../vectorstore/chroma",
    embedding_function=embeddings
)


# Load LLM
llm = OllamaLLM(
    model="qwen3:8b"
)


def ask(question):

    # Retrieve relevant documents
    docs = db.similarity_search(
        question,
        k=4
    )


    context = "\n\n".join(
        [
            doc.page_content
            for doc in docs
        ]
    )


    prompt = f"""
You are DocuMind AI, a technical documentation assistant.

Answer the question using the provided context.

Always structure your answer like this:

## Overview
Give a short explanation.

## Key Concepts
Explain important points using bullet points.

## Example
Provide code examples if applicable.

## Output
Show expected output if applicable.

## Common Use Cases
List practical applications.

## Summary
Give a short conclusion.

Question:
{question}

Context:
{context}

Answer:
"""


    response = llm.invoke(prompt)

    return response



if __name__ == "__main__":

    question = input(
        "Ask Python question: "
    )

    answer = ask(question)

    print("\nAnswer:")
    print(answer)