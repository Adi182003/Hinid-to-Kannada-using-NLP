from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from model.translator import Translator
import os

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files (CSS, JS)
app.mount("/static", StaticFiles(directory="../frontend/static"), name="static")

# Serve index.html at root
@app.get("/")
def read_index():
    return FileResponse(os.path.abspath("../frontend/index.html"))

class TranslationRequest(BaseModel):
    text: str

@app.post("/translate")
async def translate(request: TranslationRequest):
    translator = Translator()
    translated_text = translator.translate(request.text)
    return {"translated_text": translated_text}
