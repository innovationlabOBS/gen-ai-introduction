######################################################################
# This is an example of how to set up a chatbot that uses the user and 
# assistant roles
######################################################################

import os

from openai import OpenAI

# Define variable for chat loop. Chat will run as long as running is True
running = True

# Create a chat history that will be appended to as the conversation progresses
chat_history = []

# Retrieve the open ai api key from the environment
api_key = os.getenv("OPENAI_API_KEY")

# Create the openai client
openai_client = OpenAI(api_key=api_key)

# Define a system prompt ( the system prompt is used to define background instructions on how the LLM should behave)
system_prompt = "You are a helpful assistent. start by introducing yourself and asking the user what they need assistance with."

# Add the system prompt to the chat history
chat_history.append({"role": "system", "content": system_prompt})

# create a function that will return the model parameters with the messages set to chat history
def get_model_params():
    return {
        "model": "gpt-4o-2024-05-13",
        "messages": chat_history,
        "max_tokens": 4096,
        "temperature": 0.0,
        "top_p": 1,
        "presence_penalty": 0,
        "frequency_penalty": 0,
        "stream": False
    }

# Create infinite loop for chat conversation
while running == True:
    # Call the openai api and recieve a response
    response = openai_client.chat.completions.create(**get_model_params())

    # Get the assistant text response
    assistant_response = response.choices[0].message.content

    # Display the assistant response
    print("Assistant: " + assistant_response)

    # Add the assistant response to the chat history
    chat_history.append({"role": "assistant", "content": assistant_response})

    # Get the user input
    user_response = input("User: ")

    # If the user types "exit", then end the conversation
    if user_response.lower() == "exit":
        running = False
        break

    # Add the user input to the chat history
    chat_history.append({"role": "user", "content": user_response})