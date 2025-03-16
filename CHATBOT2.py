import nltk
import random
import spacy
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download required resources
nltk.download("punkt")

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Define knowledge base (solutions)
knowledge_base = {
    "greeting": ["Hello! How can I assist you today?", "Hi there! What can I help you with?", "Hey! Need any help?"],
    "goodbye": ["Goodbye! Have a great day!", "See you soon!", "Take care!"],
    "thanks": ["You're welcome! Always happy to help!", "No problem!", "Glad I could assist!"],
    "troubleshooting": [
        "Try restarting the application and checking for updates.",
        "Make sure all cables are properly connected.",
        "Clear your cache and cookies, then restart your device."
    ],
    "password_reset": [
        "To reset your password, go to the settings page and select 'Reset Password'.",
        "Check your email for a password reset link.",
        "Contact customer support if you're unable to reset your password."
    ],
    "software_installation": [
        "Download the latest version from the official website and follow the installation guide.",
        "Ensure your system meets the minimum requirements before installing.",
        "Run the installer as an administrator to avoid permission issues."
    ]
}

# Prepare data for vectorization
intent_phrases = {
    "greeting": ["hello", "hi", "hey", "good morning", "good evening"],
    "goodbye": ["bye", "goodbye", "see you", "take care"],
    "thanks": ["thank you", "thanks", "appreciate it"],
    "troubleshooting": ["my app is not working", "software crash", "fix error", "troubleshoot issue"],
    "password_reset": ["forgot password", "reset my password", "change password"],
    "software_installation": ["install software", "setup application", "installation guide"]
}

# Create training data
training_sentences = []
training_labels = []

for intent, phrases in intent_phrases.items():
    training_sentences.extend(phrases)
    training_labels.extend([intent] * len(phrases))

# Convert text to TF-IDF vectors
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(training_sentences)

def get_intent(user_input):
    """Identify intent using TF-IDF and cosine similarity."""
    input_vector = vectorizer.transform([user_input])
    similarities = cosine_similarity(input_vector, X)
    best_match_index = similarities.argmax()
    confidence = similarities[0, best_match_index]

    if confidence > 0.3:  # Set confidence threshold
        return training_labels[best_match_index]
    return None

def chatbot_response(user_input):
    """Generate a response based on detected intent."""
    intent = get_intent(user_input)
    if intent and intent in knowledge_base:
        return random.choice(knowledge_base[intent])
    else:
        return "I'm not sure about that. Can you provide more details?"

def chat():
    """Start chatbot conversation loop."""
    print("ChatBot: Hello! How can I assist you? (Type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("ChatBot: Goodbye!")
            break
        response = chatbot_response(user_input)
        print(f"ChatBot: {response}")

if __name__ == "__main__":
    chat()
