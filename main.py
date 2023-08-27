from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import openai
import os
from dotenv import load_dotenv

from model import answer_question

app = FastAPI()

load_dotenv()


def get_openai_api_key():
    if os.getenv('LOCAL_DEV') == 'True':
        return os.getenv("OPENAI_API_KEY")
    else:
        return os.environ.get("OPENAI_API_KEY")


openai.api_key = get_openai_api_key()
# origins = [os.getenv("ORIGIN")]
#
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


class Question(BaseModel):
    question: str


@app.get("/")
def get_answer():
    return {'Data': 'Hello User'}


@app.post("/ask")
def get_answer(question_data: Question):
    return {'answer': 'Here is your answer'}
    # question = question_data.question
    # return answer_question(question)
