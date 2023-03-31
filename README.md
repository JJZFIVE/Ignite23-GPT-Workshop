# Duke Ignite GPT3 Workshop 2023: Using the ChatGPT API

Welcome to Duke Ignite 2023! We're glad you're here. This repository will show you how to use
the ChatGPT API to generate text. You'll be able to chat with it here in your terminal. The goal of
this workshop is to show you how you can incorporate the API into your projects this weekend.
Happy hacking!

## Steps to run this locally

1. Clone this repository and open a terminal window in your project directory
1. `python3 -m venv venv` - creates a virtual environment where you can put your dependencies
1. `source venv/bin/activate` - activates the virtual environment
1. `pip install -r requirements.txt` - installs the dependencies
1. Go to OpenAI and get an API key (https://platform.openai.com/account/api-keys)
1. Create a file called `.env` and add this line: `OPENAI_API_KEY=YOUR OPEN AI KEY HERE FROM THE WEBSITE`
1. `python3 main.py` - runs the program

(Note: how to freeze the venv into requirements.txt: `pip freeze > requirements.txt`)

This repo was put together by Joe Zakielarz, Duke '24.
