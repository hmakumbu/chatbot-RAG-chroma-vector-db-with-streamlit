import os
import json
# from scraping_module import scrape_page_to_json
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
# from de 

load_dotenv()

# DATA_PATH = os.getcwd()+ "data/ammi_program.txt"
DATA_PATH = os.getenv("DATAPATH")

def load_text(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")

    loader = TextLoader(file_path)
    documents = loader.load()


    return documents



# print(load_text(DATA_PATH))

# Scrape URLs and save JSON
# def load_scraped_data():
#     urls = [
#         'https://aimsammi.org/',
#         'https://aimsammi.org/about-ammi-2/',
#         'https://aimsammi.org/admission-2/',
#         'https://aimsammi.org/events/',
#         'https://aimsammi.org/blog-2/',
#     ]

#     scraped_data = [scrape_page_to_json(url) for url in urls]

#     # Save scraped data to a JSON file
#     json_file_path = os.path.join(os.getenv("DATA_PATH"), 'scraped_data.json')
#     with open(json_file_path, 'w') as json_file:
#         json.dump(scraped_data, json_file, indent=4)

#     return json_file_path, scraped_data