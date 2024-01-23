#task1 - pick a random word from the list of words
import random
import word_list
import hangman

l = hangman.logo
print(l)

stages = hangman.stages
lives = 6
word = word_list.word_list
end_of_game = False
chosen_word = random.choice(word)
word_length = len(chosen_word)
display = []

for _ in range(word_length):
  display += "_"

while not end_of_game:
  guess = input("Guess a letter: ").lower()
  
  if guess in display:
    print(f"you have already guessed the {guess}")
  for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter
    
  if guess not in chosen_word:
    print(f"you have guessed the letter {guess} wrong so you lose a life")
    lives -= 1
    if lives == 0:
      print("You lose.")
      end_of_game = True
  print(f"{' '.join(display)}")
    
  if "_" not in display:
    print("You win.")
    end_of_game = True
    
        
  print(stages[lives])
      