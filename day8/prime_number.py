def prime(n):
    if n==1:
        return False
    elif n==2:
        return True
    else:
        for i in range(2,n):
            if n%i==0:
                return False
        return True
    
a = int(input("enter your number :"))
b = prime(a)

if b == True:
    print(f"the number {a} is a prime number")
else:
    print(f"the number {a} is not a prime number")