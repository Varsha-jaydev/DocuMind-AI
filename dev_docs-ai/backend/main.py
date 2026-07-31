from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from rag.query import ask


app = FastAPI(
    title="DocuMind AI"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class Question(BaseModel):
    question: str



@app.get("/")
def home():

    return {
        "message": "Python AI running"
    }



@app.post("/chat")
def chat(
    data: Question
):

    answer = ask(
        data.question
    )

    return {
        "answer": answer
    }