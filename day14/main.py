from game_data import data
import random

print("...Welcome to the Higher or Lower Game....\n")

print("....Guess who has more followers....\n")

name = random.choice(data)
print(name['name'])