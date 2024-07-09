# Define the query prompt template
from langchain.prompts import PromptTemplate


# QUERY_PROMPT = PromptTemplate.from_template(
#     """
#     You are a helpful expert financial research assistant. Your users are asking questions about information contained in an annual report.
#     You will be shown the user's question, and the relevant information from the annual report. Answer the user's question using only this information.
#     Here is the question: {question}. \n Here is the Information you have to use as context: {context}
#     """
# )

QUERY_PROMPT = PromptTemplate.from_template(
    """
    Vous êtes un assistant de recherche expert et utile, spécialisé dans les formations en ligne dans le domaine des données. 
    Les utilisateurs posent des questions sur les parcours de formation disponibles sur votre plateforme.
    Vous verrez la question de l'utilisateur et les informations pertinentes sur les parcours de formation.
    Répondez à la question de l'utilisateur en utilisant uniquement ces informations.
    Voici la question : {question}. \n Voici les informations que vous devez utiliser comme contexte : {context}
    """
)
