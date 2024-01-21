print("\n....fizzbuzz game....\n")

print("if number is divisible by 3.. print fizz")
print("if number is divisible by 5.. print buzz")
print("if number is divisible by 3 and 5.. print fizzbuzz")

n = int(input("enter the number :"))

for i in range(1,n+1):
    if i%3 == 0 and i%5 == 0:
        print("fizzbuzz")
    elif i%3 == 0:
        print("fizz")
    elif i%5 == 0:
        print("buzz")
    else:
        print(i)