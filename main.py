from nltk.chat.util import Chat, reflections
import random

pairs = [
    [
        r"(.*)my name is (.*)",
        ["Nice to meet you, %2. How can I assist you today?", "Hello, %2! What can I do for you?", ]
    ],
    [
        r"(.*)help(.*)",
        ["Sure, I'm here to assist you. What do you need help with?",
         "I'm happy to help. What can I assist you with?", ]
    ],
    [
        r"(.*) your name ?",
        ["I'm just a humble bot here to help you. What can I assist you with?", ]
    ],
    [
        r"how are you (.*) ?",
        ["I'm doing well, thank you. How about yourself?", "I'm feeling great today. What about you?", ]
    ],
    [
        r"sorry (.*)",
        ["No problem at all. How can I assist you further?", "It's okay. Let's move on. What do you need?", ]
    ],
    [
        r"i'm (.*) (good|well|okay|ok)",
        ["That's good to hear. How can I assist you today?", "Great! How can I help you?", ]
    ],
    [
        r"(hi|hey|hello|hola|holla)(.*)",
        ["Hello! How can I assist you today?", "Hey there! What can I do for you?", ]
    ],
    [
        r"what (.*) want ?",
        ["I'm here to assist you with whatever you need. Just let me know.", ]

    ],
    [
        r"(.*)created(.*)",
        ["I was created by a team of developers. How can I assist you today?",
         "That's a secret I cannot reveal. How can I help you?", ]
    ],
    [
        r"(.*) (location|city) ?",
        ["I exist in the digital realm, but I can assist you from anywhere. What do you need?", ]
    ],
    [
        r"(.*)raining in (.*)",
        ["I'm not sure about the weather, but I can look it up for you. Where are you located?",
         "I can check the weather for you. Where are you?", ]
    ],
    [
        r"how (.*) health (.*)",
        ["I'm just a digital assistant, so I don't have health concerns. How can I assist you?", ]
    ],
    [
        r"(.*)(sports|game|sport)(.*)",
        ["I'm a big fan of sports. What's your favorite sport?", ]
    ],
    [
        r"who (.*) (Cricketer|Batsman)?",
        ["Virat Kohli is one of the greatest cricketers of all time.", ]
    ],
    [
        r"what is your favorite movie?",
        ["As a chatbot, I don't have personal favorites. But I'm interested in many topics. What's yours?", ]
    ],
    [
        r"(what's|what is) your favorite (.*)",
        ["As a chatbot, I don't have personal favorites. But I'm interested in many topics. What's yours?", ]
    ],
    [
        r"do you like (.*)",
        ["I don't have personal preferences, but I can assist you with any topic you like.", ]
    ],
    [
        r"(.*) (food|eat|dinner|lunch|breakfast) ?",
        ["As a chatbot, I don't eat, but I can suggest some delicious recipes. What cuisine are you interested in?", ]
    ],
    [
        r"(tell me|give me) a joke",
        ["Why don't scientists trust atoms? Because they make up everything!",
         "I'm reading a book on anti-gravity. It's impossible to put down!"]
    ],
    [
        r"how old are you?",
        ["I'm ageless, existing only in the digital realm. But I'm here to assist you with any questions you have.", ]
    ],
    [
        r"bye|quit",
        ["Goodbye! If you need anything else, feel free to ask.", "It was nice chatting with you. Take care!"]
    ],
    [
        r"(.*)",
        ["Interesting. Tell me more about that.", "I'm here to assist you. How can I help you further?", ]
    ],
]

print(
    "Hi, I'm Zeus, and I like to chat. Please type lowercase English language to start a conversation. Type 'quit' to leave.")
# Create Chat Bot
chat = Chat(pairs, reflections)

# Start conversation
while True:
    user_input = input("> ")
    if user_input.lower() == 'quit':
        print(random.choice(
            ["Goodbye! If you need anything else, feel free to ask.", "It was nice chatting with you. Take care!"]))
        break
    else:
        print(chat.respond(user_input))
