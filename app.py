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
            st.experimental_rerun()

def save_conversation(question, response):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_path= os.getcwd()+ "/data/conversation_history.txt"
    with open(file_path, "a") as file:
        file.write(f"Date et Heure: {timestamp}\n")
        file.write(f"User: {question}\n")
        file.write(f"Bot: {response}\n\n")

def main():
    st.title("ChatBox App AMMI Programm")
    st.write("Ask questions about the Platform DataBeez.")

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