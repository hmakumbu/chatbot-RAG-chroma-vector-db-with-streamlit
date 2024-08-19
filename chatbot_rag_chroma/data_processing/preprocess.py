import json
from langchain.schema import Document

def process_document(data):
    texts = []
    for document in data:
        paragraphs = document.get("paragraphs", [])
        headers = [header.get("text") for header in document.get("headers", [])]
        texts.extend(paragraphs + headers)
    texts = [text for text in texts if text.strip()]
    return [Document(page_content=text) for text in texts]

with open("website_structure.json", "r") as f:
    data = json.load(f)

processed_documents = process_document(data)
