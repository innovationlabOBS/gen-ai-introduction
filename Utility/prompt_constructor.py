######################################################################
# A function to construct a prompt from a meta prompt and a dictionary 
# of variables
######################################################################

def prompt_constructor(meta_prompt, variables):
    """
    Construct a prompt from a meta prompt and a dictionary of variables

    Args:
    meta_prompt (str): The meta prompt string
    variables (dict): The dictionary of variables to replace in the meta prompt

    Returns:
    str: The constructed prompt
    """
    prompt = meta_prompt
    for key, value in variables.items():
        prompt = prompt.replace(f"<<{key}>>", value)
    return prompt