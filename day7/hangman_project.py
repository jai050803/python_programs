#task1 - pick a random word from the list of words
import random
word = ["hello", "balloon" , "adventure", "bookkeeper", "andaman", "narendra", "delhi"]

chosen_word = random.choice(word)

display = []
for i in range(len(chosen_word)):
    display.append("_")

#task2 - take input from the user
guess = input("\n\n\nGuess a letter : ").lower()

#task3 - check if the letter is in the word and if yes replace it in the display list
for i in range(len(chosen_word)):
    if chosen_word[i] == guess:
        display[i] = guess

print(display)
