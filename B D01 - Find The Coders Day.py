year = int(input())
leap = 0
if year%4 == 0:
    leap = 1
if year > 1918:
    if year % 100 == 0:
        leap = 0
    if year % 400 == 0:
        leap = 1
if year==1918:
    print("26.09.",year,sep="")  
else:
    if leap==0:
        print("13.09.",year,sep="")
    else:
        print("12.09.",year,sep="")
