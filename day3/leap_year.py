a = int(input("enter the year : "))
def leap_year(year):
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                return "leap Year"
            else:
                return "not a leap Year"
        else:
            return "leap Year"
    else:
        return "not a leap Year"

print("the year is ",leap_year(a))