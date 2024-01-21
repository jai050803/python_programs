print("\n..program to find sum of even numbers from 2 to n....\n")

n = int(input("enter the number :"))
sum = 0
for i in range(2,n+1,2):
    sum += i

print(f"Sum of even number from 2 to {n} is {sum}")