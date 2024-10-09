import nltk
from nltk.chat.util import Chat
from llm import chat_with_llm

# Create a dictionary to store user states (for each user session)
user_states = {}

# Pairs: List of patterns and corresponding responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How can I assist you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there!", "Hi! How can I help you today?",]
    ],
    [
        r"how are you?",
        ["I'm doing great, how about you?", "I'm good! Ready to assist you.",]
    ],
    [
        r"thank you|thanks",
        ["You're welcome!", "Happy to help!", "Glad I could assist you!",]
    ],
    [
        r"goodbye|bye|quit",
        ["Goodbye! Have a great day!", "Bye! Looking forward to your visit.", "See you soon at the museum!",]
    ],
    [
        r"तिकिटांची किंमत काय आहे",
        ["राष्ट्रीय संग्रहालयातील प्रवेश शुल्क खालीलप्रमाणे आहे:\n\nप्रौढ: 20 रुपये\nविदेशी नागरिक: 500 रुपये\n12 व्या वर्गापर्यंतचे विद्यार्थी: विनामूल्य (शालेय ओळखपत्रासह)\n\nतुम्हाला कोणत्याही प्रवेश शुल्कांबद्दल अधिक माहिती हवी असेल तर तुम्ही संग्रहालयाच्या वेबसाइटला भेट देऊ शकता किंवा त्यांना फोन करू शकता.\n\nतुमच्याकडे काही प्रश्न असतील तर मला कळवा."]
    ]
]


reflections = {
    "i am"       : "you are",
    "i was"      : "you were",
    "i"          : "you",
    "i'm"        : "you are",
    "i'd"        : "you would",
    "i've"       : "you have",
    "i'll"       : "you will",
    "my"         : "your",
    "you are"    : "I am",
    "you were"   : "I was",
    "you've"     : "I have",
    "you'll"     : "I will",
    "your"       : "my",
    "yours"      : "mine",
    "you"        : "me",
    "me"         : "you"
}


chatbot = Chat(pairs, reflections)

def get_chatbot_response(user_input, user_id):
    response = chatbot.respond(user_input)
    if response:
        return response
    else:
        return chat_with_llm(user_input)



if __name__ == "__main__":
    print("Welcome! I am your museum ticket booking assistant. How can I help you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break
        response = get_chatbot_response(user_input, "user1")
        print(f"Bot: {response}")