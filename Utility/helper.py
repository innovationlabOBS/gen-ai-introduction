import json

# load txt file
def load_txt_file(file_path):
    with open(file_path, 'r', encoding="utf-8") as file:
        return file.read()