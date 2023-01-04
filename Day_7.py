#Step 2

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


word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
player_lives = 7
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

blanked = []
blankedStr = ""
letter_position = -1
for letter in chosen_word:
  blanked.append("_")

while chosen_word != blankedStr:
  guess = input("Guess a letter: ").lower()

  for letter in chosen_word:
    letter_position += 1
    if letter == guess:
      blanked[letter_position] = letter
    
  if guess not in chosen_word:
    player_lives -= 1
    print(stages[player_lives])
    if player_lives == 0:
      print("End of Game you Lose!!")
      break
  letter_position = -1
  
    
  blankedStr = "".join(blanked)
  print(blankedStr)
  if "_" not in blanked:
    print("End of Game you Win!!")


    # else:
    #   player_lives -= 1
    #   if player_lives == 0:
    #    
    #     print("End of Game you Lose!!")

    #Step 5

import random, hangman_words, hangman_art
#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
print(hangman_art.logo)

#Testing code
# print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"
guessed = []
while not end_of_game:
  while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in guessed:
      print(f"{guess} has already been guessed!")
      break
    else:
      guessed.append(guess)

    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    
    #Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    print(hangman_art.stages[lives])