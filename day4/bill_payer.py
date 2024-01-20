import random

print("\n....decide who will pay the bill......\n")

name = input("enter the names separated by space :")
lst = list(map(str, name.split()))

random_payer = random.randint(0,len(lst)-1)

print(f"{lst[random_payer]} will pay the bill")
    