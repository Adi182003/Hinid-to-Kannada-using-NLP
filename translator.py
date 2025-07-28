from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

class Translator:
    def __init__(self):
        self.model_name = "ai4bharat/indictrans2-indic-en-1B"
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name, use_fast=False, trust_remote_code=True)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(self.model_name, trust_remote_code=True)

    def translate(self, text):
        # IndicTrans2 expects a prefix for source and target languages
        input_text = f"<2kan> {text}"  # <2kan> means translate to Kannada
        inputs = self.tokenizer(input_text, return_tensors="pt", padding=True, truncation=True)
        output_tokens = self.model.generate(**inputs, max_length=256)
        translated_text = self.tokenizer.decode(output_tokens[0], skip_special_tokens=True)
        return translated_text

translator = Translator()