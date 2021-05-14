def is_integer(n):
    try:
        int(n)
    except ValueError:
        return False
    else:
        return True


def get_verse(raw_bib):

    # gets rid of '\n'
    lines = raw_bib.splitlines()
    i = 0
    # find the first int = intro and make it a seperate line
    while not is_integer(lines[i][:1]):
        i += 1
    lines[i] = "\n" + lines[i] + "\n"

    i += 1

    # iterate through lines and make each verse a seperate line
    while i < len(lines):
        if is_integer(lines[i][:1]):
            lines[i] = "\n" + lines[i]
        i += 1
    
    # joins and trims 
    verse = ''.join(lines)
    verse = verse[str.find(verse, ">") + 1:]
   
    
    return verse