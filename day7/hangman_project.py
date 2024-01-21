#task1 - pick a random word from the list of words
import random
word = ["hello", "balloon" , "adventure", "bookkeeper", "andaman", "narendra", "delhi"]

chosen_word = random.choice(word)
display = []
for i in range(len(chosen_word)):
    display.append("_")
for i in display:
    print(i, end=" ")

#task2 - take input from the user
guess = input("\n\n\nGuess a letter :").lower()


for i in chosen_word:
    if guess == i:
        print("correct")
    else:
        print("Wrong")

