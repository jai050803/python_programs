#python program to find if a number is prime or not



n = int(input("enter the number you want to check : "))
prime = True
for i in range(2,n):
    if n%i == 0:
        prime = False
        
if prime == True:
    print(f"the number {n} is a prime number")
else:
    print(f"The number {n} is not a prime number")