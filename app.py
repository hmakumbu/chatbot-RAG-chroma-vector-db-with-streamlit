import streamlit as st
from chatbot_rag_chroma.ai_model import llm
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough
import os
from dotenv import load_dotenv
from chatbot_rag_chroma.prompt import QUERY_PROMPT
from get_llm_features import get_retriever, get_chain

load_dotenv()

DATA_PATH = os.getenv("DATAPATH")

# Function to handle questions
def handle_question(retriever, chain):
    question_text = st.session_state.new_question_input
    if question_text:
        # Retrieve relevant documents
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

# Main function for the application
def main():
    st.title("ChatBox App DataBeez")
    st.write("Ask questions about the Platform DataBeez.")

    if "history" not in st.session_state:
        st.session_state.history = []

    if "new_question_input" not in st.session_state:
        st.session_state.new_question_input = ""

    for i, (question, response) in enumerate(st.session_state.history):
        st.write(f"**Question {i+1}:** {question}")
        st.write(f"**Response:** {response}")
        st.write("---")

    st.text_input("Ask your question:", key="new_question_input", on_change=lambda: handle_question(retriever, chain))

# Run the main function
if __name__ == "__main__":
    file_path = os.path.join(DATA_PATH, "fake_document_calendrier_LMS.pdf")
    retriever = get_retriever(file_path)
    chain = get_chain(QUERY_PROMPT=QUERY_PROMPT, llm=llm)
    
    main()

#=======================================================================================