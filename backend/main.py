from fastapi import FastAPI
from pydantic import BaseModel
from backend.brain import chinky_brain 

app = FastAPI()
@app.get("/")
def home():
    return{
        "message":"Chinky Backend Is Running"
    }
class ChatRequest(BaseModel):
    message: str
    
@app.post("/chat")
def chat(request:ChatRequest):
   chinky_brain(request.message)