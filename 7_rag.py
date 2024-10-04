######################################################################
# This is an example of rag or retrieval augmented generation. It is 
# a technique that uses embedding vectors to retrieve relevant chunks
# from a large text source and adds these to the prompt in order to 
# generate a more relevant response.
# This example uses json files instead of a vector database for simplicity.
######################################################################

import os
import json
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from Utility.llm_api import llm_api_call, llm_api_call_streaming, get_embedding
from Utility.prompt_constructor import prompt_constructor
from Utility.helper import load_txt_file

meta_prompts_path = "MetaPrompts"
rag_documents_path = "RAG Documents"
rag_embeddings_path = "RAG Embeddings"

# Determines the size of each text chunk in words
chunk_size = 1000

# Overlap is used so that information isn't lost between chunks.
overlap_size = 20

# Number of chunks to retrieve and put into the prompt
chunks_to_retrieve = 5

# Meta prompt used for rag
rag_meta_prompt = load_txt_file(os.path.join(meta_prompts_path, "rag.txt"))

# Large document to retrieve chunks from
rag_document = load_txt_file(os.path.join(rag_documents_path, "DSM5.txt"))

# This function takes in the filename of a large document and creates json files containing chunks of 
# text along with an embedding vector
def create_rag_from_filename(filename):
    with open(filename,'r', encoding="utf-8") as f:
        contents = f.read()
        chunks = create_text_chunks(contents)
        json_filename = os.path.splitext(rag_embeddings_path + os.path.basename(filename))[0] + '.json'
        create_rag_embeddings_json(chunks, json_filename)

# This function takes in a string of text and returns a list of text chunks
def create_text_chunks(text):
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size - overlap_size):
        chunk = words[i:i + chunk_size]
        chunks.append(' '.join(chunk))
    return chunks

# This function takes in a list of text chunks and a filename and creates json files containing 
# the text chunks and their embedding vectors
def create_rag_embeddings_json(chunks, filename):
    for i, chunk in enumerate(chunks):
        print("Processing Chunk " + str(i))
        embedding = get_embedding(chunk)
        entry = { 'text': chunk, 'embedding': embedding}
        with open(f"{rag_embeddings_path}/{filename}_{str(i)}.json", 'w', encoding="utf-8") as f:
            json.dump(entry, f)

# Loads in the embedding vectors from the json files
def load_embeddings():
    print("Loading Embeddings...")
    text_embedding_array = []
    files = os.listdir(rag_embeddings_path)
    for file in files:
        with open(os.path.join(rag_embeddings_path, file), 'r', encoding="utf-8") as f:
            text_embedding_array.append(json.load(f))
    print("Finished Loading Embeddings")
    return text_embedding_array

# Creates an embedding vector for the user query and uses cosine similarity to find the most 
# similar chunks of text
def get_top_results(user_query, text_embedding_array):
    user_query_embedding = np.array(get_embedding(user_query)).reshape(1, -1)
    embeddings = np.array([item['embedding'] for item in text_embedding_array])
    cos_similarities = cosine_similarity(user_query_embedding, embeddings)[0]
    top_indices = np.argsort(cos_similarities)[-chunks_to_retrieve:]
    top_texts = [text_embedding_array[i]['text'] for i in top_indices]
    return top_texts

if __name__ == "__main__":
    # This creates the embedding vectors for the document. This only needs to be done once and takes 
    # a little while. If you want to test this out, delete the contents of the RAG Embeddings folder 
    # and run the line below.

    #create_rag_from_filename(os.path.join(rag_documents_path, "DSM5.txt"))

    # Load the text chunks and associated embedding vectors
    text_embedding_array = load_embeddings()

    # We are using the DSM5 in this example, so ask the user for a mental health related question
    user_query = input("Enter your mental health related question: ")

    # Get the top results based on the user query
    top_results = get_top_results(user_query, text_embedding_array)

    # Create the prompt by injecting the user query and the rag content into the meta prompt
    prompt = prompt_constructor(meta_prompt=rag_meta_prompt, variables={"USER_QUERY": user_query, "RAG_CHUNKS": "\n".join(top_results)})

    # Call the llm api with the prompt
    response = llm_api_call(prompt=prompt)

    # Display response
    print("Assistant: " + response)

