######################################################################
# This utility processes the text from an llm by extracting extraneous 
# characters that occur before and after a valid json object, then 
# converting the str to a dict
######################################################################

import re
import json

def json_repair(text):
    # Regular expression pattern to match JSON objects
    # This pattern assumes the JSON object is not nested
    json_pattern = r'\{.*?\}'

    # Search for the JSON object in the text
    match = re.search(json_pattern, text, re.DOTALL)

    if match:
        # Extract the JSON string
        json_str = match.group(0)
        try:
            # Parse the JSON string to ensure it's valid
            json_obj = json.loads(json_str)
            return json_obj
        except json.JSONDecodeError:
            print("Found JSON-like text, but it's not valid JSON.")
            return None
    else:
        print("No JSON object found in the text.")
        return None