import get_date as get_date
import soup as soup
import string_mod as string_mod
import sys

def print_date(date):
    print("verse for" + str(date) + ": \n")

def print_verse(url):
    verse = string_mod.get_verse(soup.init_string(url))
    print(verse)

#ui for getting date or today
def print_today():
    today = get_date.today()
    print_date(today)
    url = soup.get_url(get_date.today())
    print_verse(url)

def print_given_date():
    date = input('Enter date (format:YYYYMMDD), x to exit: ')

    if date == 'x' :
        main_ui()
    if get_date.verify_date(date):
        print_date(date)    
        print_verse(soup.get_url(date))
    else:
        print('WRONG INPUT!')
        print_given_date()


def fail_inp():
    print("Invalid input, try again\n")
    main_ui()

def exit():
    print("thanks!\n")
    sys.exit()
    

def main_ui():
    inp = input("t for today or d for manual input, x to exit: ")
    inputs = {
        'x': exit,
        't': print_today,
        'd': print_given_date
    }
    func = inputs.get(inp, fail_inp)
    func()
