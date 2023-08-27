from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import openai
import os
from dotenv import load_dotenv

from model import answer_question

app = FastAPI()

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

origins = [os.getenv("ORIGIN")]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Question(BaseModel):
    question: str


@app.post("/ask")
def get_answer(question_data: Question):
    question = question_data.question
    return answer_question(question)