import requests, pprint
from bs4 import BeautifulSoup

URL ='https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
URL1 = 'https://maria.catholic.or.kr/mi_pr/missa/missa.asp'
URL2 = 'http://mobile2.catholic.or.kr/web/bible/bible_jeol.asp?gubuncode=new2&bbl_code=147&bbl_chptNum=1&flag=1'
URL3 = 'https://missa.cbck.or.kr/DailyMissa/20210502'
page = requests.get(URL3)
soup = BeautifulSoup(page.content, 'html.parser')

def insert_n(verse, i):
    return verse[:i] + "\n" + verse[i:]


def is_integer(n):
    try:
        int(n)
    except ValueError:
        return False
    else:
        return True

def get_start(v):
    return v[str.find(v, ",") + 1: str.find(v, "-")]

def get_verse(raw_bib):
    no_n = ''.join(raw_bib.splitlines())
   
    verse = no_n[str.find(no_n, ">") + 1:]

    # i = str.find(verse, "-") + 1
    
    # while is_integer(verse[i]): 
    #     i += 1
    
    # verse = insert_n(verse, i)
    # i += 1

    
    
    s = get_start(verse)
    i = str.find(verse, "," + s) + 2
    print(str(i) + "\n")
    
    temp = insert_n(verse[i:], str.find(verse[i:], s))
    verse = verse[:i] + temp
    
    


    while i < len(verse):
        if is_integer(verse[i]) and not is_integer(verse[i-1]):
            verse = insert_n(verse, i)
            i += 1
        i += 1

    return verse


def main():
   
   

    string = soup.text

    string = string[str.find(string, "복음 환호송"): str.find(string, "그리스도님 찬미합니다") + len("그리스도님 찬미합니다.")]
    
    verse = get_verse(string)

    print(verse)

    
if __name__ == "__main__":
    main()