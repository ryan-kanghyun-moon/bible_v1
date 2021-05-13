import requests, pprint
from bs4 import BeautifulSoup

URL ='https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
URL1 = 'https://maria.catholic.or.kr/mi_pr/missa/missa.asp'
URL2 = 'http://mobile2.catholic.or.kr/web/bible/bible_jeol.asp?gubuncode=new2&bbl_code=147&bbl_chptNum=1&flag=1'
URL3 = 'https://missa.cbck.or.kr/DailyMissa/20210502'
page = requests.get(URL3)
soup = BeautifulSoup(page.content, 'html.parser')

def main():
   
   
    string = repr(soup.text)
    
    string = string[str.find(string, "복음 환호송"): str.find(string, "그리스도님 찬미합니다") + len("그리스도님 찬미합니다.")]

    print(string)
   

    
if __name__ == "__main__":
    main()