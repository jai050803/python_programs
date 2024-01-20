print("\n....your own rock paper scissors game.....\n")

print("..choose your weapon .. 0 for rock 1 for paper and 2 for scissor")

rock ="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

import random
    
player = int(input("\nchoose :"))
if player in range(0,3):
    print("your choice ..")
    weapon2 = ""
    if player == 0:
        weapon2 = "rock"
        print(rock)
    elif player == 1:
        weapon2 = "paper"
        print(paper)
    elif player == 2:
        weapon2 = "scissors"
        print(scissor)
    
opponent = random.randint(0,2)
if player in range(0,3):
    print("computer choice ..")
    weapon1 = ""
    if opponent == 0:
        weapon1 = "rock"
        print(rock)
    elif opponent == 1:
        weapon1 = "paper"
        print(paper)
    elif opponent==2:
        weapon1 = "scissors"
        print(scissor)

if player == 0 and opponent == 2:
    print(f"you won.. you chose {weapon2} and computer chose {weapon1}")
elif player == 0 and opponent == 1:
    print(f"you lost.. you chose {weapon2} and computer chose {weapon1}")
elif player == 1 and opponent == 0:
    print(f"you won.. you chose {weapon2} and computer chose {weapon1}")
elif player == 1 and opponent == 2:
    print(f"you lost.. you chose {weapon2} and computer chose {weapon1}")
elif player == 2 and opponent == 0:
    print(f"you lost.. you chose {weapon2} and computer chose {weapon1}")
elif player == 2 and opponent == 1:
    print(f"you won.. you chose {weapon2} and computer chose {weapon1}")
elif player == opponent:
    print(f"draw... both chose {weapon1}")

else:
    print("you chose invalid number")