# Blackjack game ..........
import random
print("\n.........Welcome to blackjack game.......\n")

def winner(player_total, computer_total):
    if player_total > 21:
        print("its a bust! you lost")
    elif player_total < computer_total:
        print("You lost")
    elif player_total == computer_total:
        print("Its a draw")
    else:
        print("You won!!")
    
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

game = True
while game == True:
    start = input("\ntype y to start the the game else type n :").lower()
    if start == "y":
        game = True
    else:
        game = False
        break
    [x,y] = random.choices(cards, k=2)
    [a,b] = random.choices(cards, k=2)
    print(f"Your cards :{[x,y]}")
    print(f"Computer's first card :{b}")

    ask = input("Type y to get another card and type n to pass :")
    if ask == "y":
        z = random.choice(cards)
        print(f"your final hand :{[x,y,z]}")
        player_total = sum([x,y,z])
        computer_total =sum([a,b]) 
        print(f"computer's final hand :{[a,b]}")
        winner(player_total, computer_total)
    else:
        print(f"Your final hand : {[x,y]}")
        print(f"computer's final hand :{[a,b]}")
        player_total = sum([x,y]) 
        computer_total =sum([a,b])
        winner(player_total, computer_total)





