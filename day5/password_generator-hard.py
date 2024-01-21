print("\n.. generate your random password using random password generator...\n")
import random

print("How many letters you want in your password ?")
n = int(input("type here :"))

print("how many symbols you want in your password ?")
a = int(input("type here :"))

print("how many numbers you want in your password ?")
b = int(input("type here :"))
password_lst = []
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

for i in range(0,n):
    letter = random.randint(0,51)
    password_lst.append(letters[letter])

for j in range(0,a):
    symbol = random.randint(0,8)
    password_lst.append(symbols[symbol])

for k in range(0,b):
    number = random.randint(0,9)
    password_lst.append(numbers[number])

random.shuffle(password_lst)
print(password_lst)
str1 = ""
for i in password_lst:
    str1 += str(i)
print(f"Your random password is {str1}")