import google.generativeai as genAI
from dotenv import load_dotenv
import os

load_dotenv() #it loads the variables from .env file

API_KEY=os.getenv("GEMINI_API_KEY")
genAI.configure(api_key=API_KEY)

model = genAI.GenerativeModel("gemini-2.0-flash")

chat = model.start_chat()

print("Chat with gemini! Type 'exit' to quit")

while True:
    user_input=input("You: ")
    if user_input.lower() == "exit":
        break
    response = chat.send_message(user_input)
    print("Gemini: ",response.text)