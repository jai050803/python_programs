import random

print("\n.........Your virtual Toss........\n")

print("whats your call? heads or tails ?\n")
choice = input("type here :")
choice = choice.lower()

result = random.randint(0,1)
coin = 0
if result == 0:
    coin = "heads"
else:
    coin = "tails"
    
if choice == coin:
    print(f"its {coin} ,congratulations you won the toss")
else:
    print(f"oops you lost.. its {coin}")