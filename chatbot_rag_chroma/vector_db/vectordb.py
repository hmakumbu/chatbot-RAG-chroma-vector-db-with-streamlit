import os
import chromadb
from dotenv import load_dotenv
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.schema import Document

# Load environment variables
load_dotenv()

# Chroma database path
CHROMA_DATA_PATH = os.path.join(os.getcwd(), "chroma_data")

def create_vector_db(documents: list[Document]):
    """
    Creates a vector database using Chroma with persistent storage.

    Args:
    documents (list[Document]): List of documents to be added to the vector database.

    Returns:
    vector_db: The initialized vector database.

    Raises:
    ValueError: If a tenant or database connection issue occurs.
    RuntimeError: If a general error occurs during vector database creation.
    """
    try:
        # Initialize PersistentClient for Chroma
        chroma_client = chromadb.PersistentClient(path=CHROMA_DATA_PATH)

        # Initialize the embedding model
        embedding_model = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

        # Initialize the Chroma vector database
        vector_db = Chroma(
            client=chroma_client,
            collection_name="local-rag",
            embedding_function=embedding_model
        )

        # Add documents to the vector database
        vector_db.add_documents(documents)

        return vector_db

    except ValueError as e:
        raise ValueError(f"Could not connect to ChromaDB: {e}")

    except Exception as e:
        raise RuntimeError(f"An error occurred while creating the vector database: {e}")


