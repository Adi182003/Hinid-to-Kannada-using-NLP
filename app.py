from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from model.translator import Translator

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TranslationRequest(BaseModel):
    text: str

@app.post("/translate")
async def translate(request: TranslationRequest):
    translator = Translator()
    translated_text = translator.translate(request.text)
    return {"translated_text": translated_text}