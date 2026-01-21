from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TextInput(BaseModel):
    text: str

desi_replies = [
    "Arre bhai 😄 zindagi me itna mat soch",
    "Aye haye 😂 ye toh full desi problem hai",
    "Bhai tu tension le raha hai, tension tujhe le jayegi",
    "Shaanti rakho mitron, sab set ho jayega",
    "Bhai ye duniya gol hai, ghoom ke wahi aati hai"
]
@app.get("/")
def home():
    return {
        "message": "Desi AI Backend Live 🚀",
        "status": "running"
    }

@app.post("/chat")
def chat(input: TextInput):
    reply = random.choice(desi_replies)
    return {
        "question": input.text,
        "reply": reply
    }
