
# Bible Verse Scraper V1
BVS reforms scraped verse from [this Korean website](https://missa.cbck.or.kr/DailyMissa/20210503) to fit **one line for each verse** format.

___
## Motivation
As a sunday school teacher, preparing for weekly class involved copying verses and reformatting. Doing this every week led me to plan this program where I will get automatically reformatted text scraped from a website after inputing a desired date.  
This project was ispired by [this tutorial](https://realpython.com/beautiful-soup-web-scraper-python/) for scraping web pages and modifying texts.

---
## How to Use
Type ``
python ./main.py
`` in terminal to run, and follow the shown instructions. You might need to download **Beautiful Soup** to run.

---
## Implementation Details
I have used...
- **requests** to get the html containing the target verse from the [website](https://missa.cbck.or.kr/DailyMissa/20210503)
- **Beautiful Soup** to convert html to text
- **Datetime** to obtain local(machine) date to handle request for today's verse
- **re (regular expression)** to validate and fail the input date before requesting the acutual html

___
## Future Plans for BVS
I am planning to build a website to make this program accessible anywhere. I will have to resolve copyright issues before making this any more public.

---
## Copyright
All content was scraped without consent from [this website](https://missa.cbck.or.kr/DailyMissa/20210503)

---
## 한국어 설명
이 프로그램은 [이 웹사이트](https://missa.cbck.or.kr/DailyMissa/20210503) 에서 복음 부분을 **한 줄 당 하나의 구절** 포멧으로 바꾸어 줍니다.  
``python ./main.py  ``로 실행할 수 있고 안내를 따라하면 됩니다. 