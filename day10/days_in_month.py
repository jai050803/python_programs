from leapyear import leap_year

def days_in_month(year,month):
    month_days=[31,28,31,30,31,30,31,31,30,31,30,31]
    if month ==2 and leap_year(year) == "leap Year":
        return 29
    else:
        return month_days[month-1]

year = int(input("enter the year : "))
month = int(input("enter the month : "))
days = days_in_month(year,month)
print(f"in given month we have {days} days")