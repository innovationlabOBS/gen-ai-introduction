######################################################################
# This is an example of how to use the meta prompt patern, which is a 
# template prompt in which values can be replaced with variables.
######################################################################

import os

# From now on, we will be using the llm_api utility for briefness
from Utility.llm_api import llm_api_call, llm_api_call_streaming
from Utility.helper import load_txt_file

meta_prompts_path = "MetaPrompts"

# Load the meta prompt
poem_meta_prompt = load_txt_file(os.path.join(meta_prompts_path, "poem_generator.txt"))

# Define the meta prompt variables
poem_subject = "A rainy day"
poem_author = "Edgar Allen Poe"

# Replace the meta prompt variables with the actual values
prompt = poem_meta_prompt.replace("<<SUBJECT>>", poem_subject).replace("<<AUTHOR>>", poem_author)

# Call the llm api with the prompt
llm_output = llm_api_call(prompt=prompt)

# Display the output
print(llm_output)

