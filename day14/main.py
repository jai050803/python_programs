from game_data import data
import random

print("...Welcome to the Higher or Lower Game....\n")

print("....Guess who has more followers....\n")


right = True
while True:
    name1 = random.choice(data)
    name2 = random.choice(data)
    print(f"The competition is between {name1['name']} vs {name2['name']}")

    answer = input("Who has more followers? Type 'a' or 'b' :").lower()

    follower1 = name1['follower_count']
    follower2 = name2['follower_count']
    if answer == "a":
        if follower2 > follower1:
            print("You are wrong.")
            right = False
        else:
            print("You are right you won this round...")
    elif answer == "b":
        if follower2 > follower1:
            print("You are right. You won this round...")
        else:
            print("You are wrong")
            right = False
