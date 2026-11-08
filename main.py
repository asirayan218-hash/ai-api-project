from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Ayan Independent AI Engine", version="1.0")

# Secret Key jo tumne pehle set ki thi
API_KEY = "ayan_secret_api_key_123"

class PromptRequest(BaseModel):
    prompt: str

@app.post("/generate")
def generate_response(data: PromptRequest, x_key: str = Header(None)):
    # Authentication check
    if x_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key, lala!")
    
    user_input = data.prompt.lower()
    
    # Yahan tumhara apna independent logic aur smart engine chalega
    # Tum yahan apne rules, patterns, ya local AI model ka code fit kar sakte ho
    if "hello" in user_input or "salam" in user_input:
        reply = "Walaikum Assalam! Bolo lala, kya haal hain aur kya help chahiye?"
    elif "kaise ho" in user_input:
        reply = "Main ekdum fit hoon, lala! Batao apna project kahan tak pahuncha."
    else:
        # Dynamic response generation logic (independent of any 3rd-party API)
        reply = f"Ayan AI Engine received: '{data.prompt}'. Yeh lohara aur fast response, bina kisi ki dependency ke!"

    return {
        "status": "success",
        "engine": "Ayan-Core-v1",
        "response": reply
    }from fastapi import FastAPI, Header, HTTPException

app = FastAPI()

# Ek secret API key (jo sirf tumhare pas ho ya RapidAPI ke pass ho)
MY_SECRET_KEY = "ayan_secret_api_key_123"

@app.get("/")
def home():
    return {"message": "AI API is live!"}

@app.get("/predict")
def predict(x_key: str = Header(None)):
    if x_key != MY_SECRET_KEY:
        raise HTTPException(status_code=403, detail="Unauthorized! Invalid or missing API Key.")
    
    # Yahan tumhara AI model ka code aayega
    return {"result": "AI processing successful!"}
      
