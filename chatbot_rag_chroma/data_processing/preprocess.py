import json
from langchain.schema import Document
import os
from load import load_text
from langchain.text_splitter import RecursiveCharacterTextSplitter
from dotenv import load_dotenv
from typing import List, Dict, Any

# Load environment variables from the .env file

load_dotenv()

DATA_PATH = os.getenv("DATAPATH")

# def process_documents(documents: List[str]) -> List[Document]:
#     text_splitter = RecursiveCharacterTextSplitter(separators=["\n\n", "\n", ". ", " ", ""], chunk_size=40, chunk_overlap=0)
#     docs = text_splitter.split_documents(documents)
#     return docs

def process_documents(documents):
    text_splitter = RecursiveCharacterTextSplitter(separators=["\n\n", "\n", ". ", " ", ""], chunk_size=300, chunk_overlap=30)
    docs = text_splitter.split_documents(documents)

    return docs

data = load_text(DATA_PATH)
doc = process_documents(data)

#print(doc[2])

# for doc in processed_docs:
#     print(f"Metadata: {doc['metadata']}, Content: {doc['page_content']}")


# # # Retrieve the DATA_PATH from environment variables
# DATA_PATH = os.getenv("DATAPATH")

# if DATA_PATH is None:
#     print("DATA_PATH is not set in the environment variables.")
# elif not os.path.exists(DATA_PATH):
#     print(f"File not found at path: {DATA_PATH}")
# else:
#     with open(DATA_PATH, "r") as f:
#         data = txt.load(f)

#     # Process the JSON data into a list of texts (paragraphs + headers)
#     def extract_text(data: List[Dict]) -> List[str]:
#         texts = []
#         for document in data:
#             paragraphs = document.get("paragraphs", [])
#             headers = [header.get("text") for header in document.get("headers", [])]
#             texts.extend(paragraphs + headers)
#         texts = [text for text in texts if text.strip()]
#         return texts

#     # Wrap each text in a Document object and split the documents
#     def process_text(texts: List[str]) -> List[Document]:
#         documents = [Document(page_content=text) for text in texts]  # Wrap each text in Document
#         text_splitter = RecursiveCharacterTextSplitter(separators=["\n\n", "\n", ". ", " ", ""], chunk_size=400, chunk_overlap=0)
#         docs = text_splitter.split_documents(documents)
#         return docs

    # Process the data if it was loaded successfully
    # documents =extract_text(data)
    # dic_doc = process_text(documents)
    # print(len(dic_doc))


# # Ensure the correct file path is constructed
# DATA_PATH = os.path.join(os.getcwd(), "data_processing", "website_structure.json")

# # Check if the file exists before trying to open it
# if os.path.exists(DATA_PATH):
#     with open(DATA_PATH, "r") as f:
#         data = json.load(f)
# else:
#     print(f"File not found at path: {DATA_PATH}")


# def process_document(data):
#     texts = []
#     for document in data:
#         paragraphs = document.get("paragraphs", [])
#         headers = [header.get("text") for header in document.get("headers", [])]
#         texts.extend(paragraphs + headers)
#     texts = [text for text in texts if text.strip()]

#     return texts
#     #return [Document(page_content=text) for text in texts]


# # Process the data if it was loaded successfully
# if 'data' in locals():
#     processed_documents = process_document(data)
#     print(processed_documents)