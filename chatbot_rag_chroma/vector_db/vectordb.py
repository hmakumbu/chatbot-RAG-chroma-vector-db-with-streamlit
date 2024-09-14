import os
import chromadb
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain_community.vectorstores import Chroma
# from chatbot_rag_chroma.data_processing.preprocess import process_document
from dotenv import load_dotenv
from langchain.schema import Document

# Load environment variables from .env file
load_dotenv()

# Get the Chroma data path from environment variables
CHROMA_DATA_PATH = os.getcwd() + "/chroma_data"

def create_vector_db(documents: list[Document]):
    try:
        # Initialize the PersistentClient for the Chroma vector database
        chroma_client = chromadb.PersistentClient(path=CHROMA_DATA_PATH)

        # Initialize the embedding model
        embedding_model = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

        # Initialize the Chroma vector database with the persistent client and documents
        vector_db = Chroma(
            client=chroma_client,
            collection_name="local-rag",
            embedding_function=embedding_model
        )

        # Add the documents to the vector database
        vector_db.add_documents(documents)

        return vector_db

    except ValueError as e:
        # Handle errors related to tenant or database connection
        raise ValueError(f"Could not connect to ChromaDB: {e}")

    except Exception as e:
        # General error handling for unexpected issues
        raise RuntimeError(f"An error occurred while creating the vector database: {e}")


