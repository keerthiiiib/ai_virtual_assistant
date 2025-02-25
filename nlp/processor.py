import spacy
from loguru import logger

# Load spaCy NLP model
nlp = spacy.load("en_core_web_sm")

# Intent keywords mapping
intent_map = {
    "greeting": ["hello", "hi", "hey"],
    "farewell": ["bye", "goodbye"],
    "thanks": ["thank you", "thanks"],
    "weather": ["weather", "temperature", "forecast"],
}

def process_text(text: str) -> str:
    """Process input text and determine intent."""
    try:
        doc = nlp(text.lower())  # Tokenize and process text
        tokens = [token.text for token in doc]  # Extract words

        for intent, keywords in intent_map.items():
            if any(word in tokens for word in keywords):
                logger.info(f"Intent detected: {intent}")
                return f"Intent recognized: {intent}"

        logger.info("No intent matched.")
        return "Sorry, I didn't understand that."

    except Exception as e:
        logger.error(f"Error processing text: {e}")
        return "An error occurred while processing your request."
