import get_date as date
import soup as soup
import string_mod as string_mod


#ui for getting date or today
def print_today():
    url = soup.get_url(date.today())
    verse = string_mod.get_verse(soup.init_string(url))
    return verse


def print_given_date():
    # TODO
    return "oops not there yet"

def fail_inp():
    print("Invalid input, try again")
    main_ui()

def main_ui():
    inp = input("t for today or d for manual input: ")
    inputs = {
        't': print_today,
        'd': print_given_date
    }
    func = inputs.get(inp, fail_inp)
    print(func())
