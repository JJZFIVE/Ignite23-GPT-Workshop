# https://platform.openai.com/docs/guides/chat/introduction

import os
import openai
from dotenv import load_dotenv

# Load the environment variables from .env file. See README.md for more details
load_dotenv()

# Set the OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            ]
print("---Welcome to Terminal-GPT---", end="\n\n")

while (True):
    # Get user input
    user_input = input("Enter query: ")
    messages.append({"role": "user", "content": user_input})
   
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=1000
    )

    messages.append(response.choices[0].message)
    print(response.choices[0].message.content)

    if (response.choices[0].finish_reason != "stop"):
        print("You've exceeded the max supply of tokens. Please restart the program.")
        break
