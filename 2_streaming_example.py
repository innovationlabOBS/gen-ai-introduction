######################################################################
# This is a simple example that shows how to set up streaming
######################################################################

import os

from openai import OpenAI

# Retrieve the open ai api key from the environment
api_key = os.getenv("OPENAI_API_KEY")

# Create the openai client
openai_client = OpenAI(api_key=api_key)

# Define a prompt
prompt = "Write a poem about a rainy day"

# Define the model parameters and set the prompt
model_params = {
        "model": "gpt-4o-2024-05-13",
        "messages": [{"role": "system", "content": prompt}],
        "max_tokens": 4096,
        "temperature": 0.0,
        "top_p": 1,
        "presence_penalty": 0,
        "frequency_penalty": 0,
        "stream": True
    }

# Call the openai api and recieve a response
response = openai_client.chat.completions.create(**model_params)

# This response will be a generator that we can iterate over to get the chunks as they are created
for chunk in response:
    print(chunk.choices[0].delta.content, end='')