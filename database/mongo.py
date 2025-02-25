from pymongo import MongoClient
from loguru import logger

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")  # Change this if using Docker
db = client["ai_voice_assistant"]  # Database name
collection = db["interactions"]  # Collection (table) name

def save_interaction(user_text, bot_response):
    """Save user input and bot response to MongoDB."""
    data = {"user_input": user_text, "bot_response": bot_response}
    collection.insert_one(data)
    print(f"Saved to MongoDB: {data}")
def get_all_interactions(limit=10):
    """Retrieve stored interactions from MongoDB."""
    try:
        interactions = list(collection.find().limit(limit))  # Convert cursor to list
        return [{"user_input": i.get("user_input", ""), "bot_response": i.get("bot_response", "")} for i in interactions]
    except Exception as e:
        logger.error(f"Error retrieving interactions: {e}")
        return []
