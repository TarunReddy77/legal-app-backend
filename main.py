from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import openai
import os
from dotenv import load_dotenv

from model import answer_question

app = FastAPI()

load_dotenv()


# Serve the Vue.js frontend files
# app.mount("/", StaticFiles(directory="../frontend/dist", html=True))

origins = [os.getenv("ORIGIN")]

# Add CORS middleware to allow frontend API requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to limit allowed origins
    # allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_openai_api_key():
    if os.getenv('LOCAL_DEV') == 'True':
        return os.getenv("OPENAI_API_KEY")
    else:
        return os.environ.get("OPENAI_API_KEY")


openai.api_key = get_openai_api_key()


class Question(BaseModel):
    question: str


@app.get("/")
def get_answer():
    return {'Data': 'Hello User'}


@app.post("/ask")
def get_answer(question_data: Question):
    return {'answer': f'Here is your answer - {openai.api_key}'}
    # question = question_data.question
    # return answer_question(question)
