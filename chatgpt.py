"""
You can get the session taken from your browser application cookies.(Make sure you have logged in to the OpenAI's chatGPT console.)
"""

from pyChatGPT import ChatGPT
from pprint import pprint

session_token = "YOUR TOKEN"
try:
    api = ChatGPT(session_token)
    print("Connected to chatGPT!")
except Exception as err:
    print(f"Connection error. {err}")
    raise SystemExit

counter = 1
while True:
    print()
    question = input(f'You: Question-{counter}: ')
    if question != 'q'.lower():
        response = api.send_message(question)
        print()
        pprint(f"GPT: {response['message']}")
    else:
        print("Connection closed")
        break
    counter += 1
