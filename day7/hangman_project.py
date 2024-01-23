#task1 - pick a random word from the list of words
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word = ["hello", "balloon" , "adventure", "bookkeeper", "andaman", "narendra", "delhi"]

chosen_word = random.choice(word)
print(chosen_word)
display = []
for i in range(len(chosen_word)):
    display.append("_")
for i in chosen_word:
    while "_" in display:
        guess = input("\n\n\nGuess a letter : ").lower()
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess

        
end_of_game = False
        
