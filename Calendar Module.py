import calendar as c 
month, date, year = map(int,input().split())
print(c.day_name[c.weekday(year,month,date)].upper())
