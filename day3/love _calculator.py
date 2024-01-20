print("\n.... Try this love calculator to know how much compatible you are together....\n")

print("\n...Try out....\n")

name1 = input("\nEnter Your name :")
name2 = input("Enter your partners Name :")

name1.lower(), name2.lower()
count = 0
for i in name1:
    if i == "l" or i == "o" or i == "v" or i == "e":
        count += 20
    if i == "t" or i == "r" or i == "u":
        count += 5
    for j in name2:
        if i == j:
            count += 10
        if j == "l" or j == "o" or j == "v" or j == "e":
            count += 20
        if j == "t" or j == "r" or j == "u":
            count += 5
        
print(f" Your score is {count}")

if count <= 30:
    print("Oops! You need to make your relationship more strong")
elif count in range(30,70):
    print("you are good together")
elif count in range (70,100):
    print("You are a perfect couple")
else:
    print("Your relationship is made in heaven")
        
        
            
