from datetime import datetime
import re

def today():
    date = datetime.today()
    yr = date.year 
    mo = date.month
    day = date.day
    today = yr * 10000 + mo * 100 + day
    # print(today)
    return today

def verify_date(date):
    # TODO
    
    # verify = r'^202[1-3](((0[13578])|(1[02]))((0[1-9])|([12]\d)|(3[01])))|(02((0[1-9])|(1\d)|(2[1-9])))|(((0[469])|(11))((0[1-9])|([12]\d)|(30)))$'
    # match = re.match(verify, date)
    # return match != None
    # year: ^20[1-3]
    ver_31s = r'202[1-3](0[13578]|1[02])(0[1-9]|[12]\d|3[01])$'
    ver_28s = r'202[1-3]02(0[1-9]|1\d|2[1-9])$'
    ver_30s = r'202[1-3](0[469]|11)(0[1-9]|[12]\d|30)$'
    return re.match(ver_31s, date) != None or re.match(ver_28s, date) != None or re.match(ver_30s, date) != None 
