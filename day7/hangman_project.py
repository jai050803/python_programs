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

lives = 6

word = ["hello", "balloon" , "adventure", "bookkeeper", "andaman", "narendra", "delhi"]
end_of_game = False
chosen_word = random.choice(word)
word_length = len(chosen_word)
print(f'Pssst, the solution is {chosen_word}.')
display = []

for _ in range(word_length):
  display += "_"

while not end_of_game:
  guess = input("Guess a letter: ").lower()
  for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter
    
  if guess not in chosen_word:
      lives -= 1
      if lives == 0:
        end_of_game = True
        print("You lose.")
            
  print(f"{' '.join(display)}")
    
  if "_" not in display:
    end_of_game = True
    print("You win.")
        
  print(stages[lives])
      