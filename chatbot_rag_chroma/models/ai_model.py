from langchain_community.chat_models import ChatOllama
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
# Charger les variables d'environnement depuis le fichier .env
# load_dotenv()

# # Initialiser le modèle LLM
# local_model = "mistral"
# llm = ChatOllama(model=local_model)

load_dotenv()

groq_api_key = os.getenv("API_Key_groq")

llm = ChatGroq(temperature=0, groq_api_key=groq_api_key, model_name="mixtral-8x7b-32768")