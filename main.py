from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI(
    title="Desi AI 🤖",
    description="Full Desi Style AI Backend 😄☕",
    version="1.0"
)

class TextInput(BaseModel):
    text: str

desi_replies = [
    "Arre bhai 😄 zindagi me itna mat soch, chai pee ☕",
    "Aye haye 😂 ye toh full desi problem hai",
    "Bhai tu tension le raha hai, tension tujhe le rahi hai 😭",
    "Shaanti rakho mitron, sab set ho jayega 😎",
    "Bhai ye duniya gol hai, ghoom ke sab milta hai 🤝"
]

@app.get("/")
def home():
    return {
        "message": "Desi AI Backend Live 🚀",
        "status": "running"
    }

@app.post("/generate")
def generate(data: TextInput):
    reply = random.choice(desi_replies)
    return {
        "input": data.text,
        "reply": reply
    }
