print("\n.....roller coaster ride ...... \n")
height = int(input("enter your height in cm : "))
age = int(input("enter your age : "))

if height >= 120:
    if age >= 18:
        print("you can ride the rollercoaster and you need to pay 100 rupees")
    else:
        print("you can ride the rollercoaster and you need to pay 50 rupees")
else:
    print("you can't ride the rollercoaster")