import os
from dotenv import load_dotenv
from pypdf import PdfReader

# Load environment variables from .env file
load_dotenv()

# Get the data path from environment variables
#DATA_PATH = os.getenv("DATAPATH")

def load_pdf(file_path):
    # Specify the PDF file name
    #file_path = os.path.join(DATA_PATH, "microsoft_annual_report_2022.pdf")
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    # Read pdf
    reader = PdfReader(file_path)
    pdf_texts = [p.extract_text().strip() for p in reader.pages]
    # Filter the empty strings
    data = [text for text in pdf_texts if text]
    return data
