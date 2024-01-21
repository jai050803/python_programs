print("\n....the program will calculate the average height of n number of students.....\n")

print("enter the height of each person in cm separated by space ...")

name = input().split()
for n in name:
    name[name.index(n)] = int(n)
sum = 0
total = 0
for i in name:
    sum += i
    total += 1
average = round(sum/total)
print(f"average height is {average}cm")
    
    