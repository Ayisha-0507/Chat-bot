import nltk
import random
from nltk.chat.util import Chat, reflections
from nltk.tokenize import word_tokenize

# Download necessary NLTK data
nltk.download('punkt')

# Skill-based recommendations
skill_resources = {
    "data science": [
        "Start with Python and statistics. Try Google's Data Analytics course: https://bit.ly/3YbKxPR",
        "Learn Pandas & NumPy. Here's a free Data Science roadmap: https://bit.ly/3QYzB6t",
        "Practice real datasets. Check out Kaggle: https://www.kaggle.com/learn"
    ],
    "machine learning": [
        "Learn Scikit-Learn & TensorFlow. A great course: https://bit.ly/3T4XG4r",
        "Build ML models. Hands-on tutorials: https://bit.ly/3OZcCQJ",
        "Follow a structured ML path: https://bit.ly/3D5Z1FN"
    ],
    "coding": [
        "Master Python. Free course: https://bit.ly/3x4nTcz",
        "Improve problem-solving. Try LeetCode: https://leetcode.com",
        "Follow a structured roadmap for coding: https://roadmap.sh"
    ],
    "cybersecurity": [
        "Learn ethical hacking. Free course: https://bit.ly/3IDuKtb",
        "Practice on Hack The Box: https://www.hackthebox.com/",
        "Follow the Cybersecurity roadmap: https://roadmap.sh/cyber-security"
    ],
    "web development": [
        "Start with HTML, CSS, JS. FreeCodeCamp: https://www.freecodecamp.org/",
        "Learn backend with Django/Flask: https://realpython.com/tutorials/django/",
        "Complete roadmap for web dev: https://roadmap.sh/web"
    ]
}

# Define chatbot responses
pairs = [
    ["hi|hello|hey", ["Hello! What skill are you looking to develop?"]],
    ["how are you", ["I'm here to help you with learning! What topic interests you?"]],
    ["my name is (.*)", ["Nice to meet you, %1! What skill do you want to learn?"]],
    ["i want to learn (.*)", ["Great choice! Here are some resources for %1:", "Here’s where you can start learning %1:"]],
    ["bye|exit|quit", ["Goodbye! Keep learning and growing!"]],
    ["thank you|thanks", ["You're welcome! Keep exploring new skills."]],
    ["(.*)", ["I might not know that, but I can help you with tech skills!"]]
]

chatbot = Chat(pairs, reflections)

# Chatbot interaction function
def chatbot_interaction():
    print("ChatBot: Hi! What's your name?")
    user_name = input("You: ").strip().capitalize()
    
    print(f"ChatBot: Nice to meet you, {user_name}! What skill are you interested in learning? (Type 'bye' to exit)")
    
    while True:
        user_input = input(f"{user_name}: ").lower()
        tokens = word_tokenize(user_input)  # Tokenize user input
        
        if user_input in ['bye', 'exit', 'quit']:
            print(f"ChatBot: Goodbye, {user_name}! Keep learning! 🚀")
            break
        
        # Check if the user mentioned a skill
        for skill in skill_resources.keys():
            if skill in user_input:
                print(f"ChatBot: Here are some great resources for {skill}:")
                for resource in skill_resources[skill]:
                    print(f"- {resource}")
                break
        else:
            response = chatbot.respond(user_input)
            print(f"ChatBot: {response}")

# Run the chatbot
if __name__ == "__main__":
    chatbot_interaction()
