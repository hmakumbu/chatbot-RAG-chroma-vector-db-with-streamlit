import os
import json
from dotenv import load_dotenv
from chatbot_rag_chroma.vector_db.vectordb import create_vector_db
from chatbot_rag_chroma.data_processing.preprocess import process_documents
from chatbot_rag_chroma.data_processing.load import load_text
from chatbot_rag_chroma.models.ai_model import llm
from chatbot_rag_chroma.prompts.prompt import prompt
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough
import sys

sys.path.append(os.path.abspath(os.getenv("FOLDER_PATH")))
load_dotenv()

print(f"PYTHONPATH: {os.getenv('PYTHONPATH')}")


file_path = os.getenv("DATAPATH")

def get_chain(prompt, llm):
    chain = (
        {"context": RunnablePassthrough(), "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    return chain

def get_retriever():
    
    text = load_text(file_path)
    documents = process_documents(text)
    vector_db = create_vector_db(documents)
    
    retriever = vector_db.as_retriever(
        search_type="similarity_score_threshold",
        search_kwargs={"k": 3, "score_threshold": 0.5},
    )
    
    return retriever

