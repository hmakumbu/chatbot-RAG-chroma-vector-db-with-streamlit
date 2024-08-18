import streamlit as st
from chatbot_rag_chroma.vectordb import create_vector_db
from chatbot_rag_chroma.ai_model import llm
#from langchain.prompts import PromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough
from chatbot_rag_chroma.load import load_pdf
from chatbot_rag_chroma.preprocess import process_document
import os
from chatbot_rag_chroma.prompt import QUERY_PROMPT

# Initialize the Chroma vector database
DATA_PATH = os.getenv("DATAPATH")

file_path = os.path.join(DATA_PATH, "fake_document_calendrier_LMS.pdf")


# Create the chain

def get_chain(QUERY_PROMPT, llm):
    chain = (
        {"context": RunnablePassthrough(), "question": RunnablePassthrough()}
        | QUERY_PROMPT
        | llm
        | StrOutputParser()
    )
    return chain

def get_retriever(file_path):

    data = load_pdf(file_path)
    list_Documents = process_document(data)

    vector_db = create_vector_db(list_Documents)


    # Initialize the retriever
    retriever = vector_db.as_retriever(
        search_type="similarity_score_threshold",
        search_kwargs={"k": 3, "score_threshold": 0.5},
    )
    
    return retriever

