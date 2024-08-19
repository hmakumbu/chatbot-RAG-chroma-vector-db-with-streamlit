import requests
from bs4 import BeautifulSoup
import json

# List of URLs to analyze
urls = [
    'https://aimsammi.org/',
    'https://aimsammi.org/about-ammi-2/',
    'https://aimsammi.org/admission-2/',
    'https://aimsammi.org/events/',
    'https://aimsammi.org/blog-2/',
]

def analyze_page_to_json(url):
    page_data = {
        'url': url,
        'title': '',
        'headers': [],
        'paragraphs': [],
        'links': [],
        'images': []
    }
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        html_content = response.content
        soup = BeautifulSoup(html_content, 'html.parser')
        
        page_data['title'] = soup.title.string if soup.title else "No title"
        headers = soup.find_all(['h1', 'h2', 'h3'])
        for header in headers:
            page_data['headers'].append({'tag': header.name, 'text': header.text.strip()})
        paragraphs = soup.find_all('p')
        for p in paragraphs:
            page_data['paragraphs'].append(p.text.strip())
        links = soup.find_all('a')
        for link in links:
            page_data['links'].append({'href': link.get('href'), 'text': link.text.strip()})
        images = soup.find_all('img')
        for img in images:
            page_data['images'].append({'src': img.get('src'), 'alt': img.get('alt')})

    except requests.exceptions.RequestException as e:
        print(f"Error accessing {url}: {e}")

    return page_data

all_pages_data = [analyze_page_to_json(url) for url in urls]

with open('website_structure.json', 'w') as json_file:
    json.dump(all_pages_data, json_file, indent=4)
