######################################################################
# This is an example of how to use structured output to implemetn chain 
# of thought. The llm will output a rationale behind it's answer to the
# user, in addition to the curated answer. Only the curated answer will 
# be displayed to the user, as the rationale's purpose is just to guide
# the LLM in generating a better answer. This works because of the auto
# regressive nature of LLMs.
######################################################################

import os
import json

from Utility.llm_api import llm_api_call, llm_api_call_streaming
from Utility.prompt_constructor import prompt_constructor
from Utility.helper import load_txt_file
from Utility.json_repair import json_repair

meta_prompts_path = "MetaPrompts"
data_path = "Data"

# Load the meta prompt
chain_of_thought_meta_prompt = load_txt_file(os.path.join(meta_prompts_path, "chain_of_thought.txt"))

# Get user question
user_input = input("Enter your question: ")

# Replace the meta prompt variables with the actual values
prompt = prompt_constructor(meta_prompt=chain_of_thought_meta_prompt, variables={"USER_QUESTION": user_input})

# Call the llm api with the prompt and get the structured data string
json_output_str = llm_api_call(prompt=prompt)

# print the raw output to view the rationale
print(json_output_str)

# convert the output string to a dictionary. The json repair is necessary because often, the llm will output json objects with superfluous text before and after the json object.
dict_output = json_repair(json_output_str)

# print the curated answer
print("========= Answer =========")
print(dict_output["answer"])

