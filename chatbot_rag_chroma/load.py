import os
from dotenv import load_dotenv
import json
from pypdf import PdfReader
from scrapegraphai.graphs import SmartScraperGraph
import nest_asyncio

nest_asyncio.apply()

# Load environment variables from .env file
load_dotenv()

# Configuration dictionary for the graph
graph_config = {
    "llm": {
        "model": "ollama/llama3",  # Specify the model for the LLM
        "temperature": 0.5,  # Set temperature for generating detailed output
        "format": "json",  # Set output format as JSON for structured data
        "base_url": "http://localhost:11434",  # Base URL for Ollama
    },
    "embeddings": {
        "model": "ollama/nomic-embed-text",  # Specify the model for embeddings
        "base_url": "http://localhost:11434",  # Base URL for Ollama
    },
    "verbose": True,  # Enable verbose mode for debugging
}

# Initialize SmartScraperGraph with prompt, source, and configuration
smart_scraper_graph = SmartScraperGraph(
    prompt='''
Extract detailed information from the following sections of the website:

- **Home**:
  - **Description**: Extract the main description of the program.
  - **Partnership**: List any partnerships mentioned.
  - **Acceptance Rate**: Provide the acceptance rate if available.
  - **Countries**: Mention the number of countries represented by the students.
  - **Number of Female Students**: Provide the percentage or number of female students.
  - **Graduation Rate**: Mention the graduation rate.
  - **Students Mentored**: Provide the number of students mentored.
  - **Latest News**: List the latest news articles, including the title, date, time, description, and image metadata (alt text and src).

- **About**:
  - **Description**: Extract the description of the African Master's in Machine Intelligence (AMMI).
  - **Our Centers**: Mention the details of the centers associated with AMMI.
  - **About AMMI**: Provide detailed information about the AMMI program.
  - **AMMI Leadership**: List key leadership figures and their roles.
  - **Our Lecturers**: Extract information about the lecturers involved in the program.
  - **Our Students**: Provide details about the student body, including any notable statistics.

- **Admissions**:
  - **Why AMMI**: Explain why students should consider AMMI.
  - **Admission Requirements**: List the requirements for admission.
  - **Academic History**: Provide details about the academic background expected.
  - **References**: Mention any reference requirements.
  - **Personal Statement**: Extract the guidelines for the personal statement.
  - **Background Summary**: Provide a summary of the background expected for applicants.
  - **FAQs**: List frequently asked questions, along with their answers.

- **Events**:
  - **Upcoming Events**: Extract details about upcoming events, including the title, date, time, description, and image metadata (alt text and src).

- **Blog**:
  - **Blog Posts**: List all blog posts, including the title, author, publication date, content summary, and image metadata (alt text and src).

For each section, include all available metadata, including alt text and src for images, and container information if present.
'''
,
    source="https://aimsammi.org/",  # URL to scrape
    config=graph_config  # Pass the scraper configuration
)

# Run the SmartScraperGraph and store the result
result = smart_scraper_graph.run()

# Convert result to JSON format with indentation
output = json.dumps(result, indent=2)

# Split the JSON string into lines
line_list = output.split("\n")

# Print each line of the JSON separately
for line in line_list:
    print(line)


# # Get the data path from environment variables
# #DATA_PATH = os.getenv("DATAPATH")

# def load_pdf(file_path):
#     # Specify the PDF file name
#     #file_path = os.path.join(DATA_PATH, "microsoft_annual_report_2022.pdf")
#     if not os.path.exists(file_path):
#         raise FileNotFoundError(f"The file {file_path} does not exist.")
    
#     # Read pdf
#     reader = PdfReader(file_path)
#     pdf_texts = [p.extract_text().strip() for p in reader.pages]
#     # Filter the empty strings
#     data = [text for text in pdf_texts if text]
#     return data
#
#playwright 
#scrapegraphai==0.9.0b7 
#nest_asyncio