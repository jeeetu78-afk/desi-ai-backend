from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TextInput(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "Desi AI Backend Live 🚀"}

@app.post("/generate")
def generate(data: TextInput):
    return {
        "reply": f"Arre bhai 😂 tumne likha: {data.text}"
    }
