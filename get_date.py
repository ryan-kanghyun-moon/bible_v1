from datetime import datetime

def today():
    date = datetime.today()
    yr = date.year 
    mo = date.month
    day = date.day
    today = yr * 10000 + mo * 100 + day
    # print(today)
    return today
    

if __name__ == "__main__":
    today()