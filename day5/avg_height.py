print("\n....the program will calculate the average height of n number of students.....\n")

print("enter the height of each person in cm separated by space ...")

name = input().split()
sum = 0

for i in range(0,len(name)):
    sum += int(name[i])
    
average =sum/len(name)



print(f"average height is {average}cm")
    
    