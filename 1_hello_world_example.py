######################################################################
# This is a simple hello world example of how to run the openai api
# in python. This example sets up the openai client, defines a prompt
# and model parameters, and then calls the openai api to generate a
# response. The response is then parsed and displayed to the user.
######################################################################

import os

from openai import OpenAI

# Retrieve the open ai api key from the environment
api_key = os.getenv("OPENAI_API_KEY")

# Create the openai client
openai_client = OpenAI(api_key=api_key)

# Define a prompt
prompt = "Write a poem about a rainy day"

# Define the model parameters and set the prompt ( in this example, the prompt uses the system role, but we will see examples of user and assistant role in other examples)
model_params = {
        "model": "gpt-4o-2024-05-13",
        "messages": [{"role": "system", "content": prompt}],
        "max_tokens": 4096,
        "temperature": 0.0,
        "top_p": 1,
        "presence_penalty": 0,
        "frequency_penalty": 0,
        "stream": False
    }

# Call the openai api and recieve a response
response = openai_client.chat.completions.create(**model_params)

# Parse the response and display the message
print(response.choices[0].message.content)