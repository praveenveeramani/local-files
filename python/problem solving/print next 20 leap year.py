year=int(input("enter the year;"))
leap_year=[]
while len(leap_year)<20:
    if (year%4==0 and year%100!=0) or year%400==0:
        leap_year.append(year)
    year=year+1
print("20 leap year is",leap_year)
