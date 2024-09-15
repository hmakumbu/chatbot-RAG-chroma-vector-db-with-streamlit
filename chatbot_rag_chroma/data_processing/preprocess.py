import os
from dotenv import load_dotenv
from typing import List
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document

# Load environment variables
load_dotenv()

def process_documents(documents: List[Document]):
    """
    Processes documents by splitting them into smaller chunks.

    Args:
    documents (List[Document]): List of documents to be processed.

    Returns:
    List[Document]: List of split documents.
    """
    text_splitter = RecursiveCharacterTextSplitter(separators=["\n\n", "\n", " "], chunk_size=400, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)

    return docs
