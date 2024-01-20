print("\n.... find the treasure......\n")   

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("\n....start the game.. write start")
start = input()

if start == "start":
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure hidden on a mountain cave....") 
    name = input("enter your name :")
    print("your adenture starts when you find a map while going to school. \nthe map shows a red mark near the mountain lake \n")
    print("you need to answer the following questions while on your way..\n")
    print(f'''when you enter the cave.. you encounter a wise owl.. \nthe wise owl said \"hey you! where you going?\"
{name} : I want to find the tressure hidden inside the cave 
wise owl : okay.. but first you need to answer my question.. if wrong you are dead 
{name} : okay ask me.. i am ready for it..
wise owl : Tell me.. "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?
''')
    
    answer = input("enter your answer here :")
    if answer == "echo" or answer == "ECHO" or answer == "Echo":
        print('''wise owl : bravo!! you got it right.. you can go ahead''')
        print('''\nAs you go ahead, you meet a mysterious old man who asks you another question:
Old Man: "The more you take, the more you leave behind. What am I?"''')
        
        answer2 = input("Enter your answer here: ")
        if answer2.lower() == "footsteps":
            print('''Old Man: "Impressive! You may proceed further."''')
            print('''\nContinuing your journey, you find a locked door. To open it, you need to solve another riddle:
I fly without wings. I cry without eyes. Wherever I go, darkness follows me. What am I?"''')
            
            answer3 = input("Enter your answer here: ")
            if answer3.lower() == "cloud":
                print('''\nThe door opens, and you find yourself facing a talking parrot.
Parrot: "You're doing well, adventurer! Here's your next challenge:
I have keys but no locks. I have space but no room. You can enter, but you can't go inside. What am I?"''')
            
                answer4 = input("Enter your answer here: ")
                if answer4.lower() == "keyboard":
                    print('''Parrot: "You're clever! Move ahead and face the next trial."''')
                    print('''\nAs you venture deeper, you encounter a shadowy figure:
Figure: "The more you look at it, the less you see. What is it?"''')
                    
                    answer5 = input("Enter your answer here: ")
                    if answer5.lower() == "darkness":
                        print('''\nFigure: "Well done! You're on the right path. The treasure awaits you."''')
                        print("\n\nCongratulations, adventurer! You have successfully navigated through the challenges and found the hidden treasure.")
                    else:
                        print("\nOops! Your journey ends here. Game over!")
                
                else:
                    print("\nOops! Your journey ends here. Game over!")
            else:
                print("\nOops! Your journey ends here. Game over!")
        else:
            print("\nOops! Your journey ends here. Game over!")
    
    else:
        print('''\nOOPS! you are wrong little fellow! now get ready to die..''')
        print("\n\n game over!!")
    
    

