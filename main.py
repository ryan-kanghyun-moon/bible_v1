import string_mod as string_mod
import soup as soup

URL ='https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
URL1 = 'https://maria.catholic.or.kr/mi_pr/missa/missa.asp'
URL2 = 'http://mobile2.catholic.or.kr/web/bible/bible_jeol.asp?gubuncode=new2&bbl_code=147&bbl_chptNum=1&flag=1'
URL3 = 'https://missa.cbck.or.kr/DailyMissa/20210503'


def main():
    
        
    url = URL3
    
    verse = string_mod.get_verse(soup.trim_text(soup.init_string(url)))

    print(verse)

    
if __name__ == "__main__":
    main()