# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lrzvkrxY2IqfkkUTyd45ma7Vwy_IT_7Z
"""

import nltk
from nltk.chat.util import Chat, reflections

# Define some basic patterns and responses
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you', ['I am doing well, thank you!', 'I\'m fine, thanks. How about you?']),
    (r'fine|good', ['Great!', 'That\'s good to hear.']),
    (r'bye|goodbye', ['Goodbye!', 'See you later!', 'Bye.']),
    (r'(.*)', ["I'm sorry, I didn't understand that.", 'Could you please rephrase that?']),
]

# Create a chatbot using the patterns
chatbot = Chat(patterns, reflections)

# Function to start the chat
def start_chat():
    print("Hello! I'm your chatbot. Type 'bye' to exit.")
    while True:
        user_input = input('You: ')
        if user_input.lower() == 'bye':
            print('Goodbye!')
            break
        response = chatbot.respond(user_input)
        print('Bot:', response)

# Download necessary NLTK data (only need to run this once)
# nltk.download('punkt')

# Start the chat
start_chat()
  


