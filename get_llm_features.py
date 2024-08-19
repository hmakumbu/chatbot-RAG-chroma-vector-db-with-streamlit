import os
import json
from dotenv import load_dotenv
from chatbot_RAG_chroma_vector_db.chatbot_rag_chroma.vector_db.vectordb import create_vector_db
from chatbot_RAG_chroma_vector_db.chatbot_rag_chroma.data_processing.preprocess import process_document
from chatbot_RAG_chroma_vector_db.chatbot_rag_chroma.models.ai_model import llm
from chatbot_RAG_chroma_vector_db.chatbot_rag_chroma.prompts.prompt import QUERY_PROMPT
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough

load_dotenv()

DATA_PATH = os.getenv("DATAPATH")
file_path = os.path.join(DATA_PATH, "website_structure.json")

def get_chain(QUERY_PROMPT, llm):
    chain = (
        {"context": RunnablePassthrough(), "question": RunnablePassthrough()}
        | QUERY_PROMPT
        | llm
        | StrOutputParser()
    )
    return chain

def get_retriever():
    with open(file_path, "r") as f:
        data = json.load(f)
    
    documents = process_document(data)
    vector_db = create_vector_db(documents)
    
    retriever = vector_db.as_retriever(
        search_type="similarity_score_threshold",
        search_kwargs={"k": 3, "score_threshold": 0.5},
    )
    
    return retriever
