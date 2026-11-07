from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Ayan AI API", version="1.0")

class PromptRequest(BaseModel):
    prompt: str

@app.get("/")
def home():
    return {"message": "Ayan AI API is live and running!"}

@app.post("/v1/chat/completions")
def chat_completion(data: PromptRequest):
    user_query = data.prompt
    response_text = f"Ayan AI processed your prompt: '{user_query}'. Commercial scale API is ready!"
    
    return {
        "model": "ayan-ai-v1",
        "choices": [{
            "message": {
                "role": "assistant",
                "content": response_text
            }
        }]
    }
