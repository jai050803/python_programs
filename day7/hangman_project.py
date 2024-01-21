#task1 - pick a random word from the list of words
import random
word = ["hello", "balloon" , "adventure", "bookkeeper", "andaman", "narendra", "delhi"]

chosen_word = random.choice(word)
#task2 - take input from the user
guess = input().lower()

if guess in chosen_word:
    print(True)
else:
    print(False)

