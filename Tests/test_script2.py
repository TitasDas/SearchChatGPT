from bs4 import BeautifulSoup

with open("C:/Users/TD/Downloads/chatgpt_conversations/chat.html", 'r', encoding='utf-8') as f:
    content = f.read()
    soup = BeautifulSoup(content, 'lxml')  # Change parser to lxml
    text_content = soup.get_text()

print(text_content)