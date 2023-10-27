import os
from bs4 import BeautifulSoup


def search_conversations(directory, query):
    results = {}
    print(f"Searching in directory: {directory} for query: {query}")  # Debug line

    for filename in os.listdir(directory):
        if filename.endswith('.html'):
            with open(os.path.join(directory, filename), 'r', encoding='utf-8') as f:
                content = f.read()
                soup = BeautifulSoup(content, 'html.parser')
                text_content = soup.get_text()
                print(f"Checking file: {filename}")  # Debug line

                if query.lower() in text_content.lower():
                    results[filename] = extract_snippet(text_content, query)
                    print(f"Match found in: {filename}")  # Debug line
                else:
                    print(f"No match in: {filename}")  # Debug line

    return results


def extract_snippet(text, query, surrounding=30):
    """Extract a snippet of text surrounding the first occurrence of the query."""
    index = text.lower().find(query.lower())
    if index == -1:
        return None
    start_index = max(0, index - surrounding)
    end_index = min(len(text), index + len(query) + surrounding)
    return text[start_index:end_index]
