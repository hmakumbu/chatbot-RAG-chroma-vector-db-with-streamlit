from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document

def process_document(data : list[str]) -> list[Document]:

   # data = load_pdf()
    # Convert the text data into a list of Document objects
    documents = [Document(page_content=doc.strip()) for doc in data if doc.strip()]
    
    # Initialize text splitter
    text_splitter = RecursiveCharacterTextSplitter(separators=["\n\n", "\n", ". ", " ", ""], chunk_size=1000, chunk_overlap=0)
    
    # Split documents into chunks
    chunks = text_splitter.split_documents(documents)
    return chunks
