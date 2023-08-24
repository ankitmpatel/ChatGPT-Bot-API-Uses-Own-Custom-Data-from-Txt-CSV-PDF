from llama_index import SimpleDirectoryReader, GPTListIndex, readers, GPTSimpleVectorIndex, LLMPredictor, PromptHelper, ServiceContext
from langchain import OpenAI
import sys
import os

def construct_index():
    # Set the directory path where your content_data folder is located
    directory_path = './context_data'
    # Set OpenAI API key
    os.environ["OPENAI_API_KEY"] = "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"
    # set maximum input size
    max_input_size = 4096
    # set number of output tokens
    num_outputs = 2000
    # set maximum chunk overlap
    max_chunk_overlap = 20
    # set chunk size limit
    chunk_size_limit = 600 

    # define prompt helper
    prompt_helper = PromptHelper(max_input_size, num_outputs, max_chunk_overlap, chunk_size_limit=chunk_size_limit)

    # define LLM
    llm_predictor = LLMPredictor(llm=OpenAI(temperature=0, model_name="text-embedding-ada-002", max_tokens=num_outputs))
 
    documents = SimpleDirectoryReader(directory_path).load_data()
    
    service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor, prompt_helper=prompt_helper)
    index = GPTSimpleVectorIndex.from_documents(documents, service_context=service_context)

    index.save_to_disk('index.json')

    return index

construct_index()
