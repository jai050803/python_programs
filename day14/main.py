from game_data import data
import random

print("...Welcome to the Higher or Lower Game....\n")

print("....Guess who has more followers....\n")

score = 0
right = True
while True:
    name1 = random.choice(data)
    name2 = random.choice(data)
    if name1 == name2:
        name2 = random.choice(data)
    print(f"The competition is between {name1['name']} vs {name2['name']}")

    answer = input("Who has more followers? Type 'a' or 'b' :").lower()

    follower1 = name1['follower_count']
    follower2 = name2['follower_count']

    if answer == "a":
        if follower2 > follower1:
            print("You are wrong.")
            break
        else:
            print("You are right you won this round...")
            score += 1
    elif answer == "b":
        if follower2 > follower1:
            print("You are right. You won this round...")
            score += 1
        else:
            print("You are wrong")
            break
    
