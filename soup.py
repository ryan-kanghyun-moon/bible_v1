import requests, pprint
from bs4 import BeautifulSoup

#get html from website and return text version
def init_string(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup.text

# trim text to workable substring
def trim_text(string):
    return string[str.find(string, "복음 환호송"): str.find(string, "그리스도님 찬미합니다") + len("그리스도님 찬미합니다.")]
    
