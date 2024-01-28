import random

print("\n....Welcome to your number guessing game....\n")
print("\nI am thinking of a number from 1 to 100.. can you guess it?")
answer = random.randint(1,101)
def attempts(ask):
    if ask == "easy":
        attempt = 10
        return attempt
    else:
        attempt = 5
        return attempt 
ask = input("\nchoose the difficulty level \"easy\" or \"hard\" :")
turns = attempts(ask)
print(f"you have got {turns} chances to guess the correct answer !!")
i = 1
while i <= turns:
    guess = int(input("enter your guess :"))
    if guess > answer:
        print("too high..")
    elif guess < answer:
        print("too low..")
    else:
        print("\ncongrats!! you got it right..")
        break
    i += 1
    print(f"\nYou have {turns - i+1} chances left")
if i == turns+1:
    print(f"\noops! you ran out of your chances... you lose. the right answer was {answer}")
    