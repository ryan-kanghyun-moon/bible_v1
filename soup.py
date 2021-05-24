import requests
from bs4 import BeautifulSoup

# URL ='https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
# URL1 = 'https://maria.catholic.or.kr/mi_pr/missa/missa.asp'
# URL2 = 'http://mobile2.catholic.or.kr/web/bible/bible_jeol.asp?gubuncode=new2&bbl_code=147&bbl_chptNum=1&flag=1'
# URL3 = 'https://missa.cbck.or.kr/DailyMissa/20210516'

# trim text to workable substring
def trim_text(string):
    return string[str.find(string, "복음 환호송"): str.find(string, "그리스도님 찬미합니다") + len("그리스도님 찬미합니다.")]

#get html from website and return text version
def init_string(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    return trim_text(soup.text)

# returns a new url with given date
def get_url(date):
    return "https://missa.cbck.or.kr/DailyMissa/" + str(date)