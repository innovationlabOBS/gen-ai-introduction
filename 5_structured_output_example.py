######################################################################
# This is an example of how to use the llm to generate structured data.
# This can be useful for generating multiple output per inference, as well
# as generating structured data for conventional downstream code.
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
structured_output_meta_prompt = load_txt_file(os.path.join(meta_prompts_path, "structured_output.txt"))

# Define the meta prompt variables
hobbies = load_txt_file(os.path.join(data_path, "hobbies_list.txt"))
favorite_foods = load_txt_file(os.path.join(data_path, "favorite_foods.txt"))

# Replace the meta prompt variables with the actual values
prompt = prompt_constructor(meta_prompt=structured_output_meta_prompt, variables={"HOBBIES": hobbies, "FAVORITE_FOODS": favorite_foods})

# Call the llm api with the prompt and get the structured data string
json_output_str = llm_api_call(prompt=prompt)

print(json_output_str)

# convert the output string to a dictionary. The json repair is necessary because often, the llm will output json objects with superfluous text before and after the json object.
dict_output = json_repair(json_output_str)

# Access the individual elements of the object as required
print(dict_output["hobbies"])
print(dict_output["foods"])

