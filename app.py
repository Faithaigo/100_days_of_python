import random

hangman_pics = [
    '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''',
    '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',
    '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',
    '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
    '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
    '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',
    '''
  +---+
  |   |
      |
      |
      |
      |
========='''
]

d_list = ["aardvark", "baboon", "camel"]

print("""
    /=======================\\
    | Welcome to Hangman!!! |
    \\=======================/
  """)

chosen_word = random.choice(d_list)

placeholder = ''

for place in chosen_word:
    placeholder += '_'

print(placeholder)

lives = 6
game_over = False
correct_letters = []
while not game_over:
    print(f'You have {lives}/6 lives left')
    guess = input("Guess a letter ").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    display = ''
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += '_'
    print(f"Word to guess: {display}")

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        lives -= 1

    if lives == 0:
        game_over = True
        print(f'It was {chosen_word} You loose')

    if '_' not in display:
        game_over = True
        print('Game over')

    print(hangman_pics[lives])
