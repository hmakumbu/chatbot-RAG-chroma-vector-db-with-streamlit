import os
import chromadb
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain_community.vectorstores import Chroma
from chatbot_RAG_chroma_vector_db.chatbot_rag_chroma.data_processing.preprocess import process_document
from dotenv import load_dotenv
from langchain.schema import Document


# Load environment variables from .env file
load_dotenv()

# Get the Chroma data path from environment variables
CHROMA_DATA_PATH = os.getenv("CHROMA_DATA_PATH")

def create_vector_db(documents : list[Document]):
    # Initialize the PersistentClient for the Chroma vector database
    chroma_client = chromadb.PersistentClient(path=CHROMA_DATA_PATH)

    # Load and process the PDF to get the documents
    # documents = process_document()

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




#=====================



# import os
# import chromadb
# from langchain.embeddings import SentenceTransformerEmbeddings
# from langchain_community.vectorstores import Chroma
# from preprocess import process_documents_from_multiple_sources
# from dotenv import load_dotenv
# from langchain_community.embeddings import FastEmbedEmbeddings

# # Charger les variables d'environnement depuis le fichier .env
# load_dotenv()

# # Obtenir le chemin du dossier de données Chroma depuis les variables d'environnement
# CHROMA_DATA_PATH = os.getenv("FOLDER_PATH")

# def create_vector_db():
#     # Initialiser le PersistentClient pour la base de données Chroma
#     chroma_client = chromadb.PersistentClient(path=CHROMA_DATA_PATH)

#     # Charger et traiter les PDF pour obtenir les documents
#     pdf_paths = ["microsoft_annual_report_2022.pdf", "WEF_The_Global_Cooperation_Barometer_2024.pdf"]
#     documents = process_documents_from_multiple_sources(pdf_paths)

#     # Initialiser le modèle d'embedding
#     embedding_model = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

#     # Initialiser la base de données vectorielle Chroma avec le client persistant et les documents

#     #vector_db = Chroma.from_documents(documents=documents, embedding=FastEmbedEmbeddings())
#     vector_db = Chroma(
#         client=chroma_client,
#         collection_name="local-rag",
#         embedding_function=embedding_model
#     )

#     # Ajouter les documents à la base de données vectorielle
#     vector_db.add_documents(documents)

#     return vector_db

