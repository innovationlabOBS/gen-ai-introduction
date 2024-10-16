######################################################################
# Functions to call simple llm api for testing
######################################################################

import os
import numpy as np
from openai import OpenAI

api_key = os.getenv("OPENAI_API_KEY")

openai_client = OpenAI(api_key=api_key)

def llm_api_call(prompt=None, messages=None, temperature=0.0):

    if messages != None:
        pass
    elif prompt != None:
        messages = [{"role": "system", "content": prompt}]
    else:
        raise ValueError("prompt or messages must be provided")

    model_params = {
            "model": "gpt-4o-2024-05-13",
            "messages": messages,
            "max_tokens": 4096,
            "temperature": temperature,
            "top_p": 1,
            "presence_penalty": 0,
            "frequency_penalty": 0,
            "stream": False
        }

    response = openai_client.chat.completions.create(**model_params)
    return response.choices[0].message.content
    
def llm_api_call_streaming(prompt=None, messages=None, temperature=0.0):

    if messages != None:
        pass
    elif prompt != None:
        messages = [{"role": "system", "content": prompt}]
    else:
        raise ValueError("prompt or messages must be provided")

    model_params = {
            "model": "gpt-4o-2024-05-13",
            "messages": messages,
            "max_tokens": 4096,
            "temperature": temperature,
            "top_p": 1,
            "presence_penalty": 0,
            "frequency_penalty": 0,
            "stream": True
        }

    response = openai_client.chat.completions.create(**model_params)
    for chunk in response:
        yield chunk.choices[0].delta.content

# Used for rag
def get_embedding(text, model="text-embedding-3-small"):
    return openai_client.embeddings.create(input = [text], model=model).data[0].embedding