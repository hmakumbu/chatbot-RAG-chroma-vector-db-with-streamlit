import os
import chromadb
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv
from langchain.schema import Document

load_dotenv()
CHROMA_DATA_PATH = os.getenv("CHROMA_DATA_PATH")

def create_vector_db(documents):
    chroma_client = chromadb.PersistentClient(path=CHROMA_DATA_PATH)
    embedding_model = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    vector_db = Chroma(
        client=chroma_client,
        collection_name="local-rag",
        embedding_function=embedding_model
    )
    vector_db.add_documents(documents)
    return vector_db


