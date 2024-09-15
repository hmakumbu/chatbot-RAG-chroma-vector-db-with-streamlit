import streamlit as st
from dotenv import load_dotenv
from chatbot_rag_chroma.models.ai_model import llm
from chatbot_rag_chroma.prompts.prompt import prompt

import os
from get_llm_features import get_retriever, get_chain
from datetime import datetime


load_dotenv()
#DATA_PATH = os.getenv("DATAPATH")
#file_path = os.path.join(DATA_PATH, "website_structure.json")

DATA_PATH = os.getenv("DATAPATH")

def handle_question(retriever, chain):
    question_text = st.session_state.new_question_input
    if question_text:
        relevant_documents = retriever.get_relevant_documents(question_text)
        context_text = " ".join([doc.page_content for doc in relevant_documents if hasattr(doc, 'page_content')])
        if not context_text.strip():
            context_text = "No relevant context found in the provided document."
        inputs = {"context": context_text, "question": question_text}
        results = chain.invoke(inputs)
        if results:
            response = results if isinstance(results, str) else results[0]
            st.session_state.history.append((question_text, response))
            st.session_state.new_question_input = ""
            # st.experimental_rerun()

            if st.button('Rerun'):
                st.rerun

def save_conversation(question, response):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_path= os.getcwd()+ "/data/conversation_history.txt"
    with open(file_path, "a") as file:
        file.write(f"Date et Heure: {timestamp}\n")
        file.write(f"User: {question}\n")
        file.write(f"Bot: {response}\n\n")

def main():
    st.title("ChatBot App AMMI Programm")
    with st.sidebar:

        st.sidebar.markdown("**Important Announcement.**")
        #st.sidebar.write("")
        st.sidebar.text("""Hello everyone,


Dear students of the AMMI program,
we are excited to present this test version 
of the AMMI chatbot application. This tool is designed 
to help you communicate with the program, 
providing information about its content and related details.

We have launched this test version to gather feedback 
that will help us improve the application. 
All questions and responses are recorded and analyzed 
to identify areas that need adjustment before the release. 
For now, the project is accessible to a limited group. 
If the chatbot provides an incorrect response, 
please kindly provide the correct answer in return. 
Your contribution is crucial to the success of this project.

The chatbot is built using the RAG system and prompt engineering. 
Your feedback will help us explore the integration 
of additional concepts to enhance its performance.

Thank you for your active participation and support!.""")
      

    if "history" not in st.session_state:
        st.session_state.history = []

    if "new_question_input" not in st.session_state:
        st.session_state.new_question_input = ""

    for i, (question, response) in enumerate(st.session_state.history):
        st.write(f"**Question {i+1}:** {question}")
        st.write(f"**Response:** {response}")
        st.write("---")

        save_conversation(question,response)

    st.text_input("Ask your question:", key="new_question_input", on_change=lambda: handle_question(retriever, chain))

if __name__ == "__main__":
    retriever = get_retriever()
    chain = get_chain(prompt=prompt, llm=llm)
    main()