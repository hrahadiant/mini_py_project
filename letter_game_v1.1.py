# only guess a single letter
# only guess an alphabetic
# user can play again
# strikes max up to 7
# draw guesses letter, spaces, and strikes

import random

words = [
    'cow',
    'cat',
    'crocodile',
    'lion',
    'tiger',
    'mouse',
    'goat',
    'giraffe',
    'elephant',
    'dear',
    'eagle',
    'bear'
]

while True:
    start = input("Press enter to play or q to quit ").lower()
    if start == 'q':
        break

    secret_word = random.choice(words)
    bad_guesses = []
    good_guesses = []

    while len(bad_guesses) < 7 and len(good_guesses) != len(list(secret_word)):

        # draw the letters
        for letter in secret_word:
            if letter in good_guesses:
                print(letter, end='')
            else:
                print('.', end='')
        print('')
        print('Strikes {}/7'.format(len(bad_guesses)))

        guess = input("Guess a letter: ")

        if len(guess) != 1:
            print("You can only guess a single letter.")
            continue
        elif guess in good_guesses or guess in bad_guesses:
            print("You already guess that letter.")
            continue
        elif not guess.isalpha():
            print("You can only guess a letter.")
            continue

        if guess in secret_word:
            good_guesses.append(guess)
            if len(good_guesses) == len(list(secret_word)):
                print("You win! The word was {}".format(secret_word))
                break
        else:
            bad_guesses.append(guess)

    else:
        print("You lost! The secret word was {}".format(secret_word))
        continue
