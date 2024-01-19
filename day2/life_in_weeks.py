#life in weeks program
print("\n\n..............welcome to the life in weeks program..................... \n\n")
print("the program calculates how many weeks you have left to live based on your age \n\n")
age = int(input("enter your age :"))

years_remaining = 90 - age

days = years_remaining * 365

weeks = years_remaining * 52

months = years_remaining * 12

print(f"\n\n you have {days} days which means {weeks} weeks and  {months} in months left to live..\n\n enjoy your life..")