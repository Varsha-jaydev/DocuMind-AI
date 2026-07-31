from langchain_community.llms import Ollama


def answer_question(db, question):

    docs=db.similarity_search(
        question,
        k=4
    )


    context="\n".join(
        [d.page_content for d in docs]
    )


    llm=Ollama(
        model="qwen3:8b"
    )


    prompt=f"""

You are a Python documentation assistant.

Use this context:

{context}


Question:
{question}

Answer clearly.

"""


    return llm.invoke(prompt)