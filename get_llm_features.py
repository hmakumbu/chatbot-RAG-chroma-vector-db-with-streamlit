import streamlit as st
from chatbot_rag_chroma.vectordb import create_vector_db
from chatbot_RAG_chroma_vector_db.chatbot_rag_chroma.models.ai_model import llm
#from langchain.prompts import PromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough
from chatbot_RAG_chroma_vector_db.chatbot_rag_chroma.data_processing.load import load_pdf
from chatbot_RAG_chroma_vector_db.chatbot_rag_chroma.data_processing.preprocess import process_document
import os
from chatbot_RAG_chroma_vector_db.chatbot_rag_chroma.prompts.prompt import QUERY_PROMPT

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

