import os
import json
from dotenv import load_dotenv
from chatbot_rag_chroma.vector_db.vectordb import create_vector_db
from chatbot_rag_chroma.data_processing.preprocess import extract_text, process_text
from chatbot_rag_chroma.models.ai_model import llm
from chatbot_rag_chroma.prompts.prompt import prompt
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough
import sys

sys.path.append(os.path.abspath(os.getenv("FOLDER_PATH")))
load_dotenv()

print(f"PYTHONPATH: {os.getenv('PYTHONPATH')}")


#DATA_PATH = os.getenv("DATAPATH")
#file_path = os.path.join(DATA_PATH, "website_structure.json")
file_path = os.getcwd()+ "/chatbot_rag_chroma/data_processing/website_structure.json"

#DATA_PATH = os.path.join(os.getcwd(), "chatbot_rag_chroma", "data_processing")
#file_path = os.path.join(DATA_PATH, "website_structure.json")

def get_chain(prompt, llm):
    chain = (
        {"context": RunnablePassthrough(), "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    return chain

def get_retriever():
    with open(file_path, "r") as f:
        data = json.load(f)
    
    text = extract_text(data)
    documents = process_text(text)
    vector_db = create_vector_db(documents)
    
    retriever = vector_db.as_retriever(
        search_type="similarity_score_threshold",
        search_kwargs={"k": 3, "score_threshold": 0.5},
    )
    
    return retriever

