from fastapi import FastAPI, Header, HTTPException

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
