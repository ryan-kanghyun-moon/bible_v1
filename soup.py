import requests, pprint
from bs4 import BeautifulSoup


def init_string(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup

def soup_to_trim_text(soup):
    string = soup.text
    string = string[str.find(string, "복음 환호송"): str.find(string, "그리스도님 찬미합니다") + len("그리스도님 찬미합니다.")]
    return string
