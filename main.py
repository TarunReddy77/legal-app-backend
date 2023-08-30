from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
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


def get_origin():
    if os.getenv('LOCAL_DEV') == 'True':
        return os.getenv("ORIGIN")
    else:
        return os.environ.get("ORIGIN")

# Serve the Vue.js frontend files
# app.mount("/", StaticFiles(directory="../frontend/dist", html=True))


origins = [get_origin()]

# Add CORS middleware to allow frontend API requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

openai.api_key = get_openai_api_key()


class Question(BaseModel):
    question: str


@app.get("/")
def greet():
    return {'Data': 'Hello User'}


@app.post("/ask")
def get_answer(question_data: Question):
    # return {'answer': f'Here is your answer - {openai.api_key}'}
    question = question_data.question
    return answer_question(question)
