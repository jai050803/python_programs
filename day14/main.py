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
    print(f"\nThe competition is between {name1['name']} vs {name2['name']}")

    answer = input("\nWho has more followers? Type 'a' or 'b' :").lower()

    follower1 = name1['follower_count']
    follower2 = name2['follower_count']

    if answer == "a":
        if follower2 > follower1:
            print(f"\nYou are wrong. your final score is {score}")
            break
        else:
            score += 1
            print(f"\nYou are right. Your score is {score}")
    elif answer == "b":
        if follower2 > follower1:
            score += 1
            print(f"\nYou are right. Your score is {score}")
           
        else:
            print(f"\nYou are wrong. Your final score is {score}")
            break
    
