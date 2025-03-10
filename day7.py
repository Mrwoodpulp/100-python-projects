import random
import sys

Stages = ['''
 +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''' ,'''
 +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''','''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
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
=========''','''
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
  +---+
  |   |
      |
      |
      |
      |
========='''

]

Word_List = ["aardvark", "baboon", "camel" ]

Lives = 6
chosen_word = random.choice(Word_List)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)

for position in range(1,word_length+1):
    placeholder += "_"
print(placeholder)


game_over = False
Correct_Letters = []
while not game_over:
    guess = input("Guess a letter from the word:\n").lower()

    if guess in Correct_Letters:
        print(f"You have already Guessed {guess}")

    Display = ""
    for letter in chosen_word:
        if letter == guess:
            Display += letter
            Correct_Letters.append(letter)
        elif letter in Correct_Letters:
            Display += letter
        else:
            Display += "_"

    print(Display)

    if guess not in chosen_word:
        Lives -= 1
        print(f"You Guessed {guess}, that's not in the word. You lose a life.")
        if Lives == 0:
            game_over = True

            print(f"The word was {chosen_word}")
            print("You Lose")


    if "_" not in Display:
        game_over = True
        print("You Win.")

    print(Stages[Lives])

