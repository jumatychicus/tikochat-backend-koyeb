from fastapi import FastAPI
import requests, os

app = FastAPI()
HF_TOKEN = os.getenv("HF_TOKEN")
MODEL_URL = "https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct"

headers = {"Authorization": f"Bearer {HF_TOKEN}"}

@app.post("/")
async def chat(data: dict):
    prompt = data.get("question", "")
    payload = {"inputs": prompt}
    response = requests.post(MODEL_URL, headers=headers, json=payload)
    result = response.json()
    reply = result[0]["generated_text"] if "generated_text" in result[0] else str(result)
    return {"reply": reply}
