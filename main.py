from fastapi import FastAPI, Request, HTTPException
from fastapi import File, UploadFile
from nlp.processor import process_text
from pydantic import BaseModel
from database.mongo import save_interaction, get_all_interactions  # Ensure this exists
from loguru import logger
import speech_recognition as sr
import io

# Initialize FastAPI
app = FastAPI()

# Configure Loguru logging
logger.add("logs/app.log", rotation="1 MB", retention="10 days", level="INFO")

# Define Input Model
class UserInput(BaseModel):
    text: str

@app.post("/process/")
async def process(request: Request, user_input: UserInput):
    logger.info(f"Received Request: {await request.json()}")  # Log incoming request
    response = process_text(user_input.text)
    
    # Save interaction in MongoDB 
    try:
        save_interaction(user_input.text, response)
    except Exception as e:
        logger.error(f"Failed to save interaction: {e}")
    
    logger.info(f"Response: {response}")  # Log API response
    return {"response": response}

@app.post("/process-voice/")
async def process_voice(file: UploadFile = File(...)):
    """Process voice input and return text response."""
    recognizer = sr.Recognizer()
    audio_data = await file.read()
    audio_file = io.BytesIO(audio_data)
    
    with sr.AudioFile(audio_file) as source:
        try:
            audio = recognizer.record(source)
            text = recognizer.recognize_google(audio)  # Convert speech to text
            response = process_text(text)
            save_interaction(text, response)
            return {"transcribed_text": text, "response": response}
        except sr.UnknownValueError:
            raise HTTPException(status_code=400, detail="Could not understand the audio.")
        except sr.RequestError as e:
            raise HTTPException(status_code=500, detail=f"Speech Recognition API error: {e}")

@app.get("/interactions/")
async def get_interactions(limit: int = 10):
    """Fetch stored interactions from MongoDB."""
    interactions = get_all_interactions(limit)
    
    if not interactions:  
        raise HTTPException(status_code=404, detail="No interactions found")
    
    return {"interactions": interactions}
