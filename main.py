import requests, pprint
from bs4 import BeautifulSoup

URL ='https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
URL1 = 'https://maria.catholic.or.kr/mi_pr/missa/missa.asp'
URL2 = 'http://mobile2.catholic.or.kr/web/bible/bible_jeol.asp?gubuncode=new2&bbl_code=147&bbl_chptNum=1&flag=1'
URL3 = 'https://missa.cbck.or.kr/DailyMissa/20210502'
def main():
    page = requests.get(URL3)
    # pprint.pprint(page.content)
    
    print('안녕하세요')
    soup = BeautifulSoup(page.content, 'html.parser')
    # result = soup.find("복음")
    # print(result.prettify())
    # print(soup.prettify())
    # print(repr(soup.text.strip()))
    # print(soup.text)
    string = repr(soup.text)
    # print(string)

    string = string[str.find(string, "복음 환호송"): str.find(string, "그리스도님 찬미합니다") + len("그리스도님 찬미합니다.")]

    print(string)
    # print(str.find(string, "교회는 유다"))

    # print(string[:-2])
    
    # print(str.find("안녕하세요", "하"))

    
if __name__ == "__main__":
    main()