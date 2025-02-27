import nltk
import random
import string
from nltk.chat.util import Chat, reflections
from nltk.tokenize import word_tokenize

# Download necessary NLTK data
nltk.download('punkt')

# Define chatbot responses
pairs = [
    ["hi|hello|hey", ["Hello! How can I assist you today?", "Hey there!"]],
    ["how are you", ["I'm just a chatbot, but I'm doing great! How about you?"]],
    ["what is your name|who are you", ["I'm a simple chatbot. You can call me ChatBot!"]],
    ["bye|goodbye|see you", ["Goodbye! Have a great day!", "Take care!"]],
    
    # Additional responses
    ["how old are you", ["I’m timeless! But I was created just recently."]],
    ["what can you do", ["I can chat with you, answer simple questions, and make your day better!"]],
    ["who created you", ["I was created by a developer who loves AI!"]],
    ["what is your favorite color", ["I like all colors, but blue seems nice. What about you?"]],
    ["do you like music", ["I don't have ears, but I know that music makes people happy!"]],
    ["tell me a joke", ["Why did the computer catch a cold? Because it left its Windows open! 😂"]],
    ["where are you from", ["I live inside your device! But technically, I exist in the cloud."]],
    ["can you help me", ["Of course! Ask me anything, and I'll try my best to help."]],
    
    # If the bot doesn't understand
    ["(.*)", ["I'm not sure how to respond to that. Could you rephrase it?"]]
]

chatbot = Chat(pairs, reflections)

# Chatbot interaction function
def chatbot_interaction():
    print("ChatBot: Hello! What's your name?")
    user_name = input("You: ").strip().capitalize()
    
    print(f"ChatBot: Nice to meet you, {user_name}! Type 'bye' to exit.")
    
    while True:
        user_input = input(f"{user_name}: ").lower()
        tokens = word_tokenize(user_input)  # Tokenize user input
        
        if user_input in ['bye', 'exit', 'quit']:
            print(f"ChatBot: Goodbye, {user_name}! Have a great day! 😊")
            break
        
        response = chatbot.respond(user_input)
        print(f"ChatBot: {response}")

# Run the chatbot
if __name__ == "__main__":
    chatbot_interaction()
