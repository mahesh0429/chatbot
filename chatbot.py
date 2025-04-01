
import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()


intents = {
    'greeting': ['hello', 'hi', 'hey'],
    'goodbye': ['bye', 'see you later'],
    'thanks': ['thank you', 'thanks'],
    'help': ['help', 'what can you do'],
    'name': ['what is your name?','who are you?']
}


responses = {
    'greeting': 'Hello! How can I assist you today?',
    'goodbye': 'See you later! Have a great day!',
    'thanks': 'You\'re welcome!',
    'help': 'I can answer your questions, provide information, and assist with tasks.',
    'name': 'My Name is Mahi Chatbot,nice to meet you'
}

def chatbot(message):
                          
    tokens = nltk.word_tokenize(message)
    
                          
    lemmas = [lemmatizer.lemmatize(token) for token in tokens]
    
                       
    for intent, keywords in intents.items():
        for keyword in keywords:
            if keyword in message.lower():
                return responses[intent]
    
                      
    return 'I didn\'t understand that. Can you please rephrase?'


while True:
    message = input('User: ')
    response = chatbot(message)
    print('Mahi Chatbot:', response)
