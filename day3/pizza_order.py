print("\n...Thank for choosing Python Pizza Deliveries....\n")

print("\n... menu .....\n")
print("1. Corn cheese pizza \n2. Capsicum \n3. paneer \n4. Onion \n5. tomato")
print("\n........type the number to chose your pizza ........\n")

order = int(input("enter the number of pizza you want to choose :"))
size = input("what size S(small) M(medium or L(large)) ?\nType here :")

if order == 1:
    if size == "S":
        price = 120
        print("Corn cheese pizza of small size costs rupees 120")
    elif size == "M":
        price = 150
        print("Corn cheese pizza of medium size costs rupees 150")
    elif size == "L":
        price = 200
        print("Corn cheese pizza of large size costs rupees 200")

elif order == 2:
    if size == "S":
        price = 130
        print("Capsicum pizza of small size costs rupees 130")
    elif size == "M":
        price = 160
        print("Capsicum pizza of medium size costs rupees 160")
    elif size == "L":
        price = 210
        print("Capsicum pizza of large size costs rupees 210")

elif order == 3:
    if size == "S":
        price = 140
        print("Paneer pizza of small size costs rupees 140")
    elif size == "M":
        price = 170
        print("Paneer pizza of medium size costs rupees 170")
    elif size == "L":
        price = 220
        print("Paneer pizza of large size costs rupees 220")

elif order == 4:
    if size == "S":
        price = 110
        print("Onion pizza of small size costs rupees 110")
    elif size == "M":
        price = 140
        print("Onion pizza of medium size costs rupees 140")
    elif size == "L":
        price = 190
        print("Onion pizza of large size costs rupees 190")

elif order == 5:
    if size == "S":
        price = 100
        print("Tomato pizza of small size costs rupees 100")
    elif size == "M":
        price = 130
        print("Tomato pizza of medium size costs rupees 130")
    elif size == "L":
        price = 180
        print("Tomato pizza of large size costs rupees 180")

else:
    print("Invalid pizza number")
    
print("You want to order ? \nType Y for yes and N for no :")
confirm = input()

if confirm == "Y" or confirm == "y":
    address = input("Type the delivery address :")
    print(f" your order will be delievered to you in 30 minutes on your address {address} and your bill is {price}")

else:
    print("Thanks for reaching out to us.... hope to see you soon again")