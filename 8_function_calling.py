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

# Load the meta prompt
function_calling_meta_prompt = load_txt_file(os.path.join(meta_prompts_path, "function_calling.txt"))

# Get the user query
user_query = input("Enter your math problem: ")

# Replace the meta prompt variables with the actual values
prompt = prompt_constructor(meta_prompt=function_calling_meta_prompt, variables={"USER_QUERY": user_query})

# Call the llm api with the prompt and get the structured data string
json_output_str = llm_api_call(prompt=prompt)

# Show the raw output ( uncomment this to see the generated python method )
# print(json_output_str)

# convert the output string to a dictionary. The json repair is necessary because often, the llm will output json objects with superfluous text before and after the json object.
dict_output = json_repair(json_output_str)

# Get the method body and the name
python_method = dict_output["python_method"]
method_name = dict_output["method_name"]

# Execute the method to make it available in the code
exec(python_method)

# Call the method
result = eval(f"{method_name}()")

# Display the result
print(f"The answer is: {result}")
